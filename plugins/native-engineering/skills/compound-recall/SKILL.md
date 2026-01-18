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

### Step 2: Dynamic Matcher Execution (Flash Recall)
Run the flash recall matcher script to identify relevant past experiences:
```bash
python3 plugins/native-engineering/skills/compound-recall/scripts/recall_matcher.py --tags "[tags]" --errors "[errors]" --keywords "[keywords]"
```

**Silent Skip Logic:**
If `docs/solutions/` directory does NOT exist, skip the recall process silently.

**Matching Weights:**
1. **Error Match**: Highest priority (score 10).
2. **Tag Intersection**: Medium priority (score 5).
3. **Keyword Search**: Base priority (score 2).

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
If no matches are found by the recall matcher:
1. Try a general `grep -ri "keyword" docs/solutions/` to catch documents with missing/incomplete frontmatter.
2. If still nothing, proceed but remain alert for new compounding opportunities.

## Maintenance (Flash Recall)
**Zero maintenance required.** The `recall_matcher.py` script dynamically scans `docs/solutions/` at runtime.
- New solution documents are immediately discoverable after `git pull`
- No index files to rebuild or maintain
- No Git conflicts from shared index files
