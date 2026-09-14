# ResQ AI Plugin

Connects ChatGPT, Codex, and Claude Code to ResQ through the production MCP API.

## Before connecting

You need a ResQ account with access to the organization whose data you want to
read. Your account permissions and the organization selected during consent
determine what the integration can return. Ask your ResQ administrator for
access if the organization you need is unavailable.

For Claude Code and Codex installation commands, see the
[repository guide](https://github.com/getresq/resq-ai-plugins#readme). Workspace administrators can also make the
connection available through their workspace settings.

## What you can ask

The public integration is read-only. For a facility organization, try:

- "List the ResQ facilities I can access."
- "Show the work orders for this facility."
- "Summarize work order [code], including its status and available details."

Use a facility or work-order identifier returned by ResQ in follow-up requests.
Available tools depend on the selected organization type. The integration
does not create, update, or delete work orders.

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

## Reconnect or change organizations

If the client reports expired or revoked authorization, use its ResQ connection
controls to reconnect. A permission denial for a particular record may instead
mean that your account or selected organization cannot access it.

- **Claude Code:** open `/mcp`, select the ResQ server, clear its authentication,
  then choose **Authenticate** again.
- **Codex CLI:** for a separately configured MCP server named `resq`, run
  `codex mcp logout resq`, followed by `codex mcp login resq`. For a plugin-managed
  connection, use the plugin's authentication controls and the server identifier
  shown by the client; it may differ from a separately configured server name.
- **ChatGPT:** disconnect the ResQ connection in your plugin settings, then
  connect it again through the supported OAuth flow.

To change organizations, reconnect and select the intended organization during
ResQ consent. To change accounts, sign out of ResQ in the authorization browser
if it automatically uses your previous account. Start a new conversation after
switching so earlier organization results are not mixed with new requests.
Reconnecting does not erase information already shown in a conversation.

Never paste passwords, access tokens, or refresh tokens into a conversation or
plugin file. If reconnecting does not resolve the issue, contact
[ResQ support](https://support.getresq.com/) with the client name and error
message, excluding credentials and sensitive record data.

## Included configuration

- `.codex-plugin/plugin.json`: plugin identity, version, marketplace metadata, and MCP reference.
- `.claude-plugin/plugin.json`: Claude plugin identity, version, and publisher links.
- `.mcp.json`: production ResQ MCP endpoint used for OAuth discovery.
- `assets/`: official ResQ branding and source provenance.

## Policies

[Privacy policy](https://www.getresq.com/privacy-policy) ·
[Terms of service](https://www.getresq.com/terms-of-service)
