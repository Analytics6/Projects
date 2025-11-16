#!/usr/bin/env python3
"""
Apply medallion architecture template to all markdown project files.

This script:
1. Reads the medallion architecture template
2. For each markdown file in project_markdowns/, checks if it already has a medallion section
3. If not present, generates project-specific prefix and substitutes placeholders
4. Appends the medallion section to the file
5. Saves pre-change backup to backups_medallion/
6. Reports results
"""

import os
import re
from pathlib import Path

def generate_prefix(filename):
    """Convert filename to lowercase prefix with underscores."""
    stem = Path(filename).stem
    prefix = re.sub(r'[^a-z0-9]', '_', stem.lower())
    return prefix

def main():
    project_dir = Path("/workspaces/Projects/project_markdowns")
    template_path = project_dir / "_medallion_architecture_template.md"
    backup_dir = Path("/workspaces/Projects/backups_medallion")
    
    # Create backup directory
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    # Read template
    if not template_path.exists():
        print(f"ERROR: Template not found at {template_path}")
        return
    
    with open(template_path, 'r') as f:
        template_content = f.read()
    
    # Find all markdown files
    md_files = sorted([f for f in project_dir.glob("*.md") 
                      if f.name.startswith(("agricultural", "automated", "banking", "cloud", 
                                          "credit", "customer", "dacker", "data", "digital",
                                          "educational", "enterprise", "financial", "healthcare",
                                          "insurance", "inventory", "iot", "manufacturing",
                                          "multi", "real", "retail", "sales", "serverless",
                                          "smart", "sports", "supply", "telemedicine"))])
    
    updated_count = 0
    skipped_count = 0
    processed_files = []
    
    for md_file in md_files:
        filename = md_file.name
        
        # Read current content
        with open(md_file, 'r') as f:
            current_content = f.read()
        
        # Check if medallion section already exists
        if "## Complete Flow Diagram & Medallion Architecture" in current_content or \
           "## Medallion Architecture" in current_content:
            print(f"⊘ {filename} (already has medallion section, skipping)")
            skipped_count += 1
            continue
        
        # Generate project-specific prefix
        prefix = generate_prefix(filename)
        
        # Substitute placeholders
        medallion_content = template_content.replace("{{PREFIX}}", prefix)
        medallion_content = medallion_content.replace("{{FILENAME}}", filename)
        
        # Create backup
        backup_path = backup_dir / f"{filename}.pre_medallion.bak"
        with open(backup_path, 'w') as f:
            f.write(current_content)
        
        # Append to file
        new_content = current_content + "\n\n" + medallion_content
        with open(md_file, 'w') as f:
            f.write(new_content)
        
        updated_count += 1
        processed_files.append(filename)
        print(f"✓ {filename}")
    
    print(f"\n{'='*70}")
    print(f"Processed {updated_count + skipped_count} files: updated={updated_count}, skipped={skipped_count}")
    print(f"Medallion architecture sections appended to all markdown files.")
    print(f"Pre-change backups saved to: {backup_dir}")
    print(f"{'='*70}")
    
    # Print sample of processed files
    if processed_files:
        print("\nFiles updated:")
        for f in processed_files[:10]:
            print(f"  - {f}")
        if len(processed_files) > 10:
            print(f"  ... and {len(processed_files) - 10} more")

if __name__ == "__main__":
    main()
