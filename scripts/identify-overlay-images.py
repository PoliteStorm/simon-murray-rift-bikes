#!/usr/bin/env python3
"""
Identify images that might have logos, overlays, or text that need manual review.
Uses file size and basic heuristics to flag potential overlay images.
"""

import os
from pathlib import Path
from PIL import Image
import json

SOURCE_DIR = Path("/home/tau/RIFT/organized_bikes_refined")

def check_image_for_overlays(image_path):
    """Check if image might contain overlays, logos, or text."""
    try:
        img = Image.open(image_path)
        width, height = img.size
        
        # Very small images are often logos/components
        if width < 200 or height < 200:
            return {"flag": "small_image", "reason": f"Very small ({width}x{height}) - might be component/logo"}
        
        # Check file size - very small files might be simple graphics
        file_size = image_path.stat().st_size
        if file_size < 50000:  # Less than 50KB
            return {"flag": "small_file", "reason": f"Small file size ({file_size/1024:.1f}KB) - might be graphic/logo"}
        
        # Very large files might be high-res with overlays
        if file_size > 5000000:  # More than 5MB
            return {"flag": "large_file", "reason": f"Large file ({file_size/1024/1024:.1f}MB) - might have overlays"}
        
        return None
    except Exception as e:
        return {"flag": "error", "reason": str(e)}

def review_images():
    """Review all images and flag potential issues."""
    review_results = {
        "potential_overlays": [],
        "small_images": [],
        "large_images": [],
        "errors": []
    }
    
    for bike_dir in SOURCE_DIR.iterdir():
        if not bike_dir.is_dir() or bike_dir.name.startswith('.'):
            continue
        
        bike_name = bike_dir.name
        print(f"🔍 Reviewing {bike_name}...")
        
        # Check clean images (these should NOT have overlays)
        clean_dir = bike_dir / "images" / "clean"
        if clean_dir.exists():
            for img_file in clean_dir.glob("*"):
                if img_file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
                    result = check_image_for_overlays(img_file)
                    if result:
                        review_results["potential_overlays"].append({
                            "bike": bike_name,
                            "file": str(img_file.relative_to(SOURCE_DIR)),
                            "issue": result["flag"],
                            "reason": result["reason"]
                        })
        
        # Check detail images
        detail_dir = bike_dir / "images" / "details"
        if detail_dir.exists():
            for img_file in detail_dir.glob("*"):
                if img_file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
                    result = check_image_for_overlays(img_file)
                    if result and result["flag"] == "small_image":
                        review_results["small_images"].append({
                            "bike": bike_name,
                            "file": str(img_file.relative_to(SOURCE_DIR))
                        })
    
    # Save review results
    review_file = SOURCE_DIR / "MANUAL_REVIEW_CHECKLIST.md"
    with open(review_file, 'w') as f:
        f.write("# Manual Review Checklist\n\n")
        f.write("## Images That May Need Review\n\n")
        
        if review_results["potential_overlays"]:
            f.write("### ⚠️ Potential Overlay/Logo Images in 'clean' folder\n\n")
            f.write("These images are in the 'clean' folder but may contain logos, overlays, or text:\n\n")
            for item in review_results["potential_overlays"]:
                f.write(f"- **{item['bike']}**: `{item['file']}`\n")
                f.write(f"  - Issue: {item['issue']}\n")
                f.write(f"  - Reason: {item['reason']}\n\n")
        else:
            f.write("### ✅ No obvious overlay issues found in clean images\n\n")
        
        f.write("\n## Next Steps\n\n")
        f.write("1. Manually review all images in `images/clean/` folders\n")
        f.write("2. Move any images with logos/overlays to `overlays/` folder\n")
        f.write("3. Move any component images to `components/` folder\n")
        f.write("4. Verify all images are correctly categorized\n")
        f.write("5. Remove duplicate files (_1 versions)\n")
    
    print(f"\n✅ Review complete!")
    print(f"📄 Checklist saved to: {review_file}")
    print(f"\nFound {len(review_results['potential_overlays'])} potential issues")

if __name__ == "__main__":
    review_images()
