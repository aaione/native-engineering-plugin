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

## Progressive Disclosure Architecture

**Level 1 - Skill Name & Description (Always Loaded):**
This skill provides active institutional memory by retrieving and applying historical lessons learned.

**Level 2 - Core Protocol (Loaded on Activation):**
The full recall protocol and matcher implementation.

**Level 3 - Advanced Features (Loaded on Demand):**
BDI mental state modeling, advanced evaluation, and context clash detection algorithms.

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

### Step 2.5: Context Clash Detection

在匹配相关文档后，检测是否存在**上下文冲突**（Context Clash）。

> 详细理论请参考 `skill:context-degradation`（Agent-Skills-for-Context-Engineering）

**检测逻辑：**
1. 比较匹配到的多个解决方案
2. 比较时间戳，识别过期可能性
3. 检查是否存在矛盾的建议

**冲突处理：**
- 优先使用最近的解决方案（基于时间戳）
- 标记冲突：`⚠️ CONTEXT CLASH: [A.md] vs [B.md]，建议使用最新方案`
- 如无法确定，请求人工确认

### Step 2.6: BDI Mental State Modeling (Advanced)

Transform recalled knowledge into formal cognitive states for better reasoning:

**Beliefs (B):** Factual knowledge extracted from solutions
- "We believe that using Redis without connection pooling causes timeout errors"
- "We believe that N+1 queries can be detected by SQL logs showing repeated patterns"

**Desires (D):** Goals and preferences from historical success
- "We desire to implement connection pooling for all Redis operations"
- "We desire to add query preloading for all has_many associations"

**Intentions (I):** Committed actions based on beliefs and desires
- "We intend to add `connection_pool` configuration to Redis setup"
- "We intend to implement `includes()` in all collection queries"

**BDI Application:**
```ruby
# Before: Passive recall
"Remember to use connection pooling for Redis"

# After: Active BDI reasoning
"Based on our belief that Redis timeouts caused the outage (B),
we desire reliable Redis connections (D),
therefore we intend to implement connection pooling with config validation (I)"
```

> 详细理论请参考 `skill:bdi-mental-states`（Agent-Skills-for-Context-Engineering）

### Step 2.7: Advanced Evaluation of Recalled Knowledge

Apply LLM-as-judge techniques to assess knowledge relevance and quality:

**Direct Scoring:** Rate each recalled solution on multiple criteria:
- **Relevance (1-5):** How well it matches the current problem context
- **Recency (1-5):** How recent the solution is (newer = higher score)
- **Success Rate (1-5):** Historical success rate of the solution
- **Completeness (1-5):** How comprehensive the solution documentation is

**Pairwise Comparison:** When multiple solutions exist:
- Compare solution A vs B on specific criteria
- Use position bias mitigation (swap order and average scores)
- Generate rubric-based evaluations

**Bias Mitigation:**
- **Position Bias:** Alternate solution order in comparisons
- **Length Bias:** Score based on content quality, not verbosity
- **Recency Bias:** Apply time decay but don't over-weight recent solutions

> 详细理论请参考 `skill:advanced-evaluation`（Agent-Skills-for-Context-Engineering）

**Evaluation Integration:**
```python
def evaluate_solution(solution, context):
    scores = {
        'relevance': score_relevance(solution, context),
        'recency': score_recency(solution.timestamp),
        'success_rate': solution.historical_success_rate,
        'completeness': score_completeness(solution.documentation)
    }

    # Weighted average for final ranking
    weights = {'relevance': 0.4, 'recency': 0.2, 'success_rate': 0.3, 'completeness': 0.1}
    final_score = sum(scores[k] * weights[k] for k in scores)

    return final_score
```

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
