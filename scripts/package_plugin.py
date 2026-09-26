#!/usr/bin/env python3
"""Create a deterministic submission archive after validating the plugin."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
EXCLUDED_PARTS = {".agents", ".git", "dist", "scripts", "evals", "submission-artifacts", "__pycache__"}
EXCLUDED_SUFFIXES = {".pyc", ".DS_Store"}


def included_files(target: str) -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if any(part in EXCLUDED_PARTS for part in relative.parts):
            continue
        other_manifest = ".codex-plugin" if target == "claude" else ".claude-plugin"
        if other_manifest in relative.parts:
            continue
        if path.is_file() and path.name not in EXCLUDED_SUFFIXES and path.suffix not in EXCLUDED_SUFFIXES:
            files.append(path)
    return sorted(files, key=lambda path: path.relative_to(ROOT).as_posix())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", choices=("codex", "claude"), default="codex")
    args = parser.parse_args()
    subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_plugin.py")], check=True)
    manifest_dir = ".claude-plugin" if args.target == "claude" else ".codex-plugin"
    manifest = json.loads((ROOT / manifest_dir / "plugin.json").read_text(encoding="utf-8"))
    suffix = "-claude" if args.target == "claude" else ""
    output = DIST / f"{manifest['name']}{suffix}-{manifest['version']}.zip"
    DIST.mkdir(exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in included_files(args.target):
            relative = path.relative_to(ROOT)
            info = zipfile.ZipInfo(relative.as_posix(), date_time=(2026, 8, 21, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())
    print(output)


if __name__ == "__main__":
    main()
