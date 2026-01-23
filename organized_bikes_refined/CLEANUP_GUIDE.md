# Image Organization Cleanup Guide

## Current Status

All bike assets have been organized into the following structure:

```
bike-model/
├── images/
│   ├── clean/      # Clean bike photos (no logos/overlays)
│   ├── details/    # Detail shots
│   ├── colors/    # Color variations
│   └── geometry/  # Geometry diagrams
├── components/    # Component images (groupsets, brakes, etc.)
├── overlays/      # Images with logos/watermarks/overlays (currently empty)
├── comparisons/  # Comparison images (currently empty)
├── specs/        # Specification screenshots
└── videos/       # Video files
```

## ⚠️ Manual Review Required

### 1. Review Clean Images
Check all images in `images/clean/` folders to ensure they:
- ✅ Have no logos or watermarks
- ✅ Have no text overlays
- ✅ Are actual bike photos (not components)
- ✅ Are high quality

**Action**: Move any images with logos/overlays to `overlays/` folder

### 2. Review Component Images
Current component images:
- `CYCLONE-3rd/components/油碟大套.jpeg` - Hydraulic disc brake set
- `CYCLONE-3rd/components/禧玛诺 7170.mp4` - Shimano 7170 video
- `R10pro-disc/components/R10轮峰.mp4` - R10轮峰 video

**Action**: Verify these are actual component images, not bike photos

### 3. Identify Overlay/Logo Images
Look for images that contain:
- Brand logos
- Watermarks
- Text overlays
- Comparison graphics
- Side-by-side images

**Action**: Move these to `overlays/` or `comparisons/` folders

### 4. Remove Duplicates
There are duplicate files with `_1` suffix (created during organization).

**Action**: Review and remove duplicates:
```bash
find organized_bikes_refined -name "*_1.*"
```

### 5. Verify Component Categorization
Check that all component-related images are in `components/`:
- Groupsets (Shimano, SRAM, Campagnolo)
- Brakes
- Wheels
- Other components

**Action**: Move any component images from other folders to `components/`

## Quick Commands

### Find all clean images
```bash
find organized_bikes_refined -path "*/images/clean/*" -type f
```

### Find all component images
```bash
find organized_bikes_refined -path "*/components/*" -type f
```

### Find duplicate files
```bash
find organized_bikes_refined -name "*_1.*"
```

### Count images by category
```bash
for bike in organized_bikes_refined/*/; do
  echo "=== $(basename $bike) ==="
  echo "Clean: $(find "$bike/images/clean" -type f 2>/dev/null | wc -l)"
  echo "Components: $(find "$bike/components" -type f 2>/dev/null | wc -l)"
  echo "Details: $(find "$bike/images/details" -type f 2>/dev/null | wc -l)"
  echo "Colors: $(find "$bike/images/colors" -type f 2>/dev/null | wc -l)"
done
```

## Next Steps After Review

1. ✅ All clean images verified (no logos/overlays)
2. ✅ All component images properly categorized
3. ✅ Overlay/logo images moved to appropriate folders
4. ✅ Duplicate files removed
5. ✅ Ready to add bikes to website database
