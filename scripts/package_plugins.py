#!/usr/bin/env python3
"""Build minimal provider-specific submission ZIPs from the current checkout."""

import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins/resq"


def main():
    manifests = {
        provider: json.loads((PLUGIN / f".{provider}-plugin/plugin.json").read_text())
        for provider in ("codex", "claude")
    }
    versions = {manifest["version"] for manifest in manifests.values()}
    if len(versions) != 1:
        raise ValueError("Provider manifest versions must match")
    (ROOT / "dist").mkdir(exist_ok=True)
    for provider, manifest in manifests.items():
        references = (
            [manifest["mcpServers"], manifest["interface"]["logo"],
             manifest["interface"]["composerIcon"]]
            if provider == "codex" else ["./.mcp.json", manifest["icon"]]
        )
        files = {
            f".{provider}-plugin/plugin.json": PLUGIN / f".{provider}-plugin/plugin.json",
            "LICENSE": ROOT / "LICENSE",
        }
        for reference in references:
            relative = Path(reference)
            if relative.is_absolute() or ".." in relative.parts:
                raise ValueError(f"Invalid package reference: {reference}")
            files[relative.as_posix()] = PLUGIN / relative
        payloads = {name: source.read_bytes() for name, source in files.items()}
        output = ROOT / "dist" / f"resq-{provider}-plugin-{manifest['version']}.zip"
        with ZipFile(output, "w", ZIP_DEFLATED) as archive:
            for name, payload in payloads.items():
                archive.writestr(name, payload)
        with ZipFile(output) as archive:
            if archive.testzip() is not None or set(archive.namelist()) != set(payloads):
                raise ValueError(f"Archive validation failed: {output}")
            for name, payload in payloads.items():
                if archive.read(name) != payload:
                    raise ValueError(f"Archive content mismatch: {name}")
        print(f"Built and verified {output.relative_to(ROOT)} ({len(payloads)} files)")


if __name__ == "__main__":
    main()
