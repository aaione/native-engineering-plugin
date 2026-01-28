# Native Engineering Plugin Context Engineering Integration Plan

> **Created**: 2026-01-21
> **Implemented**: 2026-01-21
> **Version**: 1.0
> **Status**: ✅ Layers 1-2 Implemented

---

## Executive Summary

This plan proposes a **progressive integration strategy** based on in-depth research of the **Agent-Skills-for-Context-Engineering** project and a comprehensive assessment of **Native Engineering Plugin**'s existing capabilities.

### Core Conclusion

```
┌────────────────────────────────────────────────────────────────────┐
│  Relationship between Native Engineering Plugin and Agent-Skills:  │
│                                                                    │
│  Domain-Specialized Workflow Implementation  vs  Generic Context   │
│  Engineering Teaching Framework                                    │
│                                                                    │
│  Native Engineering already implements most Agent-Skills concepts, │
│  but is missing:                                                   │
│  • Systematic theoretical expression (degradation patterns, WSCI)  │
│  • Some advanced capabilities (compression strategies, eval)       │
└────────────────────────────────────────────────────────────────────┘
```

---

## Part 1: Current State Comparison Analysis

### 1.1 Native Engineering Plugin Core Strengths (Should Not Be Weakened)

| Strength | Description | Corresponds to Agent-Skills Concept |
|----------|-------------|-------------------------------------|
| **Knowledge Compounding System** | Compound Recall + docs/solutions/ + Flash Recall dynamic matching | Memory Systems + Filesystem Context |
| **Workflow Closed Loop** | Plan→Work→Review→Compound, 80/20 principle | *Unique, no Agent-Skills equivalent* |
| **Specialized Agent Group** | 27 agents, 14 Review agents execute in parallel | Multi-Agent Patterns |
| **Agent-Native Philosophy** | Parity, Granularity, Composability, Emergent, Improvement | *Mature design philosophy* |
| **Progressive Disclosure** | SKILL.md <500 lines, references/ separated | Progressive Disclosure |

### 1.2 Capability Comparison Table

| Agent-Skills Concept | Native Engineering Status | Assessment |
|---------------------|--------------------------|------------|
| Filesystem Context | docs/solutions/, plans/, scratch/ | ✅ Fully implemented |
| Multi-Agent Patterns | 27 agents organized by category, parallel execution | ✅ Fully implemented |
| Progressive Disclosure | SKILL.md spec, references/ directory | ✅ Implemented |
| Memory Systems | Compound Recall + Flash Recall | ✅ **Exceeds** Agent-Skills |
| Tool Design | Specialized agents, clear responsibilities | ✅ Implemented |
| **Context Optimization** | Partial (isolate, select), no compression | ⚠️ Needs enhancement |
| **Context Degradation** | No explicit handling of 4 degradation patterns | ❌ Missing |
| **Context Compression** | No structured compression mechanism | ❌ Missing |
| **Evaluation Framework** | No probe-based quality assessment | ❌ Missing |

### 1.3 Agent-Skills Core Theoretical Framework (To Be Integrated)

#### Four Context Degradation Patterns

```
┌───────────────────────────────────────────────────────────────────┐
│                    Context Degradation Patterns                    │
├───────────────────────────────────────────────────────────────────┤
│                                                                    │
│  1. Lost-in-Middle                                                 │
│     • Description: Attention to information in middle drops 10-40% │
│     • Symptom: Agent "forgets" key information provided earlier    │
│     • Mitigation: Place key information at beginning or end        │
│                                                                    │
│  2. Context Poisoning                                              │
│     • Description: Error information accumulates, creates feedback  │
│       loop                                                         │
│     • Symptom: Agent repeats same type of error, correction fails  │
│     • Mitigation: Clean context, rebuild correct information       │
│                                                                    │
│  3. Context Distraction                                            │
│     • Description: Irrelevant information consumes attention budget │
│     • Symptom: Agent response deviates from topic, cites irrelevant │
│       content                                                      │
│     • Mitigation: Filter irrelevant info, focus on current task    │
│                                                                    │
│  4. Context Clash                                                  │
│     • Description: Accumulated information directly contradicts    │
│     • Symptom: Agent outputs contradictory conclusions, decision   │
│       swings                                                       │
│     • Mitigation: Mark conflicts, establish priority rules         │
│                                                                    │
└───────────────────────────────────────────────────────────────────┘
```

#### WSCI Four-Bucket Strategies

| Strategy | Description | Native Engineering Counterpart |
|----------|-------------|-------------------------------|
| **W**rite | Save context outside window | ✅ docs/solutions/, plans/ |
| **S**elect | Pull relevant context on demand | ✅ Compound Recall |
| **C**ompress | Reduce tokens while preserving info | ❌ Missing |
| **I**solate | Split context across sub-agents | ✅ Parallel agents |

---

## Part 2: Optimization Plan

### 2.1 Plan Principles

```
┌────────────────────────────────────────────────────────────────────┐
│                          Design Principles                          │
├────────────────────────────────────────────────────────────────────┤
│  1. Integration Not Replacement: Enhance existing capabilities,    │
│     don't rebuild                                                 │
│  2. Protect Core Strengths: Knowledge compounding and workflow    │
│     closed-loop are competitive advantages                        │
│  3. Progressive Implementation: Execute in layers, observe effects │
│     before deciding next steps                                    │
│  4. Avoid Over-Engineering: Don't implement capabilities Native   │
│     Engineering doesn't need                                      │
└────────────────────────────────────────────────────────────────────┘
```

### 2.2 Three-Layer Optimization Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Layer 3: Architecture Completion (Execute on Demand)               │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  • Compression commands (only when long对话 scenarios need) │   │
│  │  • Evaluation framework (only when quality assessment needs)│   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              ▲                                      │
│                              │ If needed                            │
│  Layer 2: Capability Enhancement (Short-term execution)             │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  • Enhance compound-recall to handle Context Clash          │   │
│  │  • workflow:work add tool output offload mode               │   │
│  │  • Create context-health-checklist quality checklist        │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              ▲                                      │
│                              │                                      │
│  Layer 1: Principle Integration (Immediate execution)               │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  • Update architecture docs, add context engineering section│   │
│  │  • workflow:work add position sensitivity guidance          │   │
│  │  • workflow:review add Context Poisoning detection prompts  │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Part 3: Detailed Implementation Plan

### 3.1 Layer 1: Principle Integration (Immediate Execution)

#### 3.1.1 Update Architecture Documentation

**File**: `docs/architecture/README.md`

**New Section**: "Context Engineering Principles"

```markdown
## Context Engineering Principles

Native Engineering Plugin design integrates context engineering best practices.
Understanding these principles helps better use and extend the system.

### Attention Budget Concept

Context windows are constrained by attention mechanisms, not raw token capacity.
Each additional token consumes limited "attention budget."

**Native Engineering Response Strategies:**
- Progressive disclosure (SKILL.md <500 lines)
- On-demand loading (Compound Recall selective retrieval)
- Module isolation (27 specialized agents share the load)

### Four Degradation Patterns and Responses

[Add degradation pattern descriptions and Native Engineering responses]

### WSCI Four-Bucket Strategy Mapping

[Describe how Native Engineering implements Write/Select/Compress/Isolate]
```

#### 3.1.2 Enhance workflow:work

**File**: `plugins/native-engineering/commands/workflows/work.md`

**New Content** (in Phase 2: Execute section):

```markdown
### Context Health Best Practices

**Position Sensitivity**:
- Place task goals and key constraints at the beginning
- Place expected output format at the end
- Avoid accumulating large amounts of irrelevant information in the middle

**Tool Output Management**:
- When tool output > 2000 tokens, consider writing to scratch/ directory
- Return summary and file reference rather than full content

**Degradation Signal Monitoring**:
- If Agent starts repeating similar errors → Possible Context Poisoning
- If Agent response deviates from topic → Possible Context Distraction
- If above symptoms detected, consider compressing or restarting context
```

#### 3.1.3 Enhance workflow:review

**File**: `plugins/native-engineering/commands/workflows/review.md`

**Enhanced Content** (in Parallel Agents section, compound-recall-researcher description):

```markdown
14. Task compound-recall-researcher(PR content)
    - Check against known pitfalls in project memory
    - **NEW: Detect potential Context Clash (conflicting information in PR)**
    - **NEW: Flag if PR introduces patterns that contradict existing solutions**
```

### 3.2 Layer 2: Capability Enhancement (Short-term Execution)

#### 3.2.1 Enhance Compound Recall to Handle Context Clash

**File**: `plugins/native-engineering/skills/compound-recall/SKILL.md`

**New Content**:

```markdown
### Step 2.5: Context Clash Detection

After matching relevant documents, check for conflicts:

1. **Identify Signals**:
   - Current task description contradicts historical solutions
   - Multiple solutions give different recommendations
   - Technology stack upgrade invalidates old solutions

2. **Handling Strategy**:
   - Mark conflict: "⚠️ Context Clash Detected"
   - List conflicting solutions and their timestamps
   - Suggest: Prioritize recent solution, or request human confirmation

3. **Injection Format**:
   ```
   ⚠️ CONFLICT ALERT: Found conflicting approaches for [topic]
   - docs/solutions/A.md (2025-06): Recommends X
   - docs/solutions/B.md (2026-01): Recommends Y
   → Suggest using the newer approach (Y) unless otherwise specified.
   ```
```

#### 3.2.2 Tool Output Offload Pattern

**File**: Create `plugins/native-engineering/skills/compound-recall/assets/output-offload-template.md`

```markdown
# Tool Output Offload Template

When tool output exceeds threshold (~2000 tokens), use this pattern:

## Offload Process

1. Write complete output to scratch/ directory
2. Generate summary (key findings, metrics, conclusions)
3. Return summary and file reference

## Example

### Before (Context Flooding)
```
User: Search relevant documents
Agent: [Returns 8000 tokens of search results]
```

### After (Offload Mode)
```
User: Search relevant documents
Agent:
[Output saved to scratch/search_20260121_001.txt]

**Summary (3 key findings):**
1. API rate limit is 1000 req/min (see line 45)
2. Authentication uses JWT with 24h expiry (see line 123)
3. Rate limiting applies per-API-key (see line 89)

Use `grep` or `read_file` to access specific details.
```
```

#### 3.2.3 Context Health Checklist

**File**: Create `plugins/native-engineering/commands/context-health.md`

```markdown
---
name: context-health
description: Quick context health checklist
---

# /context-health

Quick diagnosis of context state, identify potential issues.

## Checklist

### 1. Degradation Symptom Detection

- [ ] **Lost-in-Middle**: Is Agent "forgetting" previously provided key information?
- [ ] **Context Poisoning**: Is Agent repeatedly making similar errors?
- [ ] **Context Distraction**: Is Agent response deviating from current task?
- [ ] **Context Clash**: Is contradictory information affecting decisions?

### 2. Suggested Actions

| Symptom | Suggested Action |
|---------|-----------------|
| Lost-in-Middle | Re-state key information, place at message beginning |
| Context Poisoning | Explicitly correct errors, or consider new conversation |
| Context Distraction | Remove irrelevant context, focus on current task |
| Context Clash | Mark conflicts, clarify priorities |

### 3. Preventive Measures

- Use Compound Recall at task start to retrieve relevant knowledge
- Offload large tool outputs to scratch/ directory
- Consider periodic summaries for long conversations

## When to Use

- When Agent seems "less capable"
- After 20+ rounds of long conversation
- When complex task is not progressing well
```

### 3.3 Layer 3: Architecture Completion (Execute on Demand)

⚠️ **Implement only when there is clear need, not recommended for immediate execution**

#### 3.3.1 Compression Command (Optional)

```markdown
---
name: context-compress
description: Generate structured session summary to reduce load for long conversations
---

## Trigger Conditions
- Conversation exceeds 30 rounds
- Tool output accumulates over 50,000 tokens
- User requests

## Compression Template

### Session Summary
- **Session Intent**: [User's core goal]
- **Files Modified**: [List of modified files]
- **Decisions Made**: [Key decisions made]
- **Current State**: [Current progress]
- **Next Steps**: [Work remaining]
```

#### 3.3.2 Evaluation Framework (Optional)

```markdown
---
name: agent-evaluation
description: Probe-based Agent quality assessment
---

## Probe Types
- Recall probe: Fact retention rate
- Artifact probe: File tracking completeness
- Continuation probe: Task planning continuity
- Decision probe: Decision reasoning chain retention
```

---

## Part 4: What We Won't Do

### ❌ Should Not Do

| What Not to Do | Reason |
|----------------|--------|
| Create standalone `context-engineering` skill | Duplicates architecture docs, adds maintenance burden |
| Copy Agent-Skills skill structure | They are educational, Native Engineering is workflow tool |
| Add Token counting dashboard | Complex implementation, uncertain benefit |
| Modify Plan→Work→Review→Compound | Mature core architecture, should not change |
| Rebuild Memory Systems | Compound Recall already exceeds Agent-Skills design |

---

## Part 5: Implementation Roadmap

### Phase 1: Principle Integration (1-2 days)

| Task | File | Change Type | Priority |
|------|------|-------------|----------|
| Add context engineering section | docs/architecture/README.md | Documentation | P1 |
| Add position sensitivity guidance | plugins/.../workflows/work.md | Documentation | P1 |
| Add Clash detection prompts | plugins/.../workflows/review.md | Documentation | P1 |

### Phase 2: Capability Enhancement (3-5 days)

| Task | File | Change Type | Priority |
|------|------|-------------|----------|
| Enhance Clash detection | skills/compound-recall/SKILL.md | Feature | P2 |
| Create output offload template | skills/compound-recall/assets/ | Resource | P2 |
| Create health check command | commands/context-health.md | New | P2 |

### Phase 3: Observation and Iteration

- Use for 1-2 weeks, collect feedback
- If long conversation needs clearly emerge → Implement compression
- If quality assessment needs clearly emerge → Implement evaluation framework

---

## Part 6: Success Metrics

### Short-term Metrics (Within 1 Month)

- [ ] Architecture docs include context engineering section
- [ ] workflow commands include position sensitivity guidance
- [ ] Compound Recall supports Clash detection

### Medium-term Metrics (Within 3 Months)

- [ ] Team members understand 4 degradation patterns
- [ ] Clear handling strategy for long conversation scenarios
- [ ] Habit established for offloading large tool outputs

### Long-term Metrics

- No clear demand indicates compression/evaluation framework are urgent
- Knowledge compounding system continues working well
- Workflow closed loop remains unaffected

---

## Appendix: Why This Is the Optimal Plan?

### A. Protect Existing Strengths

Native Engineering Plugin's core competitive advantages:
1. **Knowledge Compounding System** - More advanced than Agent-Skills
2. **Workflow Closed Loop** - No Agent-Skills equivalent
3. **Specialized Agent Group** - Production-grade capabilities

The plan **does not touch these core assets**.

### B. Fill Real Gaps

The plan only fills capabilities proven to be genuinely missing:
- Context degradation theoretical framework (cognitive level)
- Clash detection (compound-recall enhancement)
- Tool output management (best practice guidance)

### C. Avoid Over-Engineering

After analysis, the following are **not urgent needs**:
- Token counting dashboard (complex, uncertain benefit)
- Standalone compression feature (most tasks relatively independent)
- Complete evaluation framework (no clear use case)

The plan lists these as "execute on demand," not must-do items.

### D. Progressive Risk Control

Three-layer implementation:
1. Layer 1 (Principle Integration) → Zero code changes, zero risk
2. Layer 2 (Capability Enhancement) → Incremental changes, reversible
3. Layer 3 (Architecture Completion) → Execute on demand only

---

*End of Plan*

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
