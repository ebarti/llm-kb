#!/usr/bin/env node

async function readStdin() {
  const chunks = [];
  for await (const chunk of process.stdin) {
    chunks.push(chunk);
  }
  return Buffer.concat(chunks).toString("utf8");
}

function compactItem(item) {
  if (!item || typeof item !== "object") {
    return item;
  }
  const summary = { type: item.type };
  if ("status" in item) {
    summary.status = item.status;
  }
  if (item.type === "command_execution") {
    summary.command = item.command;
    summary.exit_code = item.exit_code;
  } else if (item.type === "file_change") {
    summary.changes = item.changes;
  } else if (item.type === "web_search") {
    summary.query = item.query;
  } else if (item.type === "error") {
    summary.message = item.message;
  }
  return summary;
}

function present(value) {
  return value !== undefined && value !== null && value !== "";
}

try {
  const { Codex } = await import("@openai/codex-sdk");
  const payload = JSON.parse(await readStdin());

  const clientOptions = {};
  if (present(payload.apiKey)) {
    clientOptions.apiKey = payload.apiKey;
  }
  if (present(payload.baseUrl)) {
    clientOptions.baseUrl = payload.baseUrl;
  }
  if (present(payload.codexPathOverride)) {
    clientOptions.codexPathOverride = payload.codexPathOverride;
  }
  if (present(payload.codexHome)) {
    clientOptions.env = { ...process.env, CODEX_HOME: payload.codexHome };
  }

  const codex = new Codex(clientOptions);
  const threadOptions = {
    workingDirectory: payload.cwd,
    skipGitRepoCheck: Boolean(payload.skipGitRepoCheck),
    sandboxMode: payload.sandboxMode,
    approvalPolicy: payload.approvalPolicy,
    networkAccessEnabled: Boolean(payload.networkAccessEnabled),
    webSearchMode: payload.webSearchMode,
  };
  if (present(payload.model)) {
    threadOptions.model = payload.model;
  }
  if (present(payload.modelReasoningEffort)) {
    threadOptions.modelReasoningEffort = payload.modelReasoningEffort;
  }

  const thread = codex.startThread(threadOptions);
  const turn = await thread.run(payload.prompt);
  const output = {
    finalResponse: turn.finalResponse || "",
    usage: turn.usage || null,
    threadId: thread.id,
    items: Array.isArray(turn.items) ? turn.items.map(compactItem) : [],
  };

  process.stdout.write(`${JSON.stringify(output)}\n`);
} catch (error) {
  const message = error && error.stack ? error.stack : String(error);
  process.stderr.write(`${message}\n`);
  process.exitCode = 1;
}
