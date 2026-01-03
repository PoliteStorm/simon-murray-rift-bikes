# How to View Your Brand Assets

## Quick Start

A local web server is running! Open your browser and go to:

**http://localhost:8000/preview.html**

This will show all your brand assets in an interactive gallery.

## If the Server Isn't Running

If you need to start the server manually:

```bash
cd output/brand-assets
python3 -m http.server 8000
```

Then open: **http://localhost:8000/preview.html**

## Why Use a Server?

Modern browsers block loading local files (file:// protocol) for security reasons. Using a local HTTP server allows the SVG images to load properly in the HTML preview.

## Direct SVG Access

You can also view individual SVG files directly:
- http://localhost:8000/logos/horizontal/rift-logo-horizontal-standard.svg
- http://localhost:8000/logos/icon-only/rift-logo-icon-only.svg
- etc.

## Alternative: Open SVG Files Directly

SVG files can be opened directly in:
- Web browsers (Chrome, Firefox, Safari, Edge)
- Image viewers that support SVG
- Design software (Illustrator, Inkscape, etc.)

Just double-click any `.svg` file to open it.

## File Locations

All assets are in: `output/brand-assets/`

- Logos: `logos/` subdirectories
- Social Media: `social-media/`
- Banners: `banners/`
- Overlays: `overlays/`
- Specialized: `specialized/`
