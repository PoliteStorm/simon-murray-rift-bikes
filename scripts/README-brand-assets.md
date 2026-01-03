# RIFT Brand Asset Generator

Comprehensive Python script to generate all RIFT brand assets including logos, social media assets, banners, overlays, and specialized assets.

## Usage

```bash
python3 scripts/generate-all-brand-assets.py
```

## Output Structure

The script generates assets in the following directory structure:

```
output/brand-assets/
├── logos/
│   ├── horizontal/          # Horizontal logo layouts
│   ├── vertical/            # Vertical/stacked layouts
│   ├── icon-only/           # Icon-only versions
│   └── text-only/           # Text-only versions
├── social-media/            # Social media assets
├── banners/                 # Website, email, print banners
├── overlays/                # Video overlays and watermarks
├── specialized/
│   ├── favicons/            # Browser favicons (multiple sizes)
│   ├── app-icons/           # iOS and Android app icons
│   └── business-cards/      # Business card logos
└── preview.html             # Interactive preview of all assets
```

## Generated Assets

### Primary Logos (5)
- Horizontal Standard (400×120px)
- Vertical Stacked (200×300px)
- Icon Only (200×200px)
- Text Only (400×150px)
- Compact (180×60px)

### Social Media Assets (11)
- Twitter/X Banner (1500×500px)
- Facebook Cover (1200×630px)
- Instagram PFP (400×400px)
- LinkedIn Banner (1128×191px)
- YouTube Channel Art (2560×1440px)
- TikTok PFP (400×400px)
- Standard PFP (400×400px)
- Premium PFP (400×400px)
- Minimal PFP (400×400px)
- Social Story (1080×1920px)
- Post Template (1080×1080px)

### Banners & Headers (4)
- Website Header (1920×200px)
- Email Header (600×150px)
- Print Banner (2400×600px)
- Mobile Banner (750×200px)

### Overlays & Watermarks (4)
- Video Overlay Standard (300×100px)
- Video Overlay Corner (200×66px)
- Image Watermark (150×150px)
- Transparent Badge (200×200px)

### Specialized Assets (12)
- Favicons: 16×16, 32×32, 48×48, 64×64, 128×128, 256×256px
- iOS App Icon (1024×1024px)
- Android App Icon (512×512px)
- Business Card Logo (300×100px)
- Certificate Badge (300×300px)
- Product Label (200×80px)
- Email Signature (200×60px)

**Total: 36 SVG files + 1 preview HTML**

## Customization

To customize the output:

1. **Change output directory**: Modify the `output_dir` parameter in `main()`
2. **Modify colors**: Update the `COLORS` dictionary at the top of the script
3. **Change taglines**: Update the `TAGLINES` list
4. **Adjust dimensions**: Modify individual asset generation methods

## Brand Colors

- **Emerald Dark**: `#0d4d3f`
- **Emerald Mid**: `#0f3d32`
- **Emerald Bright**: `#065f46`
- **Emerald Accent**: `#10b981`
- **Gold**: `#fbbf24`
- **White**: `#ffffff`
- **Black**: `#000000`

## Preview

After generation, open `output/brand-assets/preview.html` in a web browser to see all assets in an organized, interactive gallery.

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Notes

- All assets are generated as SVG (vector) format for infinite scalability
- Assets use the RIFT volcanic rift icon and custom geometric typography
- All backgrounds are transparent unless specified (banners have colored backgrounds)
- The script automatically creates all necessary directories
