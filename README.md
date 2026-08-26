# ResQ AI Plugins

Internal AI plugin marketplaces maintained by ResQ.

## Available plugins

- `resq`: Connects supported AI clients to the ResQ production MCP API.

## Claude Code

Validate the marketplace:

    claude plugin validate .

Add the marketplace:

    claude plugin marketplace add getresq/resq-ai-plugins

Install the ResQ plugin:

    claude plugin install resq@resq-internal

## Codex

Add the marketplace:

    codex plugin marketplace add getresq/resq-ai-plugins

Install the ResQ plugin:

    codex plugin add resq@resq-internal

## ChatGPT

Register the production MCP endpoint from <https://chatgpt.com/plugins>:

    https://api.getresq.com/mcp

Test the OAuth connection in a personal workspace, then have a workspace administrator publish the tested plugin to the intended team roles. The complete handoff checklist is in `plugins/resq/ADMIN_SETUP.md`.

## Local validation

From the repository root, add the local marketplace and install the plugin:

    claude plugin marketplace add ./
    claude plugin install resq@resq-internal

    codex plugin marketplace add ./
    codex plugin add resq@resq-internal

Complete the ResQ OAuth flow when prompted, then confirm the ResQ MCP tools are available.

## Publishing updates

1. Modify the plugin files.
2. Increment the version in both platform manifests:
   - `plugins/resq/.claude-plugin/plugin.json`
   - `plugins/resq/.codex-plugin/plugin.json`
3. Keep the two manifest versions identical and use semantic versioning.
4. Validate both platforms again.
5. Open and merge a pull request into the default branch.

Use patch releases for fixes, minor releases for backward-compatible features, and major releases for breaking changes.
