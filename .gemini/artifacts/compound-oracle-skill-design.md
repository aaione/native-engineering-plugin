# Compound Recall: 动态知识复利召回方案

## 0. 背景与愿景
在 Compound Engineering 体系中，`/workflow:compound` 沉淀了大量高质量的解决方案（`docs/solutions/`）。
**Compound Recall** 技能的目标是作为这些知识的“活性出口”，在不牺牲上下文窗口的前提下，为 AI 赋予“动态项目记忆”，使其在执行相关任务时自动避坑。

---

## 1. 核心设计：动态索引 + 渐进式披露

方案放弃手动维护 references 文件，改为基于 `docs/solutions/` 的**实时索引模式**：

| 层级 | 载体 | 内容来源 | 作用 |
| :--- | :--- | :--- | :--- |
| **Layer 1: 感知层** | `name` & `description` | 固化描述 | 告诉系统：“遇到任何规划、实现或报错任务，请先查阅我的项目记忆。” |
| **Layer 2: 路由层** | `SKILL.md` 指令 | 检索算法 | 定义如何根据当前 context 匹配索引中的标签、错误签名或关键词。 |
| **Layer 3: 索引层** | `references/index.json` | **脚本自动生成** | 存储所有 solution 的元数据和文件路径映射，实现按需加载。 |

---

## 2. 目录结构

```text
plugins/native-engineering/skills/compound-recall/
├── SKILL.md                 # 核心检索协议
├── references/              
│   ├── knowledge-index.json   # 动态索引文件（由脚本更新）
│   └── taxonomy.md            # 领域分类与分类标准
├── scripts/
│   └── index_solutions.py     # 自动化索引脚本
└── assets/
    └── recall-template.md     # 召回内容展示模板
```

---

## 3. 核心机制：索引与召回协议

### A. 索引自动化 (Indexing)
每当执行 `/workflow:compound` 产生新文档时：
1. 触发 `scripts/index_solutions.py`。
2. 聚合 `docs/solutions/**/*.md` 的 YAML Frontmatter。
3. 更新 `references/knowledge-index.json`。

### B. 召回协议 (Recall Protocol)
在 `SKILL.md` 中定义：
1. **关键词提取**: 提取当前 Error Message, Technology Tags 和 Component Name。
2. **三路匹配**:
   - `Error Signature`: 匹配报错堆栈。
   - `Tag Search`: 匹配技术栈标签（如 redis, rails）。
   - `Keyword Search`: 匹配症状描述。
3. **内容拉取**: 使用 `read_file` 直接读取命中的 `docs/solutions/` 原始 MD 文件。
4. **注入约束**: 提取 MD 中的 `Precautions` 和 `Pitfalls` 注入当前任务 context。

---

## 4. 与原方案 (Oracle) 的核心差异

1. **零维护**: references 不再存储知识内容，只存储索引映射，知识源永远是 `docs/solutions/`。
2. **更高的一致性**: 避免了 skills 目录和 docs 目录数据不同步的问题。
3. **纯净的 Payload**: AI 最终看到的是原始的、经过验证的 Solution 文档，包含完整的上下文。

---

**总结**：实现从“记录”到“实时召回”的飞跃。
