# Letter to Claude: SVG Logo Generation Script Request

Dear Claude,

I hope this message finds you well. I'm working on a custom bike shop e-commerce website called "RIFT" and need your assistance in creating a script that can generate multiple SVG logo variations.

## Project Context

RIFT is a premium custom bike shop with the following brand identity:
- **Color Scheme**: Royal emerald green (#0d4d3f, #0f3d32, #065f46) and bright gold (#fbbf24)
- **Brand Concept**: "Rift" represents the edge of biking technology - sharp, dynamic, and cutting-edge
- **Visual Style**: Modern, clean, geometric, with a volcanic rift icon (three horizontal lines with angular cracks)

## Current Logo Structure

We currently have a volcanic rift icon (three horizontal gold lines with angular cracks) and need custom typography for "RIFT" that is:
- **Unique and distinctive** (not standard system fonts)
- **Highly legible** (readable at all sizes)
- **Geometric and modern** (reflecting the "rift" concept)
- **Simple yet dynamic** (clean lines with subtle angular accents)

## Request

I need a script (preferably in Python or JavaScript/Node.js) that can:

1. **Generate 20 unique SVG logo variations** with the following characteristics:
   - All logos should use the RIFT volcanic rift icon (provided as SVG code)
   - All logos should use custom geometric letterforms for "RIFT" text
   - All logos should use the brand colors (emerald green and gold)
   - All logos should have transparent backgrounds
   - Logos should vary in:
     - Layout (horizontal, vertical, stacked, icon-only, text-only)
     - Size and proportions
     - Typography weight and spacing
     - Accent elements (lines, borders, badges, etc.)

2. **Output Requirements**:
   - Each logo should be saved as a separate SVG file
   - File naming convention: `rift-logo-[descriptor].svg`
   - All SVGs should be valid and viewable in browsers
   - SVGs should be optimized (no unnecessary code)

3. **Logo Variations Needed**:
   - Horizontal layouts (icon + text side-by-side)
   - Vertical layouts (icon above text)
   - Stacked layouts (icon above text with tagline)
   - Icon-only versions
   - Text-only versions
   - Badge/circle badge versions
   - Compact versions (for small spaces)
   - Wide banner versions
   - Minimal versions
   - Watermark versions
   - And 10 more creative variations

4. **Technical Specifications**:
   - SVG viewBox should be appropriate for each logo size
   - All paths should use the brand colors
   - Typography should be custom geometric letterforms (not fonts)
   - Icons should be scalable and crisp at any size
   - Files should be production-ready

## Current Icon Reference

Here's the volcanic rift icon structure we're using:
```svg
<!-- Three horizontal lines -->
<path d="M10 30 L90 30" stroke="#fbbf24" stroke-width="3" stroke-linecap="square"/>
<path d="M15 60 L85 60" stroke="#fbbf24" stroke-width="3" stroke-linecap="square"/>
<path d="M20 90 L80 90" stroke="#fbbf24" stroke-width="3" stroke-linecap="square"/>

<!-- Angular cracks -->
<path d="M25 15 L28 30 M75 15 L72 30" stroke="#fbbf24" stroke-width="2.5" stroke-linecap="square"/>
<path d="M30 45 L33 60 M70 45 L67 60" stroke="#fbbf24" stroke-width="2.5" stroke-linecap="square"/>
<path d="M50 75 L53 90 M50 75 L47 90" stroke="#fbbf24" stroke-width="2.5" stroke-linecap="square"/>
```

## Typography Style

The "RIFT" text should be:
- Custom geometric letterforms (not standard fonts)
- Angular and sharp (reflecting "rift" concept)
- Bold and modern
- Highly legible
- Using white (#ffffff) or gold (#fbbf24) fill
- With optional subtle emerald green (#10b981) accent lines

## Deliverable

Please provide:
1. A complete script (Python or Node.js) that generates all 20 SVG files
2. Instructions on how to run the script
3. The script should be well-commented and easy to modify
4. Output should be saved to a specified directory (e.g., `output/logos/`)

## Use Case

These logos will be used for:
- Website branding
- Marketing materials (posters, flyers)
- Video overlays
- Social media
- Print materials

The script will allow us to quickly generate and iterate on logo designs, then implement them in our Next.js website.

Thank you for your assistance! I look forward to seeing what you create.

Best regards,
RIFT Development Team

---

## Additional Notes

- The script should be flexible enough to allow easy modification of colors, sizes, and layouts
- Consider including a configuration file or parameters for easy customization
- The generated SVGs should follow best practices (proper namespaces, clean code)
- If possible, include a preview HTML file that displays all generated logos
