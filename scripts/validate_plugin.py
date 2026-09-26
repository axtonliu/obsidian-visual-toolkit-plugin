#!/usr/bin/env python3
"""Validate the public skills-only plugin package using only the standard library."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / ".codex-plugin" / "plugin.json"
TESTS_PATH = ROOT / "evals" / "submission-tests.json"
REQUIRED_SKILLS = {
    "excalidraw-diagram",
    "mermaid-visualizer",
    "obsidian-canvas-creator",
}
FORBIDDEN_NAMES = {".env", ".env.local", ".env.production"}
FORBIDDEN_SUFFIXES = {".key", ".pem", ".p12", ".mobileprovision", ".excalidrawlib"}
SECRET_PATTERNS = {
    "private key header": re.compile(r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY"),
    "GitHub token": re.compile(r"gh[opusr]_[A-Za-z0-9]{20,}"),
    "OpenAI API key": re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "Slack token": re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),
    "credential assignment": re.compile(
        r"(?i)(?:api[_-]?key|token|password|client_secret)\s*[:=]\s*[\"'][^\"'\n]{8,}[\"']"
    ),
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"missing required file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def validate_manifest() -> None:
    manifest = load_json(MANIFEST_PATH)
    claude_manifest = load_json(ROOT / ".claude-plugin" / "plugin.json")
    for field in ("name", "version", "author", "license"):
        if not claude_manifest.get(field) or claude_manifest[field] != manifest.get(field):
            fail(f"Claude and Codex manifests must agree on {field!r}")
    if not claude_manifest.get("description"):
        fail("Claude manifest needs a description")
    for field in ("name", "version", "description", "skills"):
        if not manifest.get(field):
            fail(f"manifest field {field!r} is required")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", manifest["name"]):
        fail("manifest name must be stable kebab-case")
    if manifest["skills"] != "./skills/":
        fail("manifest skills path must be ./skills/")

    interface = manifest.get("interface", {})
    for field in ("displayName", "shortDescription", "longDescription", "developerName"):
        if not interface.get(field):
            fail(f"interface field {field!r} is required for this release")

    for field in ("composerIcon", "logo"):
        value = interface.get(field)
        if not value or not value.startswith("./"):
            fail(f"interface {field} must be a ./-prefixed relative path")
        if not (ROOT / value[2:]).is_file():
            fail(f"interface {field} does not exist: {value}")

    for screenshot in interface.get("screenshots", []):
        if not screenshot.startswith("./") or not (ROOT / screenshot[2:]).is_file():
            fail(f"invalid screenshot path: {screenshot}")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(f"missing YAML frontmatter: {path.relative_to(ROOT)}")
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def validate_skills() -> None:
    skills_root = ROOT / "skills"
    actual = {path.name for path in skills_root.iterdir() if path.is_dir()}
    if actual != REQUIRED_SKILLS:
        fail(f"expected skills {sorted(REQUIRED_SKILLS)}, found {sorted(actual)}")
    for skill_name in sorted(REQUIRED_SKILLS):
        skill_path = skills_root / skill_name / "SKILL.md"
        frontmatter = parse_frontmatter(skill_path)
        if frontmatter.get("name") != skill_name:
            fail(f"skill name mismatch in {skill_path.relative_to(ROOT)}")
        if not frontmatter.get("description"):
            fail(f"missing skill description in {skill_path.relative_to(ROOT)}")


def validate_tests() -> None:
    tests = load_json(TESTS_PATH)
    positives = tests.get("positive_tests", [])
    negatives = tests.get("negative_tests", [])
    if len(positives) < 5:
        fail("submission requires at least five positive tests")
    if len(negatives) < 3:
        fail("submission requires at least three negative tests")
    for case in positives:
        for field in ("id", "prompt", "expected_behavior", "expected_result_shape", "fixture_data"):
            if not case.get(field):
                fail(f"positive test missing {field!r}: {case.get('id', '<unknown>')}")
    for case in negatives:
        for field in ("id", "prompt", "expected_behavior", "why_not_complete"):
            if not case.get(field):
                fail(f"negative test missing {field!r}: {case.get('id', '<unknown>')}")


def validate_public_boundary() -> None:
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or "dist" in path.parts:
            continue
        if path.name in FORBIDDEN_NAMES:
            fail(f"public package contains an environment file: {path.relative_to(ROOT)}")
        if path.is_file() and path.suffix.lower() in FORBIDDEN_SUFFIXES:
            fail(f"public package contains a sensitive file type: {path.relative_to(ROOT)}")
        if path.is_file() and path.suffix.lower() in {".md", ".json", ".py", ".txt", ".yaml", ".yml"}:
            text = path.read_text(encoding="utf-8", errors="replace")
            for label, pattern in SECRET_PATTERNS.items():
                if pattern.search(text):
                    fail(f"possible {label} found in {path.relative_to(ROOT)}")


def main() -> None:
    validate_manifest()
    validate_skills()
    validate_tests()
    validate_public_boundary()
    print("OK: plugin manifest, skills, assets, tests, and public boundary validated")


if __name__ == "__main__":
    main()
