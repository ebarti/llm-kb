#!/usr/bin/env python3
"""
Plugin framework for the LLM knowledge base.

Discovers, loads, and executes plugins from tools/plugins/available/.
Each plugin is a .py file that exports a register() function returning
a dict mapping hook names to callables.

Usage:
    python3 tools/plugins/framework.py run <hook_name> [args...]
    python3 tools/plugins/framework.py list
    python3 tools/plugins/framework.py enable <plugin>
    python3 tools/plugins/framework.py disable <plugin>

Hook points:
    pre_ingest   - Before a new source is ingested (args: file path)
    post_ingest  - After a new source is ingested (args: file path)
    pre_compile  - Before wiki compilation starts
    post_compile - After wiki compilation finishes
    pre_query    - Before a query is executed (args: query string)
    post_query   - After a query returns (args: query string, result path)
    on_lint      - During linting / health checks
"""

import importlib.util
import json
import os
import sys
import traceback

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PLUGINS_DIR = os.path.join(os.path.dirname(__file__), "available")
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

VALID_HOOKS = [
    "pre_ingest", "post_ingest",
    "pre_compile", "post_compile",
    "pre_query", "post_query",
    "on_lint",
]


def load_config():
    """Load the plugin configuration."""
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    return {"enabled": []}


def save_config(config):
    """Save the plugin configuration."""
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)
        f.write("\n")


def discover_plugins():
    """Scan the available/ directory for plugin files with a register() function."""
    plugins = {}
    if not os.path.isdir(PLUGINS_DIR):
        return plugins
    for fname in sorted(os.listdir(PLUGINS_DIR)):
        if not fname.endswith(".py") or fname.startswith("_"):
            continue
        name = fname[:-3]
        path = os.path.join(PLUGINS_DIR, fname)
        try:
            spec = importlib.util.spec_from_file_location(f"plugin_{name}", path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            if hasattr(mod, "register") and callable(mod.register):
                plugins[name] = mod
        except Exception:
            print(f"[plugin] Warning: failed to load {fname}")
            traceback.print_exc()
    return plugins


def get_registry():
    """Build a registry of enabled plugins mapped to their hooks."""
    config = load_config()
    enabled = set(config.get("enabled", []))
    all_plugins = discover_plugins()
    registry = {}
    for name, mod in all_plugins.items():
        if name not in enabled:
            continue
        try:
            hooks = mod.register()
            if isinstance(hooks, dict):
                registry[name] = hooks
        except Exception:
            print(f"[plugin] Warning: register() failed for {name}")
            traceback.print_exc()
    return registry


def run_hook(hook_name, args=None):
    """Run all enabled plugins registered for the given hook."""
    if args is None:
        args = []
    if hook_name not in VALID_HOOKS:
        print(f"[plugin] Unknown hook: {hook_name}")
        print(f"[plugin] Valid hooks: {', '.join(VALID_HOOKS)}")
        return False

    registry = get_registry()
    ran = 0
    errors = 0
    for plugin_name, hooks in registry.items():
        if hook_name in hooks:
            fn = hooks[hook_name]
            try:
                print(f"[plugin] Running {plugin_name}.{hook_name}...")
                fn(ROOT, *args)
                ran += 1
            except Exception as e:
                print(f"[plugin] Error in {plugin_name}.{hook_name}: {e}")
                traceback.print_exc()
                errors += 1

    print(f"[plugin] Hook '{hook_name}': {ran} plugin(s) ran, {errors} error(s)")
    return errors == 0


def list_plugins():
    """List all available plugins and their status."""
    config = load_config()
    enabled = set(config.get("enabled", []))
    all_plugins = discover_plugins()

    if not all_plugins:
        print("No plugins found in available/")
        return

    print(f"{'Plugin':<25} {'Status':<10} {'Hooks'}")
    print("-" * 65)
    for name, mod in sorted(all_plugins.items()):
        status = "enabled" if name in enabled else "disabled"
        try:
            hooks = mod.register()
            hook_list = ", ".join(sorted(hooks.keys())) if isinstance(hooks, dict) else "?"
        except Exception:
            hook_list = "(error)"
        print(f"{name:<25} {status:<10} {hook_list}")


def enable_plugin(name):
    """Enable a plugin by name."""
    all_plugins = discover_plugins()
    if name not in all_plugins:
        print(f"Plugin '{name}' not found. Available: {', '.join(sorted(all_plugins.keys()))}")
        return False
    config = load_config()
    enabled = config.get("enabled", [])
    if name not in enabled:
        enabled.append(name)
        config["enabled"] = enabled
        save_config(config)
    print(f"Plugin '{name}' enabled.")
    return True


def disable_plugin(name):
    """Disable a plugin by name."""
    config = load_config()
    enabled = config.get("enabled", [])
    if name in enabled:
        enabled.remove(name)
        config["enabled"] = enabled
        save_config(config)
        print(f"Plugin '{name}' disabled.")
    else:
        print(f"Plugin '{name}' was not enabled.")
    return True


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "list":
        list_plugins()
    elif cmd == "enable" and len(sys.argv) >= 3:
        enable_plugin(sys.argv[2])
    elif cmd == "disable" and len(sys.argv) >= 3:
        disable_plugin(sys.argv[2])
    elif cmd == "run" and len(sys.argv) >= 3:
        hook_name = sys.argv[2]
        args = sys.argv[3:]
        success = run_hook(hook_name, args)
        sys.exit(0 if success else 1)
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
