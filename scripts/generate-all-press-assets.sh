#!/bin/bash
# Master script to generate all press package assets

echo "🎨 RIFT Press Package - Complete Generation"
echo "=========================================="
echo ""

# Generate basic press package
echo "📦 Generating Basic Press Package..."
python3 scripts/generate-press-package.py

echo ""
echo "🚀 Generating Advanced Designs..."
python3 scripts/generate-press-package-advanced.py

echo ""
echo "📢 Generating Extended Variations..."
python3 scripts/generate-press-package-extended.py

echo ""
echo "✅ All press package assets generated!"
echo "📁 Check output/press-package/ for all assets"
echo ""
echo "📋 Generated Assets Summary:"
echo "  • Enhanced logos with bike/cog rift elements"
echo "  • Social media banners (Twitter, Facebook, Instagram)"
echo "  • Ad designs with multiple slogan variations"
echo "  • Video overlays and frame templates"
echo "  • Instagram carousel templates"
echo "  • Wide banner variations"
