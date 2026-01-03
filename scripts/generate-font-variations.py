#!/usr/bin/env python3
"""
RIFT Logo Font Variations Generator
Generates multiple logo variations with different typography styles
"""

import os
from typing import Dict, List, Tuple

# Brand Colors
COLORS = {
    'emerald_dark': '#0d4d3f',
    'emerald_mid': '#0f3d32',
    'emerald_bright': '#065f46',
    'emerald_accent': '#10b981',
    'gold': '#fbbf24',
    'white': '#ffffff',
    'black': '#000000'
}

# Font configurations with Google Fonts
# Organized by category: Sans-Serif, Serif, Display, Script, Monospace

FONT_VARIATIONS = [
    # ===== SANS-SERIF (Modern & Clean) =====
    {
        'name': 'inter',
        'family': 'Inter',
        'style': 'Modern & Clean',
        'category': 'Sans-Serif',
        'weight': '700',
        'google_font': 'Inter:wght@300;400;700;900',
        'letter_spacing': '0.05em'
    },
    {
        'name': 'montserrat',
        'family': 'Montserrat',
        'style': 'Elegant & Premium',
        'category': 'Sans-Serif',
        'weight': '700',
        'google_font': 'Montserrat:wght@300;400;700;900',
        'letter_spacing': '0.08em'
    },
    {
        'name': 'poppins',
        'family': 'Poppins',
        'style': 'Friendly Modern',
        'category': 'Sans-Serif',
        'weight': '700',
        'google_font': 'Poppins:wght@300;400;700;900',
        'letter_spacing': '0.05em'
    },
    {
        'name': 'space-grotesk',
        'family': 'Space Grotesk',
        'style': 'Tech-Forward',
        'category': 'Sans-Serif',
        'weight': '700',
        'google_font': 'Space+Grotesk:wght@300;400;700',
        'letter_spacing': '0.1em'
    },
    {
        'name': 'work-sans',
        'family': 'Work Sans',
        'style': 'Professional & Clean',
        'category': 'Sans-Serif',
        'weight': '700',
        'google_font': 'Work+Sans:wght@300;400;600;700',
        'letter_spacing': '0.06em'
    },
    {
        'name': 'dm-sans',
        'family': 'DM Sans',
        'style': 'Modern & Versatile',
        'category': 'Sans-Serif',
        'weight': '700',
        'google_font': 'DM+Sans:wght@400;700',
        'letter_spacing': '0.05em'
    },
    {
        'name': 'outfit',
        'family': 'Outfit',
        'style': 'Contemporary & Premium',
        'category': 'Sans-Serif',
        'weight': '700',
        'google_font': 'Outfit:wght@300;400;700;900',
        'letter_spacing': '0.08em'
    },
    {
        'name': 'plus-jakarta-sans',
        'family': 'Plus Jakarta Sans',
        'style': 'Modern & Friendly',
        'category': 'Sans-Serif',
        'weight': '700',
        'google_font': 'Plus+Jakarta+Sans:wght@400;600;700',
        'letter_spacing': '0.05em'
    },
    {
        'name': 'manrope',
        'family': 'Manrope',
        'style': 'Geometric & Balanced',
        'category': 'Sans-Serif',
        'weight': '700',
        'google_font': 'Manrope:wght@300;400;700;800',
        'letter_spacing': '0.06em'
    },
    {
        'name': 'sora',
        'family': 'Sora',
        'style': 'Clean & Professional',
        'category': 'Sans-Serif',
        'weight': '700',
        'google_font': 'Sora:wght@300;400;600;700',
        'letter_spacing': '0.05em'
    },
    {
        'name': 'epilogue',
        'family': 'Epilogue',
        'style': 'Modern & Readable',
        'category': 'Sans-Serif',
        'weight': '700',
        'google_font': 'Epilogue:wght@400;600;700;900',
        'letter_spacing': '0.06em'
    },
    {
        'name': 'nunito-sans',
        'family': 'Nunito Sans',
        'style': 'Friendly & Rounded',
        'category': 'Sans-Serif',
        'weight': '700',
        'google_font': 'Nunito+Sans:wght@300;400;700;900',
        'letter_spacing': '0.05em'
    },
    
    # ===== SERIF (Elegant & Premium) =====
    {
        'name': 'playfair',
        'family': 'Playfair Display',
        'style': 'Luxury Serif',
        'category': 'Serif',
        'weight': '700',
        'google_font': 'Playfair+Display:wght@400;700;900',
        'letter_spacing': '0.03em'
    },
    {
        'name': 'cormorant',
        'family': 'Cormorant Garamond',
        'style': 'Classic Refined',
        'category': 'Serif',
        'weight': '700',
        'google_font': 'Cormorant+Garamond:wght@300;400;700',
        'letter_spacing': '0.05em'
    },
    {
        'name': 'lora',
        'family': 'Lora',
        'style': 'Warm & Approachable',
        'category': 'Serif',
        'weight': '700',
        'google_font': 'Lora:wght@400;700',
        'letter_spacing': '0.04em'
    },
    {
        'name': 'merriweather',
        'family': 'Merriweather',
        'style': 'Professional & Legible',
        'category': 'Serif',
        'weight': '700',
        'google_font': 'Merriweather:wght@300;400;700;900',
        'letter_spacing': '0.03em'
    },
    {
        'name': 'libre-baskerville',
        'family': 'Libre Baskerville',
        'style': 'Classic & Timeless',
        'category': 'Serif',
        'weight': '700',
        'google_font': 'Libre+Baskerville:wght@400;700',
        'letter_spacing': '0.04em'
    },
    {
        'name': 'crimson-text',
        'family': 'Crimson Text',
        'style': 'Elegant & Traditional',
        'category': 'Serif',
        'weight': '600',
        'google_font': 'Crimson+Text:wght@400;600;700',
        'letter_spacing': '0.03em'
    },
    {
        'name': 'cinzel',
        'family': 'Cinzel',
        'style': 'Classical & Elegant',
        'category': 'Serif',
        'weight': '700',
        'google_font': 'Cinzel:wght@400;600;700',
        'letter_spacing': '0.08em'
    },
    {
        'name': 'spectral',
        'family': 'Spectral',
        'style': 'Refined & Sophisticated',
        'category': 'Serif',
        'weight': '700',
        'google_font': 'Spectral:wght@300;400;600;700',
        'letter_spacing': '0.04em'
    },
    
    # ===== DISPLAY/DECORATIVE (Bold & Expressive) =====
    {
        'name': 'bebas-neue',
        'family': 'Bebas Neue',
        'style': 'Bold Condensed',
        'category': 'Display',
        'weight': '400',
        'google_font': 'Bebas+Neue',
        'letter_spacing': '0.15em'
    },
    {
        'name': 'oswald',
        'family': 'Oswald',
        'style': 'Strong Modern',
        'category': 'Display',
        'weight': '600',
        'google_font': 'Oswald:wght@300;400;600;700',
        'letter_spacing': '0.12em'
    },
    {
        'name': 'righteous',
        'family': 'Righteous',
        'style': 'Bold Dynamic',
        'category': 'Display',
        'weight': '400',
        'google_font': 'Righteous',
        'letter_spacing': '0.08em'
    },
    {
        'name': 'russo-one',
        'family': 'Russo One',
        'style': 'Tech Bold',
        'category': 'Display',
        'weight': '400',
        'google_font': 'Russo+One',
        'letter_spacing': '0.1em'
    },
    {
        'name': 'orbitron',
        'family': 'Orbitron',
        'style': 'Futuristic',
        'category': 'Display',
        'weight': '700',
        'google_font': 'Orbitron:wght@400;700;900',
        'letter_spacing': '0.1em'
    },
    {
        'name': 'rajdhani',
        'family': 'Rajdhani',
        'style': 'Geometric Clean',
        'category': 'Display',
        'weight': '700',
        'google_font': 'Rajdhani:wght@300;400;600;700',
        'letter_spacing': '0.1em'
    },
    {
        'name': 'abril-fatface',
        'family': 'Abril Fatface',
        'style': 'Bold & Elegant',
        'category': 'Display',
        'weight': '400',
        'google_font': 'Abril+Fatface',
        'letter_spacing': '0.05em'
    },
    {
        'name': 'anton',
        'family': 'Anton',
        'style': 'Strong & Condensed',
        'category': 'Display',
        'weight': '400',
        'google_font': 'Anton',
        'letter_spacing': '0.1em'
    },
    {
        'name': 'black-ops-one',
        'family': 'Black Ops One',
        'style': 'Bold Military-Style',
        'category': 'Display',
        'weight': '400',
        'google_font': 'Black+Ops+One',
        'letter_spacing': '0.12em'
    },
    {
        'name': 'exo-2',
        'family': 'Exo 2',
        'style': 'Futuristic & Tech',
        'category': 'Display',
        'weight': '700',
        'google_font': 'Exo+2:wght@300;400;600;700;900',
        'letter_spacing': '0.1em'
    },
    {
        'name': 'kanit',
        'family': 'Kanit',
        'style': 'Modern & Geometric',
        'category': 'Display',
        'weight': '700',
        'google_font': 'Kanit:wght@300;400;600;700;900',
        'letter_spacing': '0.08em'
    },
    {
        'name': 'raleway',
        'family': 'Raleway',
        'style': 'Elegant & Versatile',
        'category': 'Display',
        'weight': '700',
        'google_font': 'Raleway:wght@300;400;600;700;900',
        'letter_spacing': '0.1em'
    },
    {
        'name': 'titillium-web',
        'family': 'Titillium Web',
        'style': 'Modern & Clean',
        'category': 'Display',
        'weight': '700',
        'google_font': 'Titillium+Web:wght@300;400;600;700;900',
        'letter_spacing': '0.08em'
    },
    {
        'name': 'ubuntu',
        'family': 'Ubuntu',
        'style': 'Friendly & Professional',
        'category': 'Display',
        'weight': '700',
        'google_font': 'Ubuntu:wght@300;400;700',
        'letter_spacing': '0.06em'
    },
    
    # ===== SCRIPT/HANDWRITTEN (Premium & Crafted) =====
    {
        'name': 'dancing-script',
        'family': 'Dancing Script',
        'style': 'Elegant & Flowing',
        'category': 'Script',
        'weight': '700',
        'google_font': 'Dancing+Script:wght@400;700',
        'letter_spacing': '0.05em'
    },
    {
        'name': 'great-vibes',
        'family': 'Great Vibes',
        'style': 'Sophisticated & Elegant',
        'category': 'Script',
        'weight': '400',
        'google_font': 'Great+Vibes',
        'letter_spacing': '0.08em'
    },
    {
        'name': 'pacifico',
        'family': 'Pacifico',
        'style': 'Friendly & Rounded',
        'category': 'Script',
        'weight': '400',
        'google_font': 'Pacifico',
        'letter_spacing': '0.05em'
    },
    {
        'name': 'satisfy',
        'family': 'Satisfy',
        'style': 'Casual Elegance',
        'category': 'Script',
        'weight': '400',
        'google_font': 'Satisfy',
        'letter_spacing': '0.06em'
    },
    
    # ===== MONOSPACE (Tech & Precision) =====
    {
        'name': 'jetbrains-mono',
        'family': 'JetBrains Mono',
        'style': 'Modern & Tech-Forward',
        'category': 'Monospace',
        'weight': '700',
        'google_font': 'JetBrains+Mono:wght@400;700',
        'letter_spacing': '0.1em'
    },
    {
        'name': 'fira-code',
        'family': 'Fira Code',
        'style': 'Professional & Readable',
        'category': 'Monospace',
        'weight': '700',
        'google_font': 'Fira+Code:wght@400;700',
        'letter_spacing': '0.12em'
    },
    {
        'name': 'source-code-pro',
        'family': 'Source Code Pro',
        'style': 'Clean & Technical',
        'category': 'Monospace',
        'weight': '700',
        'google_font': 'Source+Code+Pro:wght@400;700;900',
        'letter_spacing': '0.1em'
    },
]


class RIFTFontVariationGenerator:
    """Generates logo variations with different fonts"""
    
    def __init__(self, output_dir: str = 'output/font-variations'):
        self.output_dir = output_dir
        self.ensure_output_dir()
    
    def ensure_output_dir(self):
        """Create output directory if it doesn't exist"""
        os.makedirs(self.output_dir, exist_ok=True)
    
    def get_rift_icon(self, x: float, y: float, scale: float = 1.0, 
                     color: str = COLORS['gold'], stroke_width: float = None) -> str:
        """Generate the volcanic rift icon SVG paths"""
        s = scale
        sw = stroke_width if stroke_width is not None else (3 * scale)
        sw_cracks = (sw * 0.83) if stroke_width else (2.5 * scale)
        
        return f'''
        <!-- Volcanic Rift Icon -->
        <g transform="translate({x}, {y}) scale({s})">
            <!-- Horizontal lines -->
            <path d="M10 30 L90 30" stroke="{color}" stroke-width="{sw}" stroke-linecap="square"/>
            <path d="M15 60 L85 60" stroke="{color}" stroke-width="{sw}" stroke-linecap="square"/>
            <path d="M20 90 L80 90" stroke="{color}" stroke-width="{sw}" stroke-linecap="square"/>
            <!-- Angular cracks -->
            <path d="M25 15 L28 30 M75 15 L72 30" stroke="{color}" stroke-width="{sw_cracks}" stroke-linecap="square"/>
            <path d="M30 45 L33 60 M70 45 L67 60" stroke="{color}" stroke-width="{sw_cracks}" stroke-linecap="square"/>
            <path d="M50 75 L53 90 M50 75 L47 90" stroke="{color}" stroke-width="{sw_cracks}" stroke-linecap="square"/>
        </g>
        '''
    
    def get_rift_text(self, x: float, y: float, size: float, font_config: Dict, 
                     color: str = COLORS['white']) -> str:
        """Generate RIFT text using specified font"""
        return f'''
        <text x="{x}" y="{y}" 
              font-family="{font_config['family']}, sans-serif" 
              font-size="{size}" 
              font-weight="{font_config['weight']}"
              fill="{color}" 
              text-anchor="middle"
              letter-spacing="{font_config['letter_spacing']}">
            RIFT
        </text>
        '''
    
    def create_svg(self, width: int, height: int, content: str, 
                  viewbox: str = None, background: str = None,
                  fonts: List[str] = None) -> str:
        """Wrap content in SVG tags with font imports"""
        if viewbox is None:
            viewbox = f"0 0 {width} {height}"
        
        bg = f'<rect width="{width}" height="{height}" fill="{background}"/>' if background else ''
        
        # Build font imports (using CDATA to avoid XML parsing issues)
        font_imports = ''
        if fonts:
            font_urls = '|'.join(fonts)
            font_imports = f'''
    <defs>
        <style type="text/css"><![CDATA[
            @import url('https://fonts.googleapis.com/css2?family={font_urls}&display=swap');
        ]]></style>
    </defs>'''
        
        return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}" width="{width}" height="{height}">
    {font_imports}
    {bg}
    {content}
</svg>'''
    
    def save_logo(self, filename: str, svg_content: str):
        """Save SVG content to file"""
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"✓ Generated: {filename}")
    
    def generate_horizontal_logo(self, font_config: Dict):
        """Generate horizontal logo with specific font"""
        filename = f"rift-logo-horizontal-{font_config['name']}.svg"
        
        # Calculate text position (centered after icon)
        icon_width = 100
        icon_x = 20
        icon_y = 40
        text_x = 200  # Center of remaining space
        text_y = 70
        text_size = 56
        
        content = f'''
        {self.get_rift_icon(icon_x, icon_y, 1.0, COLORS['gold'])}
        {self.get_rift_text(text_x, text_y, text_size, font_config, COLORS['white'])}
        '''
        
        svg = self.create_svg(
            width=400, 
            height=120, 
            content=content,
            background=COLORS['emerald_dark'],
            fonts=[font_config['google_font']]
        )
        
        self.save_logo(filename, svg)
    
    def generate_vertical_logo(self, font_config: Dict):
        """Generate vertical logo with specific font"""
        filename = f"rift-logo-vertical-{font_config['name']}.svg"
        
        icon_x = 100
        icon_y = 30
        text_x = 150
        text_y = 200
        text_size = 50
        
        content = f'''
        {self.get_rift_icon(icon_x, icon_y, 1.0, COLORS['gold'])}
        {self.get_rift_text(text_x, text_y, text_size, font_config, COLORS['white'])}
        '''
        
        svg = self.create_svg(
            width=300, 
            height=400, 
            content=content,
            background=COLORS['emerald_dark'],
            fonts=[font_config['google_font']]
        )
        
        self.save_logo(filename, svg)
    
    def generate_text_only_logo(self, font_config: Dict):
        """Generate text-only logo with specific font"""
        filename = f"rift-logo-text-only-{font_config['name']}.svg"
        
        text_x = 200
        text_y = 80
        text_size = 70
        
        content = self.get_rift_text(text_x, text_y, text_size, font_config, COLORS['gold'])
        
        svg = self.create_svg(
            width=400, 
            height=150, 
            content=content,
            background=COLORS['emerald_dark'],
            fonts=[font_config['google_font']]
        )
        
        self.save_logo(filename, svg)
    
    def generate_compact_logo(self, font_config: Dict):
        """Generate compact logo with specific font"""
        filename = f"rift-logo-compact-{font_config['name']}.svg"
        
        icon_x = 10
        icon_y = 15
        text_x = 120
        text_y = 40
        text_size = 32
        
        content = f'''
        {self.get_rift_icon(icon_x, icon_y, 0.5, COLORS['gold'])}
        {self.get_rift_text(text_x, text_y, text_size, font_config, COLORS['white'])}
        '''
        
        svg = self.create_svg(
            width=180, 
            height=60, 
            content=content,
            background=COLORS['emerald_dark'],
            fonts=[font_config['google_font']]
        )
        
        self.save_logo(filename, svg)
    
    def generate_all_variations(self):
        """Generate all font variations"""
        print("\n" + "="*60)
        print("🎨 RIFT Font Variations Generator")
        print("="*60)
        print(f"📁 Output directory: {self.output_dir}\n")
        
        total = 0
        for font_config in FONT_VARIATIONS:
            print(f"\n📝 Generating {font_config['family']} ({font_config['style']})...")
            self.generate_horizontal_logo(font_config)
            self.generate_vertical_logo(font_config)
            self.generate_text_only_logo(font_config)
            self.generate_compact_logo(font_config)
            total += 4
        
        # Generate preview HTML
        self.generate_preview_html()
        
        print("\n" + "="*60)
        print(f"✅ Generated {total} logo variations with {len(FONT_VARIATIONS)} fonts!")
        print(f"📁 Files saved to: {self.output_dir}/")
        print(f"🌐 Preview: {os.path.join(self.output_dir, 'preview.html')}")
        print("="*60)
    
    def generate_preview_html(self):
        """Generate HTML preview of all font variations grouped by category"""
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RIFT Font Variations Preview</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Inter', Arial, sans-serif;
            background: #1a1a1a;
            color: #ffffff;
            padding: 40px 20px;
        }
        h1 {
            text-align: center;
            color: #fbbf24;
            font-size: 3em;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            color: #10b981;
            margin-bottom: 20px;
            font-size: 1.2em;
        }
        .stats {
            text-align: center;
            color: #aaa;
            margin-bottom: 50px;
            font-size: 1em;
        }
        .category-section {
            margin-bottom: 80px;
        }
        .category-title {
            color: #fbbf24;
            font-size: 2.5em;
            margin-bottom: 15px;
            padding-bottom: 15px;
            border-bottom: 3px solid #0d4d3f;
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }
        .font-section {
            margin-bottom: 60px;
        }
        .font-title {
            color: #fbbf24;
            font-size: 2em;
            margin-bottom: 10px;
            padding-bottom: 10px;
            border-bottom: 2px solid #0d4d3f;
        }
        .font-style {
            color: #10b981;
            font-size: 1.1em;
            margin-bottom: 20px;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            max-width: 1600px;
            margin: 0 auto 40px;
        }
        .logo-card {
            background: #2a2a2a;
            border: 2px solid #0d4d3f;
            border-radius: 12px;
            padding: 20px;
            transition: transform 0.3s, border-color 0.3s;
        }
        .logo-card:hover {
            transform: translateY(-5px);
            border-color: #fbbf24;
        }
        .logo-container {
            background: white;
            border-radius: 8px;
            padding: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 150px;
            margin-bottom: 15px;
            overflow: hidden;
        }
        .logo-container img {
            max-width: 100%;
            max-height: 200px;
            height: auto;
        }
        .logo-name {
            color: #fbbf24;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .logo-type {
            color: #aaa;
            font-size: 0.9em;
        }
        .nav {
            position: fixed;
            top: 20px;
            right: 20px;
            background: #2a2a2a;
            border: 2px solid #0d4d3f;
            border-radius: 8px;
            padding: 15px;
            z-index: 1000;
        }
        .nav a {
            display: block;
            color: #10b981;
            text-decoration: none;
            padding: 5px 0;
            font-size: 0.9em;
        }
        .nav a:hover {
            color: #fbbf24;
        }
    </style>
</head>
<body>
    <h1>RIFT FONT VARIATIONS</h1>
    <p class="subtitle">Explore Different Typography Styles for Your Brand</p>
    <p class="stats">''' + f"{len(FONT_VARIATIONS)} fonts × 4 variations = {len(FONT_VARIATIONS) * 4} total logo files" + '''</p>
    
    <div class="nav">
        <strong style="color: #fbbf24; display: block; margin-bottom: 10px;">Categories</strong>
        <a href="#sans-serif">Sans-Serif</a>
        <a href="#serif">Serif</a>
        <a href="#display">Display</a>
        <a href="#script">Script</a>
        <a href="#monospace">Monospace</a>
    </div>
'''
        
        # Group fonts by category
        categories = {}
        for font_config in FONT_VARIATIONS:
            category = font_config.get('category', 'Other')
            if category not in categories:
                categories[category] = []
            categories[category].append(font_config)
        
        # Category display order
        category_order = ['Sans-Serif', 'Serif', 'Display', 'Script', 'Monospace']
        category_ids = {
            'Sans-Serif': 'sans-serif',
            'Serif': 'serif',
            'Display': 'display',
            'Script': 'script',
            'Monospace': 'monospace'
        }
        
        for category in category_order:
            if category not in categories:
                continue
                
            html += f'''
    <div class="category-section" id="{category_ids[category]}">
        <h2 class="category-title">{category}</h2>
'''
            
            for font_config in categories[category]:
                html += f'''
        <div class="font-section">
            <h3 class="font-title">{font_config['family']}</h3>
            <p class="font-style">{font_config['style']}</p>
            <div class="grid">
                <div class="logo-card">
                    <div class="logo-container">
                        <img src="rift-logo-horizontal-{font_config['name']}.svg" alt="Horizontal {font_config['family']}">
                    </div>
                    <div class="logo-name">Horizontal</div>
                    <div class="logo-type">400×120px</div>
                </div>
                <div class="logo-card">
                    <div class="logo-container">
                        <img src="rift-logo-vertical-{font_config['name']}.svg" alt="Vertical {font_config['family']}">
                    </div>
                    <div class="logo-name">Vertical</div>
                    <div class="logo-type">300×400px</div>
                </div>
                <div class="logo-card">
                    <div class="logo-container">
                        <img src="rift-logo-text-only-{font_config['name']}.svg" alt="Text Only {font_config['family']}">
                    </div>
                    <div class="logo-name">Text Only</div>
                    <div class="logo-type">400×150px</div>
                </div>
                <div class="logo-card">
                    <div class="logo-container">
                        <img src="rift-logo-compact-{font_config['name']}.svg" alt="Compact {font_config['family']}">
                    </div>
                    <div class="logo-name">Compact</div>
                    <div class="logo-type">180×60px</div>
                </div>
            </div>
        </div>
'''
            
            html += '''
    </div>
'''
        
        html += '''
</body>
</html>'''
        
        preview_path = os.path.join(self.output_dir, 'preview.html')
        with open(preview_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✓ Generated: preview.html")


def main():
    """Main execution function"""
    generator = RIFTFontVariationGenerator(output_dir='output/font-variations')
    generator.generate_all_variations()


if __name__ == '__main__':
    main()
