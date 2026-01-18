#!/usr/bin/env python3
import os
import json
import re
import argparse
from pathlib import Path

def parse_simple_yaml(yaml_text):
    data = {}
    lines = yaml_text.strip().split('\n')
    current_key = None
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'): continue
        if line.startswith('- ') and current_key:
            val = line[2:].strip().strip('"').strip("'")
            if not isinstance(data.get(current_key), list): data[current_key] = []
            data[current_key].append(val)
            continue
        match = re.match(r'^([^:]+):\s*(.*)$', line)
        if match:
            key = match.group(1).strip()
            val = match.group(2).strip()
            if val.startswith('[') and val.endswith(']'):
                val = [v.strip().strip('"').strip("'") for v in val[1:-1].split(',')]
                data[key] = val
            elif not val: current_key = key
            else:
                data[key] = val.strip('"').strip("'")
                current_key = key
    return data

def extract_frontmatter(content):
    match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if match: return parse_simple_yaml(match.group(1))
    return None

def score_solution(metadata, query_tags, query_errors, query_keywords):
    score = 0
    # 1. Error Match (Highest weight)
    symptoms = metadata.get("symptoms", [])
    if isinstance(symptoms, list):
        content_errors = re.findall(r'[A-Z]\w+(?:::[A-Z]\w+)*Error', " ".join(symptoms))
        for err in query_errors:
            if err in content_errors: score += 10

    # 2. Tag Intersection
    sol_tags = [t.lower() for t in metadata.get("tags", []) if isinstance(t, str)]
    for tag in query_tags:
        if tag.lower() in sol_tags: score += 5

    # 3. Keyword Match
    title = metadata.get("title", "").lower()
    for kw in query_keywords:
        if kw.lower() in title: score += 2
        
    return score

def find_matches(query_tags, query_errors, query_keywords, solutions_dir="docs/solutions"):
    base_dir = Path(os.getcwd())
    solutions_path = base_dir / solutions_dir
    
    if not solutions_path.exists():
        return []

    results = []
    for md_file in solutions_path.rglob("*.md"):
        if md_file.name.startswith('.'): continue
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                metadata = extract_frontmatter(content)
                if metadata:
                    score = score_solution(metadata, query_tags, query_errors, query_keywords)
                    if score > 0:
                        results.append({
                            "id": md_file.stem,
                            "path": str(md_file.relative_to(base_dir)),
                            "title": metadata.get("title", md_file.stem),
                            "severity": metadata.get("severity", "medium"),
                            "score": score
                        })
        except Exception: continue

    # Sort by score (desc) and then by severity
    severity_map = {"critical": 3, "high": 2, "medium": 1, "low": 0}
    results.sort(key=lambda x: (x["score"], severity_map.get(x["severity"], 0)), reverse=True)
    return results[:5] # Return top 5

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flash Recall Matcher")
    parser.add_argument("--tags", help="Comma separated tags")
    parser.add_argument("--errors", help="Comma separated error signatures")
    parser.add_argument("--keywords", help="Comma separated keywords")
    args = parser.parse_args()

    tags = args.tags.split(',') if args.tags else []
    errors = args.errors.split(',') if args.errors else []
    keywords = args.keywords.split(',') if args.keywords else []

    matches = find_matches(tags, errors, keywords)
    print(json.dumps(matches, indent=2, ensure_ascii=False))
