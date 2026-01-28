---
name: context-health
description: Quick context health diagnosis, detect four degradation patterns and apply WSCI four-bucket strategies
argument-hint: "[optional: specific symptom to diagnose]"
---

# /context-health

Quick context health diagnostic tool.

## Built-in Capabilities

This command uses **Native Engineering Plugin built-in** context engineering skills:
- `context-degradation` - Four degradation patterns explained (Lost-in-Middle, Context Poisoning, Context Distraction, Context Clash)
- `context-optimization` - WSCI four-bucket strategies (Write, Select, Compress, Isolate)
- `context-compression` - Advanced compression strategies
- `context-fundamentals` - Context fundamentals theory

No external dependencies needed, all skills are built into this plugin.

## Usage

```bash
/context-health                    # Comprehensive diagnosis
/context-health poisoning          # Specific symptom diagnosis
```

## Diagnostic Protocol

When executing this command, follow these steps:

### Step 1: Activate Context Engineering Knowledge

Using the built-in **context-degradation** skill, understand the four context degradation patterns:
- **Lost-in-Middle**: Attention drops for information in the middle
- **Context Poisoning**: Errors accumulate and propagate
- **Context Distraction**: Irrelevant information interferes with attention
- **Context Clash**: Conflicting information causes decision swings

### Step 2: Symptom Identification

Check for the following degradation signals (based on conversation history and current task):

| Degradation Type | Detection Signal | Severity |
|------------------|-----------------|----------|
| **Lost-in-Middle** | Agent ignores previously provided key information | 🟡 Medium |
| **Context Poisoning** | Agent repeats same type of error, recurs after correction | 🔴 High |
| **Context Distraction** | Agent response deviates from current task topic | 🟡 Medium |
| **Context Clash** | Agent outputs contradictory conclusions, decision swings | 🔴 High |

### Step 3: Apply Mitigation Strategies

Based on detected symptoms, apply WSCI four-bucket strategies from built-in **context-optimization** skill:

| Strategy | Application Scenario |
|----------|---------------------|
| **Write** | Offload large outputs to scratch/ directory |
| **Select** | Use Compound Recall for selective retrieval |
| **Compress** | Generate structured summary (reference session-summary template) |
| **Isolate** | Use parallel agents to isolate context |

### Step 4: Generate Diagnostic Report

```markdown
## 🩺 Context Health Diagnostic Report

**Diagnosis Time**: [timestamp]
**Conversation Rounds**: [count]

### Detected Symptoms

| Symptom | Detection Status | Severity | Suggested Action |
|---------|-----------------|----------|------------------|
| Lost-in-Middle | ✅/❌ | 🟡/🔴 | [Description] |
| Context Poisoning | ✅/❌ | 🟡/🔴 | [Description] |
| Context Distraction | ✅/❌ | 🟡/🔴 | [Description] |
| Context Clash | ✅/❌ | 🟡/🔴 | [Description] |

### Suggested Actions

[Mitigation strategies based on context-optimization built-in skill]
```

## Quick Reference

```
┌────────────────────────────────────────────────────────────────────┐
│                    Context Degradation Quick Guide                  │
├────────────────────────────────────────────────────────────────────┤
│  Symptom: Agent "forgets" key information                           │
│  └─ Prescription: Re-state, place at beginning                     │
│                                                                     │
│  Symptom: Agent repeats same type of error                          │
│  └─ Prescription: Explicitly correct or start new conversation     │
│                                                                     │
│  Symptom: Agent response deviates from topic                        │
│  └─ Prescription: Focus instructions, remove irrelevant context     │
│                                                                     │
│  Symptom: Agent outputs contradictory conclusions                    │
│  └─ Prescription: Mark conflicts, determine priority                │
└────────────────────────────────────────────────────────────────────┘
```

## Integration with Native Engineering

This command works with the following built-in skills of Native Engineering Plugin:

| Built-in Skill | Purpose |
|----------------|---------|
| `context-degradation` | Theoretical foundation: four degradation patterns |
| `context-optimization` | Mitigation strategies: WSCI four buckets |
| `context-compression` | Advanced compression strategies (on-demand) |
| `context-fundamentals` | Context fundamentals theory |

## Native Engineering Integration

Works with the following components of this plugin:

- **compound-recall-researcher**: Detect Context Clash
- **workflow:work**: Position sensitivity best practices
- **workflow:compound**: Document correct solutions to prevent Poisoning
