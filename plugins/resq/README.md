# ResQ AI Plugin

Connects ChatGPT, Codex, and Claude Code to ResQ through the production MCP API.

## Authentication

ResQ uses OAuth. The plugin does not contain API keys, access tokens, client credentials, or authorization headers.

The production MCP endpoint publishes OAuth protected-resource and authorization-server metadata. A supported client discovers that metadata and displays its own **Connect**, **Sign in**, or **Authenticate** action. The user is then redirected to ResQ and access is limited to the organizations available to that account.

### ChatGPT

ChatGPT workspace registration is performed against this MCP endpoint:

    https://api.getresq.com/mcp

1. Register the endpoint as a plugin in ChatGPT developer mode.
2. Open or install the plugin in a personal workspace.
3. Choose **Connect** when ChatGPT requests authentication.
4. Sign into ResQ, select the authorized organization, and approve access.
5. After testing, a workspace admin can publish the plugin to the team.

See [ADMIN_SETUP.md](ADMIN_SETUP.md) for the team-admin handoff.

### Claude Code

1. Install or enable the plugin.
2. Open `/mcp` in Claude Code.
3. Select the ResQ MCP server.
4. Choose **Authenticate**.
5. Sign into ResQ.
6. Select your authorized organization and approve access.

### Codex

1. Install or enable the plugin.
2. Authenticate with ResQ when prompted.
3. Sign into ResQ.
4. Select your authorized organization and approve access.
5. Start a new thread so Codex loads the installed MCP tools.

Access is limited to the ResQ organizations and data available to your account.

## Included configuration

- `.codex-plugin/plugin.json`: plugin identity, version, marketplace metadata, and MCP reference.
- `.mcp.json`: production ResQ MCP endpoint used for OAuth discovery.
- `ADMIN_SETUP.md`: ChatGPT and Codex team-admin registration checklist.

No `.app.json` is included. That file requires a real `plugin_asdk_app...` technical ID created by ChatGPT when the MCP connection is registered. The ID is workspace/account registration data and must not be replaced with a placeholder.
