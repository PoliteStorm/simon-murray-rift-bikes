#!/usr/bin/env python3
"""
Organize bike assets from extracted zip files.
Separates actual bike photos from spec screenshots and organizes by category.
"""

import os
import shutil
from pathlib import Path

# Base paths
SOURCE_DIR = Path("/home/tau/RIFT/temp_extract")
TARGET_DIR = Path("/home/tau/RIFT/organized_bikes")

# Bike model mappings (from folder names to clean names)
BIKE_MODELS = {
    "CYCLONE-3rd (105 big)": "CYCLONE-3rd",
    "R10pro-disc (ET)": "R10pro-disc",
    "R5pro-Term (2)": "R5pro-Term",
    "T10pro-2rd": "T10pro-2rd"
}

def categorize_file(filename):
    """Categorize a file based on its name."""
    filename_lower = filename.lower()
    
    # Spec screenshots
    if "specification" in filename_lower or "spec" in filename_lower:
        return "specs"
    
    # Geometry diagrams
    if "geometry" in filename_lower or "diagram" in filename_lower:
        return "geometry"
    
    # Videos
    if filename_lower.endswith(('.mp4', '.mov', '.avi', '.webm')):
        return "videos"
    
    # Color variations
    if any(word in filename_lower for word in ["color", "colour", "matte", "black", "white", "gray", "grey", "red"]):
        if "detail" not in filename_lower:
            return "colors"
    
    # Detail shots
    if "detail" in filename_lower or "细节" in filename:
        return "details"
    
    # Main images (default for photos)
    if filename_lower.endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
        return "main"
    
    return "main"

def organize_bike_assets():
    """Organize all bike assets into proper structure."""
    stats = {
        "total_files": 0,
        "organized": 0,
        "by_category": {}
    }
    
    for source_model, target_model in BIKE_MODELS.items():
        # Try different possible source paths
        possible_paths = [
            SOURCE_DIR / source_model / source_model,
            SOURCE_DIR / source_model / source_model.split(" (")[0],  # Remove "(2)" etc
            SOURCE_DIR / source_model,
        ]
        
        source_path = None
        for path in possible_paths:
            if path.exists() and any(path.rglob("*")):
                source_path = path
                break
        
        target_base = TARGET_DIR / target_model
        
        if not source_path:
            print(f"⚠️  Source path not found for {source_model}")
            continue
        
        print(f"\n📦 Organizing {target_model}...")
        
        # Process all files in the source directory
        for file_path in source_path.rglob("*"):
            if file_path.is_file():
                stats["total_files"] += 1
                filename = file_path.name
                category = categorize_file(filename)
                
                # Determine target subdirectory
                if category == "specs":
                    target_subdir = target_base / "specs"
                elif category == "geometry":
                    target_subdir = target_base / "images" / "geometry"
                elif category == "videos":
                    target_subdir = target_base / "videos"
                elif category == "colors":
                    target_subdir = target_base / "images" / "colors"
                elif category == "details":
                    target_subdir = target_base / "images" / "details"
                else:  # main
                    target_subdir = target_base / "images" / "main"
                
                # Create target directory if needed
                target_subdir.mkdir(parents=True, exist_ok=True)
                
                # Copy file with clean name
                target_file = target_subdir / filename
                
                # Handle duplicates
                counter = 1
                while target_file.exists():
                    name_parts = filename.rsplit('.', 1)
                    if len(name_parts) == 2:
                        target_file = target_subdir / f"{name_parts[0]}_{counter}.{name_parts[1]}"
                    else:
                        target_file = target_subdir / f"{filename}_{counter}"
                    counter += 1
                
                try:
                    shutil.copy2(file_path, target_file)
                    stats["organized"] += 1
                    stats["by_category"][category] = stats["by_category"].get(category, 0) + 1
                    print(f"  ✓ {category:10} → {filename}")
                except Exception as e:
                    print(f"  ✗ Error copying {filename}: {e}")
    
    # Print summary
    print("\n" + "="*60)
    print("📊 ORGANIZATION SUMMARY")
    print("="*60)
    print(f"Total files processed: {stats['total_files']}")
    print(f"Successfully organized: {stats['organized']}")
    print(f"\nBy category:")
    for category, count in sorted(stats['by_category'].items()):
        print(f"  {category:12}: {count:3} files")
    print("="*60)
    
    # Create summary file
    summary_file = TARGET_DIR / "ORGANIZATION_SUMMARY.md"
    with open(summary_file, 'w') as f:
        f.write("# Bike Assets Organization Summary\n\n")
        f.write(f"Total files processed: {stats['total_files']}\n")
        f.write(f"Successfully organized: {stats['organized']}\n\n")
        f.write("## Files by Category\n\n")
        for category, count in sorted(stats['by_category'].items()):
            f.write(f"- **{category}**: {count} files\n")
        f.write("\n## Structure\n\n")
        f.write("Each bike model has the following structure:\n")
        f.write("```\n")
        f.write("bike-model/\n")
        f.write("  ├── images/\n")
        f.write("  │   ├── main/        (main bike photos)\n")
        f.write("  │   ├── details/     (detail shots)\n")
        f.write("  │   ├── colors/      (color variations)\n")
        f.write("  │   └── geometry/     (geometry diagrams)\n")
        f.write("  ├── specs/           (specification screenshots)\n")
        f.write("  └── videos/         (video files)\n")
        f.write("```\n")
    
    print(f"\n✅ Summary saved to: {summary_file}")

if __name__ == "__main__":
    organize_bike_assets()
