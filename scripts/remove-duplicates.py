#!/usr/bin/env python3
"""
Remove duplicate files with _1 suffix.
Keeps the original and removes duplicates.
"""

from pathlib import Path

SOURCE_DIR = Path("/home/tau/RIFT/organized_bikes_refined")

def remove_duplicates():
    """Remove duplicate files with _1 suffix."""
    duplicates = []
    removed = 0
    
    for file_path in SOURCE_DIR.rglob("*_1.*"):
        if file_path.is_file():
            # Find original file
            original_name = file_path.name.replace("_1.", ".")
            original_path = file_path.parent / original_name
            
            if original_path.exists():
                duplicates.append((str(original_path), str(file_path)))
                file_path.unlink()
                removed += 1
                print(f"✓ Removed duplicate: {file_path.name}")
    
    print(f"\n✅ Removed {removed} duplicate files")
    return removed

if __name__ == "__main__":
    remove_duplicates()
