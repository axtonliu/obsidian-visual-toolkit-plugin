# Obsidian Visual Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Plugin: Skills only](https://img.shields.io/badge/Plugin-Skills%20only-0369A1.svg)](skills/)
[![Status: Beta](https://img.shields.io/badge/Status-Beta-F59E0B.svg)](#项目状态)

**[English](README.md)**

把笔记、大纲和工作流转换成 Mermaid 图、可编辑的 Excalidraw 图，以及 Obsidian Canvas 知识地图。同一套三个 Skills 支持 Claude、Claude Code、ChatGPT 和 Codex。

作者为 Axton Liu。这是独立社区项目，并非 Obsidian、Excalidraw、Mermaid、Anthropic 或 OpenAI 的官方产品。

![Obsidian Visual Toolkit 图标](assets/logo.png)

## 包含的工作流

| Skill | 最适合 | 输出 |
|---|---|---|
| `mermaid-visualizer` | 流程、架构、时序、状态、对比 | Markdown 中的 Mermaid 代码 |
| `excalidraw-diagram` | 可编辑的手绘图、思维导图、时间线、矩阵 | `.excalidraw` 或 Obsidian Excalidraw `.md` |
| `obsidian-canvas-creator` | 空间化知识地图和交互式思维导图 | Obsidian `.canvas` JSON |

三个 Skill 的触发边界刻意保持清晰：

- 需要可移植的图表代码时，明确要求 **Mermaid**。
- 需要手绘感、可编辑图表时，明确要求 **Excalidraw**。
- 需要空间化知识地图时，明确要求 **Obsidian Canvas**。

## 项目状态

项目当前处于 Beta。三个工作流已经可以使用，并已按照公开 Plugin 的结构完成包装。不同模型版本和输入复杂度可能影响输出，请在正式文档中使用前检查生成结果。

## 依赖

需要支持 Skills 或插件的宿主，账户及套餐要求以宿主为准。本插件无需额外账户、API key、MCP server 或安装依赖包。

以下工具均为可选查看器或编辑器：

- Obsidian、GitHub 等支持 Mermaid 的 Markdown 渲染器
- [Excalidraw](https://excalidraw.com/)：打开 `.excalidraw` 文件
- [Obsidian Excalidraw plugin](https://github.com/zsviczian/obsidian-excalidraw-plugin)：打开 Obsidian Excalidraw Markdown
- [Obsidian](https://obsidian.md/)：打开 `.canvas` 文件

插件可以直接返回图表内容；当运行环境提供可写工作区时，也可以把文件保存到用户指定的位置。

## 数据与执行行为

Skills 读取用户提供的内容并返回图表代码或文件，不连接外部服务器、不采集使用统计、不自动上传内容到查看器。笔记可能包含个人信息；宿主内的处理与保留遵循宿主政策。输出保存在用户选择的工作区，是否使用在线编辑器由用户决定。

仓库中的 Python 脚本仅供维护者验证和打包，使用标准库读取插件文件并向 `dist/` 写入 ZIP；使用 Skills 时不会自动执行。

## 安装

### Claude 本地安装与测试

克隆仓库后，用 Python 3 生成 Claude ZIP：

```bash
python3 scripts/package_plugin.py --target claude
```

在 Claude 中打开 **Customize → Plugins → Add → Upload plugin**，选择 `dist/obsidian-visual-toolkit-claude-0.1.1.zip`。新建对话后明确要求生成三种格式之一。

也可以从仓库的父目录启动 Claude Code 测试：

```bash
claude --plugin-dir ./obsidian-visual-toolkit-plugin
```

Claude 与 OpenAI 官方目录上架均须经过审核和发布；本文不表示已在任一官方目录上线。

### OpenAI Plugins Directory

通过审核并发布后，可以从 ChatGPT 与 Codex 共用的 Plugins Directory 安装 **Obsidian Visual Toolkit**。

### Codex 仓库 marketplace 测试

可将本仓库添加为 marketplace source：

```bash
codex plugin marketplace add axtonliu/obsidian-visual-toolkit-plugin --ref main
codex plugin add obsidian-visual-toolkit --marketplace obsidian-visual-toolkit-marketplace
```

也可以在 ChatGPT 桌面版中完成安装。请在新任务中测试，确保加载的是最终 package。

## 示例 Prompt

```text
把这个发布流程转换成横向 Mermaid 图。

根据这些组件生成一个标准 Excalidraw 架构图。

把这篇文章的大纲整理成 Obsidian Canvas 思维导图。

用 Mermaid 对比单体架构和微服务架构。
```

## 验证与打包

```bash
python3 scripts/validate_plugin.py
claude plugin validate .
python3 scripts/package_plugin.py --target claude
python3 scripts/package_plugin.py
```

验证通过后，打包脚本会在 `dist/` 生成对应宿主的 ZIP。Claude 官方目录直接读取 GitHub 仓库，门户验证及审核独立于本地检查。

## 隐私与支持

- [隐私政策](PRIVACY.md)
- [使用条款](TERMS.md)
- [支持说明](SUPPORT.md)

## 来源

本插件把 [axton-obsidian-visual-skills](https://github.com/axtonliu/axton-obsidian-visual-skills) 中公开的三个 Skills 适配为 Claude 与 OpenAI Plugin 格式。

## License

MIT © Axton Liu
