# 工具输出卸载模板

当工具输出超过阈值（约 2000 tokens）时，使用此模式将输出写入文件系统，避免上下文膨胀。

## 理论基础

此模式基于 `skill:filesystem-context` 的文件系统上下文管理策略。

如需深入理解，请参考 Agent-Skills-for-Context-Engineering：
- `skill:filesystem-context` - 文件系统作为上下文接口
- `skill:context-optimization` - 观察掩蔽（Observation Masking）

## 核心原理

**问题**：工具调用可能返回大量输出（搜索结果 10k tokens，数据库查询数百行）。如果这些内容进入消息历史，它会在整个对话期间保持膨胀，占用 token 成本并可能降低对更相关信息的注意力。

**解决方案**：将大型工具输出写入文件而不是直接返回到上下文。Agent 然后使用目标检索（grep、行特定读取）仅提取相关部分。

## 卸载流程

```python
def handle_tool_output(output: str, tool_name: str, threshold: int = 2000) -> str:
    """处理工具输出，超过阈值时卸载到文件系统。"""
    if len(output) < threshold:
        return output
    
    # 写入 scratch pad
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"scratch/{tool_name}_{timestamp}.txt"
    write_file(file_path, output)
    
    # 生成摘要
    key_summary = extract_summary(output, max_tokens=200)
    
    # 返回引用而非完整内容
    return f"""[Output written to {file_path}]

**Summary ({len(output)} chars, ~{len(output)//4} tokens):**
{key_summary}

Use `grep -n "pattern" {file_path}` or `read_file {file_path} [start:end]` for details.
"""
```

## 摘要提取指南

有效的摘要应保留：
- **关键发现**：主要结论、重要数据点
- **位置引用**：关键信息在原文中的行号
- **模式提示**：帮助后续 grep 搜索的关键词

**示例摘要**：

```markdown
**Summary (3 key findings):**
1. API rate limit is 1000 req/min (见 line 45-47)
2. Authentication uses JWT with 24h expiry (见 line 123-130)
3. Rate limiting applies per-API-key basis (见 line 89-95)

Keywords for grep: `rate_limit`, `JWT`, `expires_in`
```

## 使用场景

### 场景 1: Web 搜索结果

```
Before (填充上下文):
Agent: [返回8000 tokens的搜索结果]

After (卸载模式):
Agent: 
[Output written to scratch/web_search_20260121_143022.txt]

**Summary:**
1. Official docs confirm API v2 deprecated (line 12-15)
2. Migration guide available at docs.example.com (line 45)
3. Breaking changes listed in CHANGELOG (line 78-120)
```

### 场景 2: 代码库搜索

```
Before (填充上下文):
Agent: [返回500个匹配结果]

After (卸载模式):
Agent:
[Output written to scratch/grep_redis_20260121_143055.txt]

**Summary (500 matches):**
- Most matches in: app/services/ (180), lib/ (120)
- Key files: redis_client.rb (45), cache_service.rb (38)
```

## 文件组织

```
project/
├── scratch/                    # 临时工作文件
│   ├── web_search_*.txt        # Web 搜索结果
│   ├── grep_*.txt              # 代码搜索结果
│   └── query_*.txt             # 数据库查询结果
└── ...
```

## 清理策略

```bash
# 清理超过7天的临时文件
find scratch/ -name "*.txt" -mtime +7 -delete
```

## Token 节省估算

| 场景 | 原始 tokens | 卸载后 tokens | 节省比例 |
|------|------------|---------------|---------|
| Web 搜索 (8k chars) | ~2000 | ~100 | 95% |
| Grep 搜索 (500 matches) | ~3000 | ~150 | 95% |
| SQL 查询 (200 rows) | ~1500 | ~80 | 95% |

## 相关资源

**Agent-Skills-for-Context-Engineering 技能**：
- `skill:filesystem-context` - 文件系统上下文模式
- `skill:context-optimization` - 观察掩蔽策略

**Native Engineering 组件**：
- `/workflow:compound` - 将有价值的卸载内容记录为解决方案
- `skill:compound-recall` - 未来检索已记录的知识
