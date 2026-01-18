---
name: compound-recall
description: Proactively retrieve and apply lessons learned from past projects (docs/solutions/) when planning, implementing, or debugging. Ensures historical pitfalls (Pitfalls) and precautions (Precautions) are consistently applied.
allowed-tools:
  - Read
  - Bash
  - Grep
preconditions:
  - docs/solutions/ directory exists with past lesson documentation
---

# Compound Recall Skill

**Purpose:** Act as the active memory of the project. This skill ensures that knowledge "compounded" in `docs/solutions/` is automatically recalled and applied to current tasks, preventing the repetition of past mistakes.

## Recall Protocol

When you start a new task (Planning, Working, or Reviewing), follow these steps:

### Step 1: Context Extraction
Identify these elements from the current task:
1. **Technologies/Tags**: e.g., `redis`, `rails`, `stimulus`.
2. **Error Signatures**: e.g., `Redis::TimeoutError`, `ActionController::ParameterMissing`.
3. **Core Themes**: e.g., `caching`, `authentication`, `n+1`.

### Step 2: Index Search (Triple-Pass)
Read the index file: `plugins/native-engineering/skills/compound-recall/references/knowledge-index.json`.

**Perform Matching in order of priority:**
1. **Pass 1: Error Match**: Check if any current error signatures exist in `error_index`.
2. **Pass 2: Tag Intersection**: Check if current technology tags overlap with `tag_index`.
3. **Pass 3: Keyword Search**: Check if core theme keywords exist in `keyword_index`.

### Step 3: Candidate Selection
- Select the top 1-3 most relevant solutions.
- If multiple matches exist, prioritize by **Severity** (`critical` > `high`) and **Recency**.

### Step 4: Content Loading & Injection
1. Use `read_file` to load the full content of the selected `docs/solutions/` files.
2. Use the **Recall Template** (`plugins/native-engineering/skills/compound-recall/assets/recall-template.md`) to format the knowledge.
3. **Inject** the lessons into your thinking or the plan:
   - "Institutional Knowledge Found: Applying precautions from `[doc-path]` to avoid `[pitfall]`."

---

## Fallback Strategy
If no matches are found in the index:
1. Try a general `grep -ri "keyword" docs/solutions/` to catch unindexed themes.
2. If still nothing, proceed but remain alert for new compounding opportunities.

## Maintenance
The index is auto-updated by `compound-docs`. To manually rebuild:
```bash
python3 plugins/native-engineering/skills/compound-recall/scripts/index_solutions.py
```
