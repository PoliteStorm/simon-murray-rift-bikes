#!/bin/bash
# Final script to download official brand logos
# Uses multiple sources and methods

LOGOS_DIR="../public/logos/partners"
mkdir -p "$LOGOS_DIR"
cd "$LOGOS_DIR"

echo "🎨 Downloading Official Brand Logos"
echo "===================================="

# Method 1: Try Simple Icons (GitHub) - these are standardized brand icons
echo ""
echo "Method 1: Simple Icons (GitHub)"
echo "--------------------------------"

download_from_github() {
    local brand=$1
    local url="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/${brand}.svg"
    echo "  Downloading ${brand}..."
    curl -L -f -s "$url" -o "${brand}.svg" 2>/dev/null
    if [ -f "${brand}.svg" ] && [ -s "${brand}.svg" ] && head -1 "${brand}.svg" | grep -q "<svg"; then
        echo "  ✓ ${brand}.svg downloaded"
        return 0
    else
        rm -f "${brand}.svg"
        echo "  ✗ ${brand} failed"
        return 1
    fi
}

# Try downloading from Simple Icons
download_from_github "shimano" || true
download_from_github "sram" || true  
download_from_github "campagnolo" || true
download_from_github "maxxis" || true

echo ""
echo "Method 2: Direct Brand Website URLs"
echo "-----------------------------------"
echo "  Note: Many brands require manual download from their official websites"
echo "  See OFFICIAL-LOGOS-REQUIRED.md for instructions"

echo ""
echo "Summary:"
echo "========"
ls -lh *.svg 2>/dev/null | awk '{print "  " $9 " (" $5 ")"}'

echo ""
echo "✅ Download complete!"
echo ""
echo "📋 Next Steps:"
echo "  1. Verify downloaded logos are correct"
echo "  2. For missing logos, download manually from brand websites"
echo "  3. Replace any custom-made logos with official versions"
