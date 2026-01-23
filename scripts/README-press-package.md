# RIFT Press Package System

Comprehensive marketing asset generation system for RIFT custom bike shop.

## Overview

This system generates professional marketing assets including:
- **Enhanced Logos**: Rift designs with integrated bike/cog elements (zip-like crack)
- **Social Media Assets**: Banners for Twitter, Facebook, Instagram (posts, stories, reels)
- **Ad Designs**: Multiple variations with slogan "I can, you can, we can Ride It"
- **Overlays & Frames**: Video overlays and frame templates for content

## Brand Identity

### Color Scheme
- **Emerald Dark**: `#0d4d3f`
- **Emerald Mid**: `#0f3d32`
- **Emerald Bright**: `#065f46`
- **Emerald Accent**: `#10b981`
- **Gold**: `#fbbf24`
- **Dark**: `#0a1f1a`

### Slogans
- **Primary**: "I can, you can, we can Ride It"
- **Short**: "Ride It"
- **Tagline**: "Premium Road Cycling. Custom Built."

### Logo Concept
The rift icon represents a crack in the ground that looks like a zip, incorporating bike elements:
- **Chain links** in the top crack
- **Cog/gear elements** in the middle crack
- **Bike chain** in the bottom crack

## Usage

### Generate Basic Press Package
```bash
python scripts/generate-press-package.py
```

### Generate Advanced Designs
```bash
python scripts/generate-press-package-advanced.py
```

### Generate All Assets
```bash
python scripts/generate-press-package.py
python scripts/generate-press-package-advanced.py
```

## Output Structure

```
output/press-package/
├── logos/
│   └── bike-rift/
│       ├── rift-logo-bike-rift-horizontal.svg
│       ├── rift-logo-bike-rift-vertical.svg
│       ├── rift-logo-bike-rift-icon-only.svg
│       └── rift-logo-bike-rift-with-slogan.svg
├── social-media/
│   ├── twitter/
│   │   └── twitter-banner.svg
│   ├── facebook/
│   │   └── facebook-cover.svg
│   ├── instagram/
│   │   ├── instagram-post.svg
│   │   └── instagram-story.svg
│   └── advanced/
│       └── instagram-reel-template.svg
├── ads/
│   ├── ad-full-slogan.svg
│   ├── ad-ride-it-only.svg
│   └── advanced/
│       ├── ad-split-screen.svg
│       └── ad-minimal-modern.svg
├── overlays/
│   └── video-overlay.svg
└── frames/
    └── frame-template.svg
```

## Adding New Content

### Adding New Images/Videos

1. Place images in `PPICS/` directory
2. Place videos in `PPICS/VIDS/` directory
3. Reference them in new generator functions

### Adding New Slogan Variations

Edit `SLOGANS` dictionary in `generate-press-package.py`:
```python
SLOGANS = {
    'primary': "I can, you can, we can\nRide It",
    'your_new': "Your new slogan here",
}
```

### Creating New Ad Designs

Add a new method to the generator class:
```python
def generate_your_new_ad(self):
    """Description of your new ad"""
    w, h = 1200, 800
    content = f'''
    <!-- Your SVG content here -->
    '''
    svg = self.create_svg(w, h, content)
    self.save_file('your-ad-name.svg', svg, 'ads')
```

Then call it in `generate_all()` method.

### Adding New Social Media Formats

1. Add dimensions to `SOCIAL_DIMENSIONS`:
```python
SOCIAL_DIMENSIONS = {
    'new_platform': (width, height),
}
```

2. Create generator method:
```python
def generate_new_platform_banner(self):
    """New platform banner"""
    w, h = SOCIAL_DIMENSIONS['new_platform']
    # Your design code
```

## Design Principles

1. **Premium & Professional**: All designs reflect high-end custom bike craftsmanship
2. **Dynamic & Modern**: Cutting-edge social media trends and engagement
3. **Brand Consistency**: Maintain emerald green and gold color scheme
4. **Bike Integration**: Bike elements naturally integrated into rift design
5. **Slogan Prominence**: "Ride It" as primary call-to-action

## Social Media Best Practices

### Twitter
- Banner: 1500x500px
- Keep text minimal (banners are small)
- Use high contrast

### Facebook
- Cover: 1200x630px
- Posts: 1200x1200px (square)
- Ensure logo/tagline visible on mobile

### Instagram
- Post: 1080x1080px (square)
- Story: 1080x1920px (vertical)
- Reel: 1080x1920px (vertical)
- Use vibrant colors, bold text

## Future Enhancements

- [ ] Animated SVG versions
- [ ] PNG export options
- [ ] Template system for user content
- [ ] Batch processing for multiple images
- [ ] Automated social media posting integration
- [ ] A/B testing variations

## Notes

- All assets are SVG for scalability
- Colors match website color scheme exactly
- Designs are optimized for social media engagement
- System is extensible for future content additions
