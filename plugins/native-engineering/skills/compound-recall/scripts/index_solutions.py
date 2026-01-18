#!/usr/bin/env python3
import os
import json
import re
from pathlib import Path
from datetime import datetime

def parse_simple_yaml(yaml_text):
    """
    Very basic YAML parser for standard frontmatter.
    Only supports key: value and simple lists.
    """
    data = {}
    lines = yaml_text.strip().split('\n')
    current_key = None
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
        # List items: "- item"
        if line.startswith('- ') and current_key:
            val = line[2:].strip().strip('"').strip("'")
            if not isinstance(data.get(current_key), list):
                data[current_key] = []
            data[current_key].append(val)
            continue
            
        # Key: Value pairs
        match = re.match(r'^([^:]+):\s*(.*)$', line)
        if match:
            key = match.group(1).strip()
            val = match.group(2).strip()
            
            # Handle inline list [a, b]
            if val.startswith('[') and val.endswith(']'):
                val = [v.strip().strip('"').strip("'") for v in val[1:-1].split(',')]
                data[key] = val
            elif not val: # Start of a list
                current_key = key
                data[key] = []
            else:
                data[key] = val.strip('"').strip("'")
                current_key = key
                
    return data

def extract_frontmatter(content):
    """Extracts metadata from markdown content using regex."""
    match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if match:
        return parse_simple_yaml(match.group(1))
    return None

def extract_keywords(text):
    """Extracts potential search keywords from text."""
    # Convert to lowercase and find words with 3+ characters
    words = re.findall(r'\b[a-z]{3,}\b', text.lower())
    # Exclude common stop words (minimal set)
    stop_words = {'the', 'and', 'for', 'with', 'from', 'this', 'that', 'when', 'failed', 'issue', 'problem', 'fixed', 'solution'}
    return list(set(words) - stop_words)

def build_index(solutions_dir="docs/solutions", output_path="plugins/native-engineering/skills/compound-recall/references/knowledge-index.json"):
    """Scans solutions and builds a structured index."""
    index = {
        "version": "1.1",
        "last_updated": datetime.now().isoformat(),
        "total_solutions": 0,
        "solutions": [],
        "tag_index": {},
        "error_index": {},
        "keyword_index": {}
    }
    
    base_dir = Path(os.getcwd())
    solutions_path = base_dir / solutions_dir
    
    if not solutions_path.exists():
        print(f"Warning: {solutions_dir} does not exist.")
        solutions_path.mkdir(parents=True, exist_ok=True)

    for md_file in solutions_path.rglob("*.md"):
        if md_file.name.startswith('.'):
            continue
            
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                metadata = extract_frontmatter(content)
                
                if metadata:
                    sol_id = md_file.stem
                    rel_path = str(md_file.relative_to(base_dir))
                    
                    # Create search vector from title and symptoms
                    search_content = f"{sol_id} {' '.join(metadata.get('symptoms', []))}"
                    keywords = extract_keywords(search_content)
                    
                    solution_entry = {
                        "id": sol_id,
                        "path": rel_path,
                        "category": md_file.parent.name,
                        "metadata": metadata,
                        "keywords": keywords
                    }
                    index["solutions"].append(solution_entry)
                    
                    # 1. Tag index
                    tags = metadata.get("tags", [])
                    if isinstance(tags, list):
                        for tag in tags:
                            tag = tag.lower()
                            if tag not in index["tag_index"]:
                                index["tag_index"][tag] = []
                            index["tag_index"][tag].append(sol_id)
                            
                    # 2. Error index (Haiku-style heuristic)
                    symptoms = metadata.get("symptoms", [])
                    if isinstance(symptoms, list):
                        for symptom in symptoms:
                            # Match error classes: Redis::TimeoutError, NameError
                            matches = re.findall(r'[A-Z]\w+(?:::[A-Z]\w+)*Error', symptom)
                            for match in matches:
                                if match not in index["error_index"]:
                                    index["error_index"][match] = []
                                if sol_id not in index["error_index"][match]:
                                    index["error_index"][match].append(sol_id)
                    
                    # 3. Keyword index (Search Vector)
                    for kw in keywords:
                        if kw not in index["keyword_index"]:
                            index["keyword_index"][kw] = []
                        if sol_id not in index["keyword_index"][kw]:
                            index["keyword_index"][kw].append(sol_id)

        except Exception as e:
            print(f"Error processing {md_file}: {e}")

    index["total_solutions"] = len(index["solutions"])
    
    output_file = base_dir / output_path
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    print(f"✓ Indexed {index['total_solutions']} solutions into {output_path}")

if __name__ == "__main__":
    build_index()
