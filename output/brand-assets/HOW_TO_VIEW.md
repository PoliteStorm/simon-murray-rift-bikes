# How to View Your RIFT Brand Assets

## ✅ Quick Start (Easiest Method)

**A web server is already running!** Open your browser and go to:

### 🌐 http://localhost:8000/index.html

This will show a simple test page to verify all SVGs are working.

### 🌐 http://localhost:8000/preview.html

This shows the full gallery of all assets.

---

## If the Server Isn't Running

### Step 1: Start the Server

Open a terminal and run:

```bash
cd /home/tau/RIFT/output/brand-assets
python3 -m http.server 8000
```

### Step 2: Open in Browser

Then open:
- **http://localhost:8000/index.html** (simple test)
- **http://localhost:8000/preview.html** (full gallery)

---

## Why You Need a Server

Modern browsers **block** loading local files (file:// protocol) for security. You MUST use a web server (http://) to view the HTML preview with images.

---

## Alternative: View SVG Files Directly

You can open any `.svg` file directly:

1. **Double-click** any `.svg` file in your file manager
2. It will open in your default image viewer or browser
3. Works for individual files, but not for the HTML preview

---

## Test Individual Files

Try opening these directly (double-click):
- `logos/icon-only/rift-logo-icon-only.svg`
- `logos/horizontal/rift-logo-horizontal-standard.svg`

If these open and show the logo, the files are working correctly!

---

## Troubleshooting

### "No images appear"
- ✅ Make sure you're using **http://localhost:8000** (not file://)
- ✅ Check the server is running: `ps aux | grep http.server`
- ✅ Try the test page: http://localhost:8000/test-direct.html

### "SVG files won't open"
- ✅ Try opening directly (double-click)
- ✅ Check file permissions: `ls -l logos/icon-only/`
- ✅ Verify file exists: `cat logos/icon-only/rift-logo-icon-only.svg`

### "Server won't start"
- ✅ Check if port 8000 is in use: `lsof -i :8000`
- ✅ Try a different port: `python3 -m http.server 8001`

---

## File Structure

```
output/brand-assets/
├── index.html          ← Simple test page
├── preview.html        ← Full gallery
├── test-direct.html    ← Direct SVG test
├── logos/              ← Primary logos
├── social-media/       ← Social media assets
├── banners/            ← Banners & headers
├── overlays/           ← Video overlays
└── specialized/        ← Favicons, app icons, etc.
```

---

## Verification

All SVG files have been validated:
- ✅ Valid XML structure
- ✅ Proper SVG namespace
- ✅ Correct viewBox attributes
- ✅ Files are accessible via HTTP

If you still see issues, the problem is likely:
1. Browser security (must use http:// not file://)
2. Server not running
3. Wrong URL/path

---

## Need Help?

1. Check server is running: `curl http://localhost:8000/logos/icon-only/rift-logo-icon-only.svg`
2. Check browser console (F12) for errors
3. Try the test page: http://localhost:8000/test-direct.html
