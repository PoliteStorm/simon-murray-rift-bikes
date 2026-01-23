#!/usr/bin/env python3
"""
Download official brand logos from reliable sources
"""

import os
import requests
from pathlib import Path

LOGOS_DIR = Path(__file__).parent.parent / "public" / "logos" / "partners"
LOGOS_DIR.mkdir(parents=True, exist_ok=True)

# Official logo sources (publicly available)
LOGO_SOURCES = {
    'shimano': [
        'https://upload.wikimedia.org/wikipedia/commons/8/8a/Shimano_logo.svg',
        'https://www.shimano.com/content/dam/shimano/shimano-site-assets/images/logo/shimano-logo.svg',
    ],
    # Add more as we find reliable sources
}

def download_logo(name, urls):
    """Try to download logo from multiple sources"""
    for url in urls:
        try:
            print(f"  Trying: {url[:60]}...")
            response = requests.get(url, timeout=10, allow_redirects=True)
            if response.status_code == 200:
                # Check if it's actually SVG content
                content = response.text
                if 'svg' in response.headers.get('content-type', '').lower() or content.strip().startswith('<svg'):
                    filepath = LOGOS_DIR / f"{name}.svg"
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"  ✓ Downloaded {name}.svg ({len(content)} bytes)")
                    return True
        except Exception as e:
            print(f"  ✗ Failed: {str(e)[:50]}")
            continue
    return False

def main():
    print("🎨 Downloading Official Brand Logos")
    print("=" * 50)
    print(f"Output directory: {LOGOS_DIR}\n")
    
    success_count = 0
    for name, urls in LOGO_SOURCES.items():
        print(f"Downloading {name.upper()}...")
        if download_logo(name, urls):
            success_count += 1
        print()
    
    print("=" * 50)
    print(f"✅ Downloaded {success_count}/{len(LOGO_SOURCES)} logos")
    print("\n📋 For other brands, please:")
    print("   1. Visit official brand websites")
    print("   2. Check Media/Press/Brand Assets sections")
    print("   3. Download SVG files manually")
    print(f"   4. Save to: {LOGOS_DIR}/")
    print("\nSee scripts/download-logos-manual.md for detailed instructions")

if __name__ == '__main__':
    main()
