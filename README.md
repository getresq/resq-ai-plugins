# ResQ AI Plugins

Connect Anthropic's Claude Code and OpenAI's Codex and ChatGPT to your authorized ResQ facilities and work orders.

You need a ResQ account with access to an eligible organization. Each user connects through ResQ OAuth; the package contains no credentials. See the [plugin guide](plugins/resq/README.md) for account setup, example requests, and reconnecting.

## Available plugins

ResQ publishes this plugin for two AI providers:

| Provider | Products | Marketplace ID | Marketplace file |
| --- | --- | --- | --- |
| Anthropic | Claude Code | `resq-claude` | `.claude-plugin/marketplace.json` |
| OpenAI | Codex and ChatGPT | `resq-openai` | `.agents/plugins/marketplace.json` |

Both integrations use the plugin identifier `resq` and connect to the ResQ production
MCP API. ResQ is the plugin publisher and authentication provider.

## Anthropic: Claude Code

Add the GitHub marketplace and install the ResQ plugin:

    claude plugin marketplace add getresq/resq-ai-plugins
    claude plugin install resq@resq-claude

## OpenAI: Codex

Add the GitHub marketplace and install the ResQ plugin:

    codex plugin marketplace add getresq/resq-ai-plugins
    codex plugin add resq@resq-openai

Complete ResQ authentication when prompted, then start a new thread.

Your ResQ account permissions determine which data you can access.

## OpenAI: ChatGPT

Follow the [ChatGPT setup instructions](plugins/resq/README.md#openai-chatgpt) to register
`https://api.getresq.com/mcp` in developer mode and connect through ResQ OAuth.
A workspace administrator can manage availability for other workspace members.

## Repository structure

This repository packages the connection to ResQ. MCP tools and OAuth behavior are
implemented by the service at `https://api.getresq.com/mcp`.

| File | Purpose |
| --- | --- |
| `.claude-plugin/marketplace.json` | Anthropic Claude Code catalog for installing from this repository. |
| `.agents/plugins/marketplace.json` | OpenAI catalog, display metadata, and installation/authentication policies. |
| `plugins/resq/.claude-plugin/plugin.json` | Anthropic Claude plugin identity and version. |
| `plugins/resq/.codex-plugin/plugin.json` | OpenAI plugin identity, version, branding, and MCP reference. |
| `plugins/resq/.mcp.json` | Shared production MCP connection. |
| `plugins/resq/assets/` | Official branding and source provenance. |

Both catalogs point to `./plugins/resq` relative to the repository root. The
Codex source type `local` means the plugin is bundled in this repository, including
when the marketplace is downloaded from GitHub.

See the [Claude marketplace documentation](https://code.claude.com/docs/en/plugin-marketplaces)
and [OpenAI packaging documentation](https://developers.openai.com/plugins/build/plugins#marketplace-metadata)
for the two catalog formats.

## Local validation

From a checkout of this repository:

    claude plugin validate .
    claude plugin validate ./plugins/resq

To test local changes, use `claude plugin marketplace add ./` or
`codex plugin marketplace add ./` in place of the GitHub source when configuring
a test installation. Both catalogs use the same installation identifiers shown above.

## Publishing updates

1. Modify the plugin files.
2. Increment the version in both platform manifests:
   - `plugins/resq/.claude-plugin/plugin.json`
   - `plugins/resq/.codex-plugin/plugin.json`
3. Keep the two manifest versions identical and use semantic versioning.
4. Validate both platforms again.
5. Publish the validated changes to the GitHub default branch.

Use patch releases for fixes, minor releases for backward-compatible features, and major releases for breaking changes.
Publishing to GitHub updates this installation source. Listing in Anthropic's or
OpenAI's public directory requires a separate submission and review.

## Help and policies

- [ResQ support](https://support.getresq.com/)
- [Privacy policy](https://www.getresq.com/privacy-policy)
- [Terms of service](https://www.getresq.com/terms-of-service)
