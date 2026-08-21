# Obsidian Visual Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Plugin: Skills only](https://img.shields.io/badge/OpenAI%20Plugin-Skills%20only-0369A1.svg)](.codex-plugin/plugin.json)
[![Status: Beta](https://img.shields.io/badge/Status-Beta-F59E0B.svg)](#项目状态)

**[English](README.md)**

一个面向 ChatGPT 与 Codex 的纯 Skills 插件，把文字转换成 Mermaid、Excalidraw 和 Obsidian Canvas 图表。

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

核心插件是纯 Skills 插件，不需要账户、API key 或 MCP server。

以下工具均为可选查看器或编辑器：

- Obsidian、GitHub 等支持 Mermaid 的 Markdown 渲染器
- [Excalidraw](https://excalidraw.com/)：打开 `.excalidraw` 文件
- [Obsidian Excalidraw plugin](https://github.com/zsviczian/obsidian-excalidraw-plugin)：打开 Obsidian Excalidraw Markdown
- [Obsidian](https://obsidian.md/)：打开 `.canvas` 文件

插件可以直接返回图表内容；当运行环境提供可写工作区时，也可以把文件保存到用户指定的位置。

## 安装

### 公共 Plugins Directory

通过审核并发布后，可以从 ChatGPT 与 Codex 共用的 Plugins Directory 安装 **Obsidian Visual Toolkit**。

### 仓库 marketplace 测试

仓库发布后，可将它添加为 marketplace source：

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
python3 scripts/package_plugin.py
```

验证通过后，打包脚本会在 `dist/` 生成可上传的 ZIP。

## 隐私与支持

- [隐私政策](PRIVACY.md)
- [使用条款](TERMS.md)
- [支持说明](SUPPORT.md)

## 来源

本插件把 [axton-obsidian-visual-skills](https://github.com/axtonliu/axton-obsidian-visual-skills) 中公开的三个 Skills 适配为 OpenAI Plugin 格式。

## License

MIT © Axton Liu
