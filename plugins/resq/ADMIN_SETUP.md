# ResQ 1.1.0 team-admin handoff

This package connects supported OpenAI clients to the production ResQ MCP endpoint:

    https://api.getresq.com/mcp

## What is in this package

- Plugin metadata for ResQ version `1.1.0`.
- The production MCP URL in `.mcp.json`.
- OAuth discovery support through the MCP server.
- No secrets, tokens, passwords, client credentials, or authorization headers.

## Register and test in ChatGPT

1. Sign into the ChatGPT account that can manage plugins for the target workspace.
2. Open <https://chatgpt.com/plugins>.
3. If required, enable developer mode under **Settings > Security and login**.
4. Create/register a plugin connection using `https://api.getresq.com/mcp`.
5. Save the connection, open it in a new chat, and choose **Connect** when prompted.
6. Sign into ResQ, select an authorized organization, and approve access.
7. Confirm the ResQ tools can list only the facilities and work orders available to that account.

ChatGPT creates a technical ID beginning with `plugin_asdk_app` during registration. Record it if this repository should later ship a ChatGPT `.app.json` mapping. Do not invent or reuse an ID from another connection.

## Publish to the team

After the personal test succeeds:

1. Return to **Plugins > Personal** in ChatGPT.
2. Open the ResQ plugin's menu and choose **Publish**.
3. Select the target workspace roles or audience.
4. Complete the workspace's review/approval flow.

Only a workspace administrator can make the plugin available to other team members. Publishing controls availability; each user still signs into ResQ individually through OAuth.

## Codex internal marketplace

The repository marketplace is named `resq-internal`. Add and install it with:

    codex plugin marketplace add getresq/resq-ai-plugins
    codex plugin add resq@resq-internal

The marketplace entry sets authentication to `ON_INSTALL`, so the user is prompted to connect to ResQ during installation when supported by the client.

## Verification notes

- The OAuth resource is `https://api.getresq.com/mcp`.
- The requested scope is `read`.
- Tokens are sent as bearer tokens in the HTTP authorization header.
- OAuth uses authorization code flow with PKCE (`S256`).

For packaging and publishing guidance, see <https://developers.openai.com/plugins/build/plugins>.
