# RIFT Font Variations

This directory contains **164 logo variations** using **41 different fonts** from Google Fonts, organized across 5 typography categories to give you maximum flexibility in how your brand looks and feels.

## Font Categories & Styles

### Sans-Serif (Modern & Clean) - 12 fonts
**Best for:** Modern, clean, professional brand identity

- **Inter** - Ultra-legible, modern, geometric
- **Montserrat** - Elegant, geometric, premium feel
- **Poppins** - Friendly, rounded, highly legible
- **Space Grotesk** - Geometric, tech-forward, unique
- **Work Sans** - Professional, clean, excellent readability
- **DM Sans** - Modern, versatile, great for digital
- **Outfit** - Contemporary, clean, premium
- **Plus Jakarta Sans** - Modern, friendly, highly legible
- **Manrope** - Geometric, balanced, professional
- **Sora** - Clean, professional, modern
- **Epilogue** - Modern, readable, versatile
- **Nunito Sans** - Friendly, rounded, approachable

### Serif (Elegant & Premium) - 8 fonts
**Best for:** Luxury, sophistication, classic elegance

- **Playfair Display** - Luxury serif, high-contrast, elegant
- **Cormorant Garamond** - Classic, refined, sophisticated
- **Lora** - Warm, approachable, readable serif
- **Merriweather** - Professional, highly legible
- **Libre Baskerville** - Classic, timeless, premium
- **Crimson Text** - Elegant, readable, traditional
- **Cinzel** - Classical, elegant, refined
- **Spectral** - Refined, sophisticated, modern serif

### Display/Decorative (Bold & Expressive) - 14 fonts
**Best for:** Impact, bold statements, dynamic presence

- **Bebas Neue** - Bold, condensed, impactful
- **Oswald** - Condensed, strong, modern
- **Righteous** - Bold, geometric, dynamic
- **Russo One** - Tech-forward, bold, modern
- **Orbitron** - Futuristic, tech-inspired
- **Rajdhani** - Modern, geometric, clean
- **Abril Fatface** - Bold, elegant, high-impact
- **Anton** - Strong, condensed, powerful
- **Black Ops One** - Bold, military-style, impactful
- **Exo 2** - Futuristic, tech-forward
- **Kanit** - Modern, geometric, versatile
- **Raleway** - Elegant, versatile, clean
- **Titillium Web** - Modern, clean, professional
- **Ubuntu** - Friendly, professional, approachable

### Script/Handwritten (Premium & Crafted) - 4 fonts
**Best for:** Artisanal, premium, handcrafted feel

- **Dancing Script** - Elegant, flowing, premium
- **Great Vibes** - Sophisticated, elegant script
- **Pacifico** - Friendly, rounded, approachable
- **Satisfy** - Casual elegance, readable script

### Monospace (Tech & Precision) - 3 fonts
**Best for:** Technical, precision, innovation

- **JetBrains Mono** - Modern, tech-forward, legible
- **Fira Code** - Professional, readable, technical
- **Source Code Pro** - Clean, technical, precise

## Logo Types Per Font

Each font has 4 variations:
1. **Horizontal** (400×120px) - Icon + text side-by-side
2. **Vertical** (300×400px) - Icon above text
3. **Text Only** (400×150px) - Typography only
4. **Compact** (180×60px) - Small space optimized

## Viewing the Variations

### Option 1: Preview HTML (Recommended)
Start a web server and open the preview:

```bash
cd output/font-variations
python3 -m http.server 8002
```

Then open: **http://localhost:8002/preview.html**

The preview is organized by font category with a navigation menu for easy browsing.

### Option 2: Direct SVG Files
Double-click any `.svg` file to view it directly in your browser.

## File Naming Convention

Files are named: `rift-logo-[type]-[font-name].svg`

Examples:
- `rift-logo-horizontal-inter.svg`
- `rift-logo-vertical-bebas-neue.svg`
- `rift-logo-text-only-playfair.svg`
- `rift-logo-compact-orbitron.svg`

Font names use lowercase with hyphens (e.g., `plus-jakarta-sans`, `jetbrains-mono`).

## Brand Personality Guide

Choose fonts based on the brand personality you want to convey:

### Premium/Luxury
- **Serif fonts**: Playfair Display, Cormorant Garamond, Cinzel, Spectral
- **Script fonts**: Great Vibes, Dancing Script
- **Sans-serif**: Montserrat, Outfit

### Modern/Tech
- **Sans-serif**: Space Grotesk, Inter, Sora, Epilogue
- **Display**: Orbitron, Exo 2, Russo One
- **Monospace**: JetBrains Mono, Fira Code

### Bold/Impactful
- **Display fonts**: Bebas Neue, Oswald, Anton, Black Ops One
- **Sans-serif**: Work Sans, Manrope

### Friendly/Approachable
- **Sans-serif**: Poppins, Nunito Sans, Plus Jakarta Sans, Ubuntu
- **Script**: Pacifico, Satisfy

### Classic/Refined
- **Serif**: Libre Baskerville, Merriweather, Lora, Crimson Text
- **Sans-serif**: Montserrat, Raleway

## Usage Tips

1. **Test in context** - View logos on different backgrounds and at various sizes
2. **Consider readability** - Some fonts (especially script and display) work better at larger sizes
3. **Match your audience** - Tech-forward fonts for innovation, serif for luxury, script for artisanal
4. **Consistency** - Use the same font across all your materials once chosen
5. **Web compatibility** - All fonts are from Google Fonts, ensuring excellent web compatibility
6. **Font weights** - Each font is configured with appropriate weights (400, 600, 700, 900) for maximum flexibility

## Technical Details

- **Font Source**: All fonts loaded from Google Fonts CDN
- **Format**: SVG with embedded font imports using CDATA
- **Colors**: 
  - Background: Emerald green (#0d4d3f)
  - Text: White (#ffffff) or Gold (#fbbf24) for text-only variants
  - Icon: Gold (#fbbf24)
- **Letter Spacing**: Optimized per font for best readability
- **Fallback Fonts**: Sans-serif fallbacks specified for each font

## Regenerating

To regenerate all variations:

```bash
python3 scripts/generate-font-variations.py
```

This will:
- Generate 164 SVG logo files (41 fonts × 4 variations)
- Create an updated preview HTML grouped by category
- Update this README

## Total Assets

- **164 SVG logo files** (41 fonts × 4 variations)
- **1 Preview HTML** file with category navigation
- **1 README** file (this document)
- All files use Google Fonts (loaded from CDN)

## Font Selection Recommendations

### For Website Headers
- **Inter**, **Work Sans**, **Sora** - Excellent readability at all sizes

### For Print Materials
- **Playfair Display**, **Cormorant Garamond** - High-quality serif options
- **Montserrat**, **Raleway** - Elegant sans-serif options

### For Social Media
- **Bebas Neue**, **Oswald** - Bold, condensed for small spaces
- **Righteous**, **Anton** - High impact, easily readable

### For Technical Documentation
- **JetBrains Mono**, **Fira Code** - Professional monospace
- **Inter**, **DM Sans** - Clean, readable sans-serif

### For Premium Branding
- **Great Vibes**, **Dancing Script** - Elegant script options
- **Cinzel**, **Spectral** - Sophisticated serif options
