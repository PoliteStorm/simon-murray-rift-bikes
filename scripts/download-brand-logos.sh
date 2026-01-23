#!/bin/bash
# Script to download official brand logos from public sources
# Note: Always verify you have permission to use these logos

LOGOS_DIR="../public/logos/partners"
mkdir -p "$LOGOS_DIR"

echo "🎨 Downloading Official Brand Logos..."
echo "======================================"

# Shimano - from Wikimedia Commons
echo "Downloading Shimano logo..."
curl -L "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Shimano_logo.svg/512px-Shimano_logo.svg" \
  -o "$LOGOS_DIR/shimano-official.svg" 2>/dev/null && echo "✓ Shimano downloaded" || echo "⚠️  Shimano download failed"

# Try alternative sources for other brands
echo ""
echo "📋 Note: Some logos may need manual download from official brand websites"
echo ""

# Check what we got
if [ -f "$LOGOS_DIR/shimano-official.svg" ]; then
  echo "✅ Successfully downloaded logos!"
  ls -lh "$LOGOS_DIR"/*.svg 2>/dev/null | head -5
else
  echo "⚠️  Automatic downloads may have failed. Please use manual method below."
fi

echo ""
echo "📝 Manual Download Guide:"
echo "========================"
echo "1. Visit brand official websites"
echo "2. Look for Media/Press/Brand Assets sections"
echo "3. Download SVG or high-res PNG files"
echo "4. Save to: $LOGOS_DIR/"
