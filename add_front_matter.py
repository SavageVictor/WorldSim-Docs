#!/usr/bin/env python3
"""
Add Just the Docs front matter to existing markdown files
"""

import os

# Front matter templates for each document
FRONT_MATTERS = {
    'AI_Systems_Core.md': '''---
layout: default
title: AI Systems - Core
parent: Documentation
nav_order: 1
has_toc: true
---

''',
    
    'AI_Systems_Enhancements.md': '''---
layout: default
title: AI Systems - Enhancements
parent: Documentation
nav_order: 2
has_toc: true
---

''',
    
    'Economic_Systems_Core.md': '''---
layout: default
title: Economic Systems - Core
parent: Documentation
nav_order: 3
has_toc: true
---

''',
    
    'Economic_Systems_Enhancements.md': '''---
layout: default
title: Economic Systems - Enhancements
parent: Documentation
nav_order: 4
has_toc: true
---

'''
}

def add_front_matter(filepath, front_matter):
    """Add front matter to a file if it doesn't already have it"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has front matter
    if content.startswith('---'):
        print(f"⚠ {filepath} already has front matter, skipping")
        return False
    
    # Add front matter
    new_content = front_matter + content
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✓ Added front matter to {filepath}")
    return True

def create_parent_page(directory):
    """Create a parent page for the documentation section"""
    parent_content = '''---
layout: default
title: Documentation
nav_order: 2
has_children: true
permalink: /docs
---

# Documentation

Select a document from the navigation menu to begin.
'''
    
    parent_path = os.path.join(directory, 'index.md')
    
    # Only create if doesn't exist
    if not os.path.exists(parent_path):
        with open(parent_path, 'w', encoding='utf-8') as f:
            f.write(parent_content)
        print(f"✓ Created parent page: {parent_path}")
        return True
    else:
        print(f"⚠ Parent page already exists: {parent_path}")
        return False

# Main execution
print("Adding Just the Docs front matter to documentation files...")
print("=" * 60)

docs_dir = 'HighLevelOverview'

# Create the directory if it doesn't exist
if not os.path.exists(docs_dir):
    print(f"⚠ Directory {docs_dir} doesn't exist. Creating it...")
    os.makedirs(docs_dir)

# Create parent index page
create_parent_page(docs_dir)

print()

# Process each file
for filename, front_matter in FRONT_MATTERS.items():
    filepath = os.path.join(docs_dir, filename)
    
    if os.path.exists(filepath):
        add_front_matter(filepath, front_matter)
    else:
        print(f"✗ File not found: {filepath}")

print("=" * 60)
print("Done!")
print()
print("Next steps:")
print("1. Rename _config_simple.yml to _config.yml")
print("2. Rename index_simple.md to index.md")
print("3. Commit and push to GitHub")
print("4. Enable GitHub Pages in Settings")
