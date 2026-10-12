# ResQ AI Plugins

Use ResQ for **Maintenance and Repairs** in Claude Code, Codex, and ChatGPT.
Connect through ResQ OAuth to read authorized records and, with explicit write
consent and account permissions, perform supported work-order actions.

This repository contains the plugin configuration, provider marketplace
catalogs, branding, and submission packaging. ResQ's hosted service at
`https://api.getresq.com/mcp` implements the tools and authentication.

## What you can do

| Access | Supported workflows |
| --- | --- |
| Read | View facilities, equipment, work orders, invoices, attachments, visits, appointments, and available technicians. |
| Write | Create and accept work orders; schedule and reschedule appointments; return appointments to scheduling; start work-order visits. |

Available tools depend on the selected organization, account permissions, OAuth
consent, and server availability. Read-only connections remain supported.
Installing or updating the plugin does not grant write access. Media upload,
attachment creation, and invoice submission are not supported.

You need a ResQ account with access to an eligible organization. For example:

- "List the ResQ facilities I can access."
- "Summarize work order [code], including its status and available details."
- "Create a work order for a leaking sink at [facility]."
- "Reschedule the appointment for work order [code] to [date and time]."

Use identifiers returned by ResQ and provide any additional details requested
before an action is performed. See the [plugin guide](plugins/resq/README.md)
for authentication, reconnecting, and changing organizations.

## Install from this repository

The plugin ID is `resq`, the marketplace ID is `resq-ai`, and the display name
is **ResQ**. Both catalogs point to `./plugins/resq`.

### Claude Code

```sh
claude plugin marketplace add getresq/resq-ai-plugins
claude plugin install resq@resq-ai
```

Open `/mcp`, select the ResQ server, and choose **Authenticate**. Sign into ResQ,
select your organization, and approve the access you intend to use.

### Codex

```sh
codex plugin marketplace add getresq/resq-ai-plugins
codex plugin add resq@resq-ai
```

Authenticate with ResQ when prompted, select your organization, and approve
access. Start a new thread after installation or reconnecting to load the
available tools. The OpenAI catalog's `local` source means the plugin lives in
this repository, including when the marketplace is downloaded from GitHub.

### ChatGPT

ChatGPT setup uses the production MCP endpoint:

```text
https://api.getresq.com/mcp
```

Follow the [ChatGPT setup guide](plugins/resq/README.md#openai-chatgpt) for
registration through developer mode and ResQ OAuth. Availability depends on
your workspace settings and administrator permissions.

Repository marketplace installation and public directory submission are
separate distribution paths. Publishing this repository does not establish
approval or availability in either provider's public directory.

## Repository layout

| Path | Purpose |
| --- | --- |
| `.claude-plugin/marketplace.json` | Claude Code repository marketplace catalog. |
| `.agents/plugins/marketplace.json` | OpenAI repository marketplace catalog and installation/authentication policies. |
| `plugins/resq/.claude-plugin/plugin.json` | Claude identity, version, privacy URL, and SVG icon reference. |
| `plugins/resq/.codex-plugin/plugin.json` | OpenAI identity, version, Read/Write capabilities, listing metadata, and MCP reference. |
| `plugins/resq/.mcp.json` | Shared production MCP connection; contains no credentials. |
| `plugins/resq/README.md` | User setup and authentication guide. |
| `plugins/resq/assets/` | Manifest-referenced PNG logo and SVG icon. |
| `docs/brand/` | Asset provenance and unused reference favicon, outside the plugin package. |
| `scripts/package_plugins.py` | Builds and verifies separate provider submission ZIPs. |
| `dist/` | Local generated ZIPs, excluded from Git. |

Asset provenance records use paths relative to the repository root. Keep
supporting documentation and unused artwork outside `plugins/resq/assets/`.

## Validate and build submission bundles

From the repository root, with Python 3 and Claude Code installed:

```sh
claude plugin validate .
claude plugin validate ./plugins/resq
python3 scripts/package_plugins.py
```

The packager requires matching manifest versions, includes every referenced
package file, and verifies ZIP integrity and byte-for-byte contents. It does
not authenticate to the MCP server, test tool behavior, or establish directory
approval. Claude's local validator may warn about the directory-requested
`privacyPolicyUrl` and `icon` fields, which Claude Code ignores at load time.

The current manifests are version **2.1.1**, producing:

| Provider | Output | Files in the ZIP |
| --- | --- | --- |
| OpenAI | `dist/resq-codex-plugin-2.1.1.zip` | `.codex-plugin/plugin.json`, `.mcp.json`, `assets/resq-logo-256.png`, `LICENSE` |
| Anthropic | `dist/resq-claude-plugin-2.1.1.zip` | `.claude-plugin/plugin.json`, `.mcp.json`, `assets/resq-wordmark.svg`, `LICENSE` |

Filenames follow the version in the manifests. Each archive has its manifest
at the ZIP root, with no enclosing repository folder. Upload the matching
provider ZIP. The build excludes repository catalogs, READMEs, provenance files,
unused artwork, and the other provider's manifest.

For local marketplace testing, substitute `./` for the GitHub repository in the
marketplace-add commands above, then install `resq@resq-ai` with the appropriate
client. Test authentication and the intended read/write workflows with a demo
account and sample data.

## Release workflow

1. Update the relevant manifests, documentation, or referenced assets.
2. For package changes, increment both provider manifest versions together.
   Use a patch for fixes, a minor version for compatible features, and a major
   version for breaking changes. A repository-only documentation edit does not
   require a package version bump.
3. Run local validation and build both provider ZIPs.
4. Commit and push the source changes. Generated ZIPs remain in ignored `dist/`.
5. Upload each provider's ZIP to its existing directory submission and complete
   the required review steps. Check the resulting scan findings; local
   validation does not guarantee acceptance.

MCP implementation, OAuth discovery, and domain-verification routes belong to
the hosted service. Coordinate those changes with the server repository; they
do not belong in the plugin manifests or ZIPs.

See the official [Claude marketplace documentation](https://code.claude.com/docs/en/plugin-marketplaces),
[OpenAI packaging documentation](https://developers.openai.com/plugins/build/plugins),
and [OpenAI submission guide](https://developers.openai.com/plugins/deploy/submission).

## Help, policies, and licensing

- [ResQ support](https://support.getresq.com/)
- [Privacy policy](https://www.getresq.com/privacy-policy)
- [Terms of service](https://www.getresq.com/terms-of-service)

Plugin configuration and documentation are licensed under the [MIT License](LICENSE).
ResQ logos and brand artwork in `plugins/resq/assets/` and `docs/brand/` are
excluded from that license. No trademark rights are granted. Access to the
hosted API requires authentication and remains subject to ResQ's terms.
