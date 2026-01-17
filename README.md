# Native Engineering Plugin

A Claude Code plugin that makes each unit of engineering work easier than the last.

## Install

```bash
/plugin marketplace add https://github.com/aaione/native-engineering-plugin
/plugin install native-engineering
```

## Workflow

```
Plan → Work → Review → Compound → Repeat
```

| Command | Purpose |
|---------|---------|
| `/workflow:plan` | Turn feature ideas into detailed implementation plans |
| `/workflow:work` | Execute plans with worktrees and task tracking |
| `/workflow:review` | Multi-agent code review before merging |
| `/workflow:compound` | Document learnings to make future work easier |

Each cycle compounds: plans inform future plans, reviews catch more issues, patterns get documented.

## Philosophy

**Each unit of engineering work should make subsequent units easier—not harder.**

Traditional development accumulates technical debt. Every feature adds complexity. The codebase becomes harder to work with over time.

Native engineering inverts this. 80% is in planning and review, 20% is in execution:
- Plan thoroughly before writing code
- Review to catch issues and capture learnings
- Codify knowledge so it's reusable
- Keep quality high so future changes are easy

## Learn More

- [Full component reference](plugins/native-engineering/README.md) - all agents, commands, skills
