# ResQ brand assets

Downloaded unchanged from the assets linked by [ResQ's public website](https://www.getresq.com/) on September 10, 2026.

| File | Format and size | Intended use |
| --- | --- | --- |
| `resq-logo-256.png` | PNG, 256 × 256, 1,778 bytes | Public listing logo and composer icon. White ResQ mark on orange. |
| `resq-wordmark.svg` | SVG, viewBox `0 0 89 28`, 4,629 bytes | Documentation and horizontal brand presentation. Paths use `#EB6A1E`. |
| `resq-favicon-32.png` | PNG, 32 × 32, 343 bytes | Reference/favicon only. Too small for OpenAI directory branding. |

Use the original square PNG for both `interface.logo` and `interface.composerIcon`. The horizontal wordmark is not a square directory icon. The original logo is sufficient without resizing: OpenAI's [branding asset requirements](https://developers.openai.com/plugins/deploy/submission-errors#image-errors) accept square raster images from 48 × 48 through 4,096 × 4,096, up to 5 MiB.

`sources.json` records the exact source URL, retrieval date, original dimensions, byte size, and SHA-256 for each file. These are existing ResQ brand assets; no new artwork was generated and no downloaded artwork was altered.

The Codex manifest references the square PNG as both `interface.logo` and
`interface.composerIcon`.

The Claude manifest references the original `resq-wordmark.svg` as its `icon`.
Anthropic's review requests an SVG or a 512 × 512 PNG; the existing SVG meets
the format requirement without resizing the 256 × 256 OpenAI logo.

## Directory reviewer notes

All files in this directory are static branding or provenance documentation.
The plugin packages no executable code, hooks, or local MCP commands. Its
`.mcp.json` configures only the remote HTTPS ResQ MCP endpoint. Nothing in the
plugin executes these assets or this README.

The SVG contains only an SVG root and two path elements, with no scripts,
event handlers, embedded content, or external references. The PNG files are
static images; no fonts are bundled. `sources.json` records their original
hashes for review.

Anthropic's image/font screening note is informational. Its directory-policy
hold requires reviewer assessment; these notes clarify asset usage and do not
claim to clear that hold.
