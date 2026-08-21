# Obsidian Visual Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Plugin: Skills only](https://img.shields.io/badge/OpenAI%20Plugin-Skills%20only-0369A1.svg)](.codex-plugin/plugin.json)
[![Status: Beta](https://img.shields.io/badge/Status-Beta-F59E0B.svg)](#status)

**[中文文档](README_CN.md)**

Turn text into Mermaid, Excalidraw, and Obsidian Canvas diagrams with one skills-only plugin for ChatGPT and Codex.

![Obsidian Visual Toolkit icon](assets/logo.png)

## Included workflows

| Skill | Best for | Output |
|---|---|---|
| `mermaid-visualizer` | Processes, architectures, sequences, states, comparisons | Mermaid code in Markdown |
| `excalidraw-diagram` | Editable hand-drawn diagrams, mind maps, timelines, matrices | `.excalidraw` or Obsidian Excalidraw `.md` |
| `obsidian-canvas-creator` | Spatial knowledge maps and interactive mind maps | Obsidian `.canvas` JSON |

The skills have deliberately narrow trigger boundaries:

- Ask for **Mermaid** when you need portable diagram code.
- Ask for **Excalidraw** when you need a hand-drawn, editable diagram.
- Ask for **Obsidian Canvas** when you need a spatial knowledge map.

## Demo

| Mermaid | Excalidraw | Obsidian Canvas |
|---|---|---|
| ![Mermaid demo](assets/mermaid-demo.png) | ![Excalidraw demo](assets/excalidraw-demo.png) | ![Canvas demo](assets/canvas-demo.png) |

## Status

This project is in beta. The three workflows are usable and packaged for public plugin testing. Output can vary with model version and input complexity, so review generated diagrams before relying on them in production documentation.

## Requirements

The core plugin is skills-only and does not require an account, API key, or MCP server.

Optional viewers and editors:

- Mermaid-compatible Markdown renderer, such as Obsidian or GitHub
- [Excalidraw](https://excalidraw.com/) for `.excalidraw` files
- [Obsidian Excalidraw plugin](https://github.com/zsviczian/obsidian-excalidraw-plugin) for Obsidian Excalidraw Markdown files
- [Obsidian](https://obsidian.md/) for `.canvas` files

The plugin can return the artifact content directly. When the host provides a writable workspace, it may also save the requested file there.

## Installation

### Public Plugins Directory

After approval and publication, install **Obsidian Visual Toolkit** from the universal Plugins Directory shared by ChatGPT and Codex.

### Repository marketplace testing

After this repository is published, add it as a marketplace source:

```bash
codex plugin marketplace add axtonliu/obsidian-visual-toolkit-plugin --ref main
codex plugin add obsidian-visual-toolkit --marketplace obsidian-visual-toolkit-dev
```

You can also install it from the ChatGPT desktop app. Test the installed plugin in a new task so the final package is loaded cleanly.

## Example prompts

```text
Turn this deployment workflow into a horizontal Mermaid diagram.

Create a standard Excalidraw architecture diagram from these components.

Organize this article outline as an Obsidian Canvas mind map.

Compare a monolith and microservices architecture as a Mermaid diagram.
```

## Project structure

```text
obsidian-visual-toolkit-plugin/
├── .codex-plugin/
│   └── plugin.json
├── assets/
├── evals/
│   └── submission-tests.json
├── scripts/
│   ├── package_plugin.py
│   └── validate_plugin.py
├── skills/
│   ├── excalidraw-diagram/
│   ├── mermaid-visualizer/
│   └── obsidian-canvas-creator/
├── LICENSE
├── PRIVACY.md
├── SUPPORT.md
└── TERMS.md
```

## Validate and package

```bash
python3 scripts/validate_plugin.py
python3 scripts/package_plugin.py
```

The package script writes a submission-ready ZIP to `dist/` after validation succeeds.

## Privacy and support

- [Privacy Policy](PRIVACY.md)
- [Terms of Use](TERMS.md)
- [Support](SUPPORT.md)

## Acknowledgments

This plugin packages and adapts the public skills from [axton-obsidian-visual-skills](https://github.com/axtonliu/axton-obsidian-visual-skills) for the OpenAI plugin format.

## License

MIT © Axton Liu
