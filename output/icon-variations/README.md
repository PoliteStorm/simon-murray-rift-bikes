# RIFT Icon Variations

This directory contains **34+ icon variations** of the RIFT volcanic rift icon, organized by complexity, style, integration, color, and size optimizations.

## Icon Structure

The RIFT icon represents volcanic/tectonic movement with:
- **Three horizontal lines** (representing tectonic plates)
- **Angular cracks** extending upward from the lines (representing volcanic activity)
- **Geometric design** reflecting the "edge of biking technology" concept

## Variation Categories

### 1. Complexity Variations (5 versions)
- **Minimal**: Ultra-simplified, just essential lines (no cracks)
- **Standard**: Current design with three lines and angular cracks
- **Enhanced**: Additional detail lines and more cracks
- **Detailed**: Complex pattern with multiple layers of cracks
- **Ornate**: Decorative elements and flourishes

### 2. Style Variations (6 versions)
- **Geometric**: Sharp angles, precise lines, square caps
- **Organic**: Curved, flowing lines with rounded caps
- **Tech**: Futuristic, digital aesthetic with gradients and glow
- **Classic**: Traditional, refined with rounded caps
- **Bold**: Thick strokes (6px), high contrast
- **Subtle**: Thin lines (1.5px), delicate appearance

### 3. Integration Variations (4 versions)
- **Standalone**: Icon only, no decorative elements
- **Framed**: Icon within decorative rectangular border
- **Badge**: Icon in circular badge
- **Square Badge**: Icon in square badge with rounded corners

### 4. Color Variations (4 versions)
- **Standard**: Gold (#fbbf24) on emerald green (#0d4d3f)
- **Inverted**: Emerald on gold background
- **Monochrome Gold**: Gold icon on transparent background
- **Monochrome Emerald**: Emerald icon on transparent background
- **Gradient**: Gold to emerald gradient fill

### 5. Size Optimizations (15 versions)
Optimized for different use cases:
- **Micro** (16×16px): Simplest form, recognizable at tiny size
  - Minimal, Standard, Bold styles
- **Small** (32×32px): Favicon optimized
  - Minimal, Standard, Bold styles
- **Medium** (64×64px): Standard icon size
  - Minimal, Standard, Bold styles
- **Large** (128×128px): Full detail visible
  - Minimal, Standard, Bold styles
- **Hero** (256×256px): Maximum detail, decorative
  - Minimal, Standard, Bold styles

## Viewing the Variations

### Option 1: Preview HTML (Recommended)
Start a web server and open the preview:

```bash
cd output/icon-variations
python3 -m http.server 8003
```

Then open: **http://localhost:8003/preview.html**

### Option 2: Direct SVG Files
Double-click any `.svg` file to view it directly in your browser.

## File Naming Convention

Files are named: `rift-icon-[variation]-[size]px.svg`

Examples:
- `rift-icon-minimal-100px.svg`
- `rift-icon-geometric-100px.svg`
- `rift-icon-badge-100px.svg`
- `rift-icon-standard-16px.svg`

## Usage Guidelines

### For Favicons
- Use **minimal-16px** or **minimal-32px** for best recognition at small sizes
- Use **standard-32px** for more detail

### For App Icons
- Use **standard-64px** or **standard-128px**
- Consider **badge** or **square-badge** versions for app stores

### For Website Headers
- Use **standard-100px** or **enhanced-100px**
- Consider **framed** or **badge** versions for emphasis

### For Social Media
- Use **standard-256px** or **detailed-256px** for profile pictures
- Use **badge** versions for professional appearance

### For Print Materials
- Use **ornate-256px** or **detailed-256px** for maximum detail
- Use **monochrome** versions for single-color printing

### For Watermarks
- Use **subtle-100px** with reduced opacity
- Use **monochrome** versions for subtle branding

## Technical Details

- **Format**: SVG (vector-based, scalable)
- **Colors**: 
  - Gold: #fbbf24
  - Emerald Dark: #0d4d3f
  - Emerald Accent: #10b981
- **Transparency**: All icons support transparent backgrounds
- **Optimization**: Clean paths, optimized for web and print

## Brand Alignment

All variations maintain:
- **Three horizontal elements** (core identity)
- **Angular/geometric aesthetic** (cutting-edge feel)
- **Volcanic/tectonic movement concept** (dynamic energy)
- **Premium, sophisticated appearance**

## Regenerating

To regenerate all variations:

```bash
python3 scripts/generate-icon-variations.py
```

## Total Assets

- **34+ SVG icon files** across all categories
- **1 Preview HTML** file with category organization
- **1 README** file (this document)
