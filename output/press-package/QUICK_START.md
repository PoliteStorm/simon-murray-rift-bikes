# RIFT Press Package - Quick Start Guide

## 🚀 Quick Generation

Run this command to generate ALL press package assets:

```bash
./scripts/generate-all-press-assets.sh
```

Or generate individually:

```bash
# Basic press package
python3 scripts/generate-press-package.py

# Advanced designs
python3 scripts/generate-press-package-advanced.py

# Extended variations
python3 scripts/generate-press-package-extended.py
```

## 📁 Asset Locations

All generated assets are in `output/press-package/`:

### Logos
- `logos/bike-rift/` - Enhanced logos with bike/cog elements in rift

### Social Media
- `social-media/twitter/` - Twitter banners
- `social-media/facebook/` - Facebook covers
- `social-media/instagram/` - Instagram posts, stories, reels
- `social-media/advanced/` - Advanced social media designs
- `social-media/variations/` - Carousel templates and variations

### Ads
- `ads/` - Main ad designs
- `ads/advanced/` - Split-screen, minimal modern designs
- `ads/variations/` - Multiple slogan variations

### Other
- `overlays/` - Video overlay templates
- `frames/` - Frame templates for content
- `banners/` - Wide banner variations

## 🎨 Brand Assets

### Colors
- **Emerald Dark**: `#0d4d3f`
- **Gold**: `#fbbf24`
- **White**: `#ffffff`
- **Dark**: `#0a1f1a`

### Slogans
- **Primary**: "I can, you can, we can Ride It"
- **Short**: "Ride It"
- **Tagline**: "Premium Road Cycling. Custom Built."

## 📐 Social Media Dimensions

- **Twitter Banner**: 1500x500px
- **Facebook Cover**: 1200x630px
- **Facebook Post**: 1200x1200px
- **Instagram Post**: 1080x1080px
- **Instagram Story**: 1080x1920px
- **Instagram Reel**: 1080x1920px

## ✨ Key Features

1. **Bike-Integrated Rift Logo**: The crack/rift includes bike elements (chain links, cogs, gears)
2. **Multiple Slogan Variations**: Various layouts with "Ride It" and full slogan
3. **Social Media Ready**: All assets sized for specific platforms
4. **Scalable SVG**: All designs are vector-based for any size
5. **Extensible System**: Easy to add new designs and content

## 🔄 Adding Your Content

### Adding Images
1. Place images in `PPICS/` directory
2. Reference in generator scripts using `<image>` tags

### Adding Videos
1. Place videos in `PPICS/VIDS/` directory
2. Use overlay templates to add branding

### Creating New Designs
1. Edit generator scripts in `scripts/`
2. Add new methods following existing patterns
3. Run generation scripts

## 📝 Next Steps

1. Review generated assets in `output/press-package/`
2. Customize designs as needed
3. Export to PNG/JPG if needed for specific platforms
4. Use overlays on your videos/images
5. Add your content to templates

## 💡 Tips

- All SVGs can be opened in browsers, design software, or converted to PNG
- Use frame templates to create consistent ad layouts
- Video overlays can be composited with your video content
- Social media assets are optimized for each platform's requirements

---

**Need help?** Check `scripts/README-press-package.md` for detailed documentation.
