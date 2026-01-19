# Native Engineering Plugin - 架构分析与设计

## 概述

这是对 Native Engineering Plugin 项目的深入架构分析，从多个角度剖析系统设计，并使用 Excalidraw 可视化展示。

## 项目核心理念

### 知识复利

**"每个工程单元应该让后续工作更简单，而不是更困难"**

传统开发会累积技术债，每个功能增加复杂度，代码库随时间变得更难维护。Native Engineering 反转了这个过程：

- **80%** 花在规划和审查
- **20%** 花在执行
- **100%** 的问题都被文档化，成为团队资产

### 工作流循环

```
Plan → Work → Review → Compound → Repeat
```

每个循环都在复利：
- Plans 为未来的 plans 提供参考
- Reviews 捕获更多问题
- Patterns 被文档化
- 知识被积累

## 架构图一览

### 1. 五层架构概览 ([01-five-layer-architecture.excalidraw.md](./01-five-layer-architecture.excalidraw.md))

展示系统的五个核心层次：

1. **用户层** - 用户通过 / 命令交互
2. **命令层** - 解析和路由命令
3. **Agent决策层** - 27个专业agents并行决策
4. **Skill执行层** - 14个核心技能提供具体能力
5. **数据存储层** - 文件系统、Git、MCP服务器

**关键洞察：**
- 清晰的层次分离
- 自上而下的数据流
- 自下而上的反馈循环

### 2. 工作流循环图 ([02-workflow-cycle.excalidraw.md](./02-workflow-cycle.excalidraw.md))

可视化核心工作流的四个阶段：

- **Plan**: 将想法转化为详细实现计划
- **Work**: 研究代码库，执行开发任务
- **Review**: 多agent代码审查，识别问题
- **Compound**: 文档化学习，积累知识

**关键洞察：**
- 80/20原则的体现
- 每个阶段的专门agents
- 持续改进的闭环

### 3. Agent组织架构 ([03-agent-organization.excalidraw.md](./03-agent-organization.excalidraw.md))

展示27个专业agents的组织结构：

- **Review Agents (14)**: 代码审查专家
  - dhh-rails-reviewer, security-sentinel, performance-oracle等
- **Research Agents (4)**: 研究分析专家
  - best-practices-researcher, framework-docs-researcher等
- **Design Agents (3)**: 设计实现专家
  - design-iterator, figma-design-sync等
- **Workflow Agents (5)**: 工作流自动化
  - lint, pr-comment-resolver等
- **Docs Agents (1)**: 文档生成专家
  - ankane-readme-writer

**关键洞察：**
- 并行执行能力
- 专业化分工
- 协作决策机制

### 4. Skill技能体系 ([04-skill-system.excalidraw.md](./04-skill-system.excalidraw.md))

展示14个核心技能模块的分类：

- **架构与设计**: agent-native-architecture (5大核心原则)
- **开发工具**: compound-docs, create-agent-skills, dhh-rails-style等
- **知识系统**: compound-recall (动态匹配、Flash Recall)
- **内容工作流**: every-style-editor, file-todos, git-worktree
- **集成工具**: agent-browser, gemini-imagegen, rclone
- **React最佳实践**: 49个规则文档

**关键洞察：**
- 渐进式披露设计
- YAML + Markdown格式
- 参考文档分离
- 可组合可扩展

### 5. 数据流动架构 ([05-data-flow.excalidraw.md](./05-data-flow.excalidraw.md))

详细展示数据在系统中的流动：

**正向流程：**
1. 用户输入命令
2. 命令层解析和路由
3. Agent层并行决策
4. Skill层具体执行
5. 数据层读写存储

**反馈机制：**
- **Compound Recall**: 读取历史问题，应用已知解决方案
- **动态上下文注入**: 实时注入可用资源、代码库状态
- **知识反馈**: 输出→存储→检索→应用

**关键洞察：**
- 完整的数据闭环
- 主动的知识检索
- 动态的上下文管理

### 6. 完整五层流程图 ([06-complete-five-layer-flow.excalidraw.md](./06-complete-five-layer-flow.excalidraw.md))

**最重要的架构图** - 展示完整的五层架构及其交互：

**第1层 - 用户层：**
- 开发者、产品经理、技术架构师
- CLI命令：/workflow:plan, /workflow:work, /workflow:review, /workflow:compound
- 交互方式：Claude IDE、命令行、自动触发

**第2层 - 命令层：**
- 工作流命令 (workflow:*)
- 工具命令 (/deepen-plan, /plan_review等)
- 职责：解析输入、提取参数、路由agent、注入上下文

**第3层 - Agent决策层：**
- 27个专业agents按类别组织
- 并行执行、专业分工、自主决策、动态协作

**第4层 - Skill执行层：**
- 14个核心技能模块
- YAML+Markdown、渐进式披露、脚本集成

**第5层 - 数据存储层：**
- plans/ - 功能计划
- docs/solutions/ - 问题解决方案库
- plugins/ - agents、commands、skills
- Git + Worktree - 版本控制
- MCP Servers - 外部资源

**设计原则：**
1. **80/20原则**: 80% Planning & Review, 20% Execution
2. **Agent Native**: Agent是一等公民，UI和Agent能力对等
3. **知识积累**: 每个工程单元让后续工作更简单

**关键洞察：**
- 完整的端到端流程
- 清晰的职责划分
- 知识反馈闭环

## 核心设计原则

### 1. Agent-Native 架构

基于 `agent-native-architecture` skill 的五大核心原则：

#### Parity (一致性)
**用户能通过UI做的，Agent也应该能通过工具实现**

这是基础原则。没有它，其他都无关紧要。

#### Granularity (粒度)
**优先使用原子级原语。功能是通过Agent在循环中达成的结果**

工具是原子能力：读文件、写文件、运行命令。功能不是你写的函数，而是你在prompt中描述的结果。

#### Composability (可组合性)
**有了原子工具和一致性，你可以通过编写新prompt创建新功能**

这是前两个原则的回报。新功能只是新的prompt。

#### Emergent Capability (涌现能力)
**Agent可以完成你没有明确设计的事情**

用户会要求Agent做你从未预料的事情。而Agent往往能够解决。

#### Improvement Over Time (持续改进)
**Agent-native应用通过积累上下文和prompt优化而变得更好**

应用在使用一个月后比第一天更好，即使没有代码改动。

### 2. 知识复利系统

**Compound Recall机制：**

```python
# 工作流
1. 解决问题 (30分钟研究)
2. 文档化 (5分钟) → docs/solutions/
3. 下次遇到类似问题 (2分钟查找)
4. 知识复利 → 团队变得更聪明
```

**Flash Recall（闪速回忆）：**
- 动态匹配系统
- 零维护成本
- 实时发现新文档
- 智能匹配算法（错误匹配>标签匹配>关键词匹配）

### 3. 渐进式披露

**Skill设计哲学：**
- SKILL.md < 500行（概览）
- 详细内容放在 references/ 目录
- 按需加载，避免上下文污染
- 标准markdown格式

### 4. 并行执行

**多Agent并行工作：**

例如 `/workflow:compound` 启动6个并行subagents：
1. Context Analyzer
2. Solution Extractor
3. Related Docs Finder
4. Prevention Strategist
5. Category Classifier
6. Documentation Writer

## 技术栈特点

### 文件系统作为接口

- plans/ - 实现计划
- docs/solutions/ - 问题解决方案
- plugins/ - agent、command、skill定义
- Git worktree - 并行开发

### MCP (Model Context Protocol) 集成

- context7 - 框架文档查询
- 100+ 框架支持
- 自动启动

### Claude Code SDK

- Tool definition
- Agent loop execution
- System prompt injection
- File operations

## 数据流模式

### 正向流（执行流）

```
用户命令 
  ↓
命令解析 (参数提取、路由)
  ↓
Agent决策 (并行执行、调用skills)
  ↓
Skill执行 (访问文件系统、运行脚本)
  ↓
数据存储 (plans/, docs/solutions/, Git)
```

### 反向流（反馈流）

```
数据存储
  ↓
Compound Recall (历史问题匹配)
  ↓
动态上下文注入 (可用资源、代码库状态)
  ↓
Command层 (增强的上下文)
  ↓
更聪明的决策
```

## 实际应用场景

### 场景1: 功能开发

```bash
/workflow:plan "添加用户认证功能"
```

**系统执行：**
1. **Plan阶段**: 4个research agents并行研究
   - compound-recall-researcher: 检查历史认证实现
   - repo-research-analyst: 分析当前代码库
   - best-practices-researcher: 查找业界最佳实践
   - framework-docs-researcher: 查阅框架文档

2. **生成**: 创建 `plans/feat-user-authentication.md`

3. **Work阶段**: 
   ```bash
   /workflow:work plans/feat-user-authentication.md
   ```
   - 创建 git worktree
   - 跟踪任务进度
   - 执行开发

4. **Review阶段**:
   ```bash
   /workflow:review
   ```
   - 14+ review agents 并行审查
   - 生成审查报告

5. **Compound阶段**:
   ```bash
   /workflow:compound
   ```
   - 6个agents并行文档化
   - 创建 `docs/solutions/authentication-implementation.md`

### 场景2: Bug修复

```bash
/reproduce-bug "用户登出后session未清理"
```

**系统执行：**
1. Compound Recall自动检索类似问题
2. Bug-reproduction-validator尝试重现
3. 找到解决方案后，自动trigger `/workflow:compound`
4. 积累到知识库

下次遇到类似session问题：**2分钟解决**（vs 首次30分钟）

## 可扩展性

### 添加新Agent

```markdown
---
name: my-custom-reviewer
description: Review code for specific domain rules
---

# My Custom Reviewer

## Responsibilities
[定义审查职责]

## Checklist
- [ ] Rule 1
- [ ] Rule 2
```

### 添加新Skill

```markdown
---
name: my-skill
description: What it does and when to use it
---

# My Skill

## Quick Start
[立即可用的例子]

## Instructions
[详细指导]
```

### 添加新Command

```markdown
---
name: my-command
description: What this command does
---

# My Command

## Usage
[使用方法]

## Implementation
[执行逻辑]
```

## 成功指标

一个成功的Native Engineering工作流应该展现：

### 速度指标
- **首次解决**: 30分钟
- **第二次解决**: 2分钟（通过compound recall）
- **知识复利率**: 15x

### 质量指标
- Review捕获的问题数量增加
- 生产问题减少
- 代码库健康度提升

### 知识指标
- docs/solutions/增长
- 团队查询文档频率
- 新人上手速度

## 未来方向

### 1. 自修改Agent

允许agents安全地修改自己的prompts和代码：
- 审批机制
- 自动检查点
- 健康检查
- 回滚能力

### 2. 更智能的上下文注入

- 预测性上下文加载
- 个性化prompt
- 团队级知识共享

### 3. 跨项目知识复用

- 共享的docs/solutions/库
- 跨团队最佳实践
- 组织级compound recall

## 总结

Native Engineering Plugin 展示了一种新的软件开发范式：

1. **Agent是一等公民**，不是事后添加的功能
2. **知识会复利**，每个问题只需深入解决一次
3. **80/20原则**，大部分时间花在规划和审查
4. **渐进式披露**，避免上下文污染
5. **并行执行**，最大化效率

这不仅仅是一个工具，而是一个**持续改进的工程系统**。

---

## 查看架构图

所有架构图都是Excalidraw格式，可以：
1. 在支持Excalidraw的编辑器中直接查看和编辑
2. 导入到 [Excalidraw官网](https://excalidraw.com/) 查看
3. 使用Obsidian + Excalidraw插件查看

**推荐查看顺序：**
1. 先看 `06-complete-five-layer-flow.excalidraw.md` (完整流程)
2. 再看 `02-workflow-cycle.excalidraw.md` (工作流)
3. 然后看其他细节图

享受探索！🚀
