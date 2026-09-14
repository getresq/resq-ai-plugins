# ResQ AI Plugins

Connect Claude Code, Codex, and ChatGPT to your authorized ResQ facilities and work orders.

You need a ResQ account with access to an eligible organization. Each user connects through ResQ OAuth; the package contains no credentials. See the [plugin guide](plugins/resq/README.md) for account setup, example requests, and reconnecting.

## Available plugins

- `resq`: Connects supported AI clients to the ResQ production MCP API.

## Claude Code

Run these commands from the root of this directory.

Validate the marketplace and plugin:

    claude plugin validate .
    claude plugin validate ./plugins/resq

Add the marketplace:

    claude plugin marketplace add ./

Install the ResQ plugin:

    claude plugin install resq@resq-internal

## Codex

From the root of this directory, add the marketplace:

    codex plugin marketplace add ./

Install the ResQ plugin:

    codex plugin add resq@resq-internal

## ChatGPT

Register the production MCP endpoint from <https://chatgpt.com/plugins>:

    https://api.getresq.com/mcp

Complete the ResQ OAuth flow when prompted and select an organization your
account can access. A workspace administrator can manage availability for other
workspace members; each user signs into ResQ separately.

## Publishing updates

1. Modify the plugin files.
2. Increment the version in both platform manifests:
   - `plugins/resq/.claude-plugin/plugin.json`
   - `plugins/resq/.codex-plugin/plugin.json`
3. Keep the two manifest versions identical and use semantic versioning.
4. Validate both platforms again.
5. Open and merge a pull request into the default branch.

Use patch releases for fixes, minor releases for backward-compatible features, and major releases for breaking changes.

## Help and policies

- [ResQ support](https://support.getresq.com/)
- [Privacy policy](https://www.getresq.com/privacy-policy)
- [Terms of service](https://www.getresq.com/terms-of-service)
