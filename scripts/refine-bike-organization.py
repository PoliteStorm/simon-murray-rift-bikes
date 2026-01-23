#!/usr/bin/env python3
"""
Refine bike asset organization:
- Separate component images
- Separate logo/overlay/edited images
- Keep clean bike images separate
- Organize components properly
"""

import os
import shutil
from pathlib import Path
from PIL import Image
import re

SOURCE_DIR = Path("/home/tau/RIFT/organized_bikes")
TARGET_DIR = Path("/home/tau/RIFT/organized_bikes_refined")

# Keywords to identify different image types
COMPONENT_KEYWORDS = [
    "component", "groupset", "shimano", "sram", "campagnolo", "brake", "brakes",
    "disc", "rotor", "crank", "chain", "cassette", "derailleur", "shift", "gear",
    "wheel", "rim", "tire", "tyre", "hub", "pedal", "saddle", "handlebar", "stem",
    "fork", "shock", "suspension", "motor", "battery", "di2", "etap", "axs",
    "禧玛诺", "油碟", "大套", "轮峰"  # Chinese component terms
]

LOGO_OVERLAY_KEYWORDS = [
    "logo", "brand", "overlay", "watermark", "text", "label", "badge", "sticker",
    "comparison", "compare", "vs", "versus", "side by side", "split"
]

COMPARISON_KEYWORDS = [
    "comparison", "compare", "vs", "versus", "side by side", "split", "before after",
    "difference", "对比"
]

DETAIL_KEYWORDS = [
    "detail", "details", "close", "closeup", "macro", "texture", "finish", "paint",
    "细节"
]

COLOR_KEYWORDS = [
    "color", "colour", "matte", "black", "white", "gray", "grey", "red", "blue",
    "green", "yellow", "orange", "purple", "pink", "silver", "gold"
]

def analyze_image_content(image_path):
    """Analyze image to detect if it contains logos, text, or overlays."""
    try:
        img = Image.open(image_path)
        # Simple heuristic: check if image is very small (likely a component/logo)
        width, height = img.size
        if width < 500 or height < 500:
            return {"likely_component": True, "likely_overlay": False}
        
        # For now, rely on filename analysis
        # In future, could use OCR or image analysis
        return {"likely_component": False, "likely_overlay": False}
    except Exception as e:
        return {"likely_component": False, "likely_overlay": False}

def categorize_image(filename, filepath):
    """Categorize an image based on filename and content."""
    filename_lower = filename.lower()
    
    # FIRST: Check if it's a spec/geometry (these take priority)
    if "specification" in filename_lower or ("spec" in filename_lower and "component" not in filename_lower):
        return "specs"
    if "geometry" in filename_lower or "diagram" in filename_lower:
        return "geometry"
    
    # Check for component images (but not geometry/specs)
    # Chinese component terms
    if any(term in filename for term in ["油碟", "大套", "禧玛诺", "轮峰"]):
        return "components"
    # Component keywords
    if any(keyword in filename_lower for keyword in ["shimano", "sram", "campagnolo", "di2", "etap", "axs", "7170", "7170"]):
        return "components"
    # Component-specific terms
    if any(keyword in filename_lower for keyword in ["brake", "brakes", "disc", "rotor", "crank", "chain", "cassette", "derailleur", "groupset"]):
        return "components"
    
    # Check for logo/overlay images
    if any(keyword in filename_lower for keyword in LOGO_OVERLAY_KEYWORDS):
        return "overlays"
    
    # Check for comparison images
    if any(keyword in filename_lower for keyword in COMPARISON_KEYWORDS):
        return "comparisons"
    
    # Check for detail images
    if any(keyword in filename_lower for keyword in DETAIL_KEYWORDS):
        return "details"
    
    # Check for color variations
    if any(keyword in filename_lower for keyword in COLOR_KEYWORDS):
        return "colors"
    
    # Default to main/clean image
    return "clean"

def refine_organization():
    """Refine the organization with better categorization."""
    stats = {
        "total": 0,
        "by_category": {},
        "by_bike": {}
    }
    
    # Create new structure
    for bike_dir in SOURCE_DIR.iterdir():
        if not bike_dir.is_dir() or bike_dir.name.startswith('.'):
            continue
        
        bike_name = bike_dir.name
        print(f"\n📦 Processing {bike_name}...")
        
        target_bike_dir = TARGET_DIR / bike_name
        target_bike_dir.mkdir(parents=True, exist_ok=True)
        
        # Create refined structure
        structure = {
            "images": {
                "clean": [],      # Clean bike photos
                "details": [],    # Detail shots
                "colors": [],     # Color variations
                "geometry": []    # Geometry diagrams
            },
            "components": [],      # Component images
            "overlays": [],       # Images with logos/overlays
            "comparisons": [],   # Comparison images
            "specs": [],         # Spec screenshots
            "videos": []         # Videos (keep as is)
        }
        
        # Process all files
        for file_path in bike_dir.rglob("*"):
            if file_path.is_file():
                stats["total"] += 1
                filename = file_path.name
                category = categorize_image(filename, file_path)
                
                # Determine target location
                if category == "components":
                    structure["components"].append(file_path)
                elif category == "overlays":
                    structure["overlays"].append(file_path)
                elif category == "comparisons":
                    structure["comparisons"].append(file_path)
                elif category == "specs":
                    structure["specs"].append(file_path)
                elif category == "geometry":
                    structure["images"]["geometry"].append(file_path)
                elif category == "details":
                    structure["images"]["details"].append(file_path)
                elif category == "colors":
                    structure["images"]["colors"].append(file_path)
                elif file_path.suffix.lower() in ['.mp4', '.mov', '.avi', '.webm']:
                    structure["videos"].append(file_path)
                else:
                    structure["images"]["clean"].append(file_path)
        
        # Copy files to new structure
        for category, files in structure.items():
            if category == "images":
                for subcat, subfiles in files.items():
                    if subfiles:
                        target_subdir = target_bike_dir / "images" / subcat
                        target_subdir.mkdir(parents=True, exist_ok=True)
                        for file_path in subfiles:
                            target_file = target_subdir / file_path.name
                            shutil.copy2(file_path, target_file)
                            stats["by_category"][f"images/{subcat}"] = stats["by_category"].get(f"images/{subcat}", 0) + 1
                            print(f"  ✓ images/{subcat:10} → {file_path.name}")
            else:
                if files:
                    target_subdir = target_bike_dir / category
                    target_subdir.mkdir(parents=True, exist_ok=True)
                    for file_path in files:
                        target_file = target_subdir / file_path.name
                        shutil.copy2(file_path, target_file)
                        stats["by_category"][category] = stats["by_category"].get(category, 0) + 1
                        print(f"  ✓ {category:12} → {file_path.name}")
        
        stats["by_bike"][bike_name] = sum(len(files) if isinstance(files, list) else sum(len(v) for v in files.values() if isinstance(v, list)) for files in structure.values())
    
    # Print summary
    print("\n" + "="*60)
    print("📊 REFINED ORGANIZATION SUMMARY")
    print("="*60)
    print(f"Total files processed: {stats['total']}")
    print(f"\nBy category:")
    for category, count in sorted(stats['by_category'].items()):
        print(f"  {category:20}: {count:3} files")
    print(f"\nBy bike:")
    for bike, count in sorted(stats['by_bike'].items()):
        print(f"  {bike:20}: {count:3} files")
    print("="*60)
    
    # Create summary document
    summary_file = TARGET_DIR / "REFINED_ORGANIZATION.md"
    with open(summary_file, 'w') as f:
        f.write("# Refined Bike Assets Organization\n\n")
        f.write("## Structure\n\n")
        f.write("```\n")
        f.write("bike-model/\n")
        f.write("├── images/\n")
        f.write("│   ├── clean/      # Clean bike photos (no logos/overlays)\n")
        f.write("│   ├── details/     # Detail shots\n")
        f.write("│   ├── colors/     # Color variations\n")
        f.write("│   └── geometry/   # Geometry diagrams\n")
        f.write("├── components/     # Component images (groupsets, brakes, etc.)\n")
        f.write("├── overlays/       # Images with logos/watermarks/overlays\n")
        f.write("├── comparisons/   # Comparison images\n")
        f.write("├── specs/         # Specification screenshots\n")
        f.write("└── videos/       # Video files\n")
        f.write("```\n\n")
        f.write("## Statistics\n\n")
        f.write(f"- Total files: {stats['total']}\n")
        f.write(f"\n### By Category\n\n")
        for category, count in sorted(stats['by_category'].items()):
            f.write(f"- **{category}**: {count} files\n")
    
    print(f"\n✅ Refined organization complete!")
    print(f"📁 Location: {TARGET_DIR}")
    print(f"📄 Summary: {summary_file}")

if __name__ == "__main__":
    refine_organization()
