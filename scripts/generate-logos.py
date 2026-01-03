#!/usr/bin/env python3
"""
RIFT Logo Generator
Generates 20 unique SVG logo variations for RIFT custom bike shop
Author: Claude AI
License: MIT
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

class RIFTLogoGenerator:
    """Generates RIFT logo variations in SVG format"""
    
    def __init__(self, output_dir: str = 'output/logos'):
        self.output_dir = output_dir
        self.ensure_output_dir()
    
    def ensure_output_dir(self):
        """Create output directory if it doesn't exist"""
        os.makedirs(self.output_dir, exist_ok=True)
    
    def get_rift_icon(self, x: float, y: float, scale: float = 1.0, color: str = COLORS['gold']) -> str:
        """Generate the volcanic rift icon SVG paths"""
        s = scale
        return f'''
        <!-- Volcanic Rift Icon -->
        <g transform="translate({x}, {y}) scale({s})">
            <!-- Horizontal lines -->
            <path d="M10 30 L90 30" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <path d="M15 60 L85 60" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <path d="M20 90 L80 90" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <!-- Angular cracks -->
            <path d="M25 15 L28 30 M75 15 L72 30" stroke="{color}" stroke-width="2.5" stroke-linecap="square"/>
            <path d="M30 45 L33 60 M70 45 L67 60" stroke="{color}" stroke-width="2.5" stroke-linecap="square"/>
            <path d="M50 75 L53 90 M50 75 L47 90" stroke="{color}" stroke-width="2.5" stroke-linecap="square"/>
        </g>
        '''
    
    def get_rift_text_geometric(self, x: float, y: float, size: float = 60, 
                                color: str = COLORS['white'], weight: str = 'bold') -> str:
        """Generate custom geometric RIFT letterforms as SVG paths"""
        scale = size / 60  # Base size is 60
        stroke_width = 8 if weight == 'bold' else 6
        
        # Custom geometric letterforms for R-I-F-T
        # R: Vertical line + angled top + diagonal leg
        r_path = f'''
            M {x + 0*scale} {y + 60*scale} L {x + 0*scale} {y + 0*scale}
            L {x + 25*scale} {y + 0*scale} L {x + 30*scale} {y + 15*scale}
            L {x + 25*scale} {y + 30*scale} L {x + 0*scale} {y + 30*scale}
            M {x + 12*scale} {y + 30*scale} L {x + 30*scale} {y + 60*scale}
        '''
        
        # I: Simple vertical line with top and bottom caps
        i_path = f'''
            M {x + 50*scale} {y + 0*scale} L {x + 50*scale} {y + 60*scale}
            M {x + 40*scale} {y + 0*scale} L {x + 60*scale} {y + 0*scale}
            M {x + 40*scale} {y + 60*scale} L {x + 60*scale} {y + 60*scale}
        '''
        
        # F: Vertical line + two horizontal lines (top and middle)
        f_path = f'''
            M {x + 80*scale} {y + 60*scale} L {x + 80*scale} {y + 0*scale}
            L {x + 110*scale} {y + 0*scale}
            M {x + 80*scale} {y + 28*scale} L {x + 105*scale} {y + 28*scale}
        '''
        
        # T: Horizontal top + vertical center
        t_path = f'''
            M {x + 125*scale} {y + 0*scale} L {x + 165*scale} {y + 0*scale}
            M {x + 145*scale} {y + 0*scale} L {x + 145*scale} {y + 60*scale}
        '''
        
        return f'''
        <g>
            <path d="{r_path}" stroke="{color}" stroke-width="{stroke_width*scale}" 
                  fill="none" stroke-linecap="square" stroke-linejoin="miter"/>
            <path d="{i_path}" stroke="{color}" stroke-width="{stroke_width*scale}" 
                  fill="none" stroke-linecap="square"/>
            <path d="{f_path}" stroke="{color}" stroke-width="{stroke_width*scale}" 
                  fill="none" stroke-linecap="square"/>
            <path d="{t_path}" stroke="{color}" stroke-width="{stroke_width*scale}" 
                  fill="none" stroke-linecap="square"/>
        </g>
        '''
    
    def get_tagline(self, x: float, y: float, size: float = 12, color: str = COLORS['gold']) -> str:
        """Generate tagline text"""
        return f'''
        <text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" 
              fill="{color}" text-anchor="middle" font-weight="300" letter-spacing="2">
            CUSTOM BIKE SHOP
        </text>
        '''
    
    def create_svg(self, width: int, height: int, content: str, viewbox: str = None) -> str:
        """Wrap content in SVG tags"""
        if viewbox is None:
            viewbox = f"0 0 {width} {height}"
        
        return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}" width="{width}" height="{height}">
    <defs>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700&amp;display=swap');
        </style>
    </defs>
    {content}
</svg>'''
    
    def save_logo(self, filename: str, svg_content: str):
        """Save SVG content to file"""
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"✓ Generated: {filename}")
    
    # ==================== LOGO VARIATIONS ====================
    
    def logo_1_horizontal_primary(self):
        """Horizontal layout - Icon left, text right"""
        content = f'''
        <rect width="600" height="200" fill="{COLORS['emerald_dark']}"/>
        {self.get_rift_icon(20, 50, 1.0, COLORS['gold'])}
        {self.get_rift_text_geometric(180, 70, 60, COLORS['white'], 'bold')}
        '''
        self.save_logo('rift-logo-01-horizontal-primary.svg', 
                      self.create_svg(600, 200, content))
    
    def logo_2_vertical_stacked(self):
        """Vertical layout - Icon above text"""
        content = f'''
        <rect width="300" height="400" fill="{COLORS['emerald_mid']}"/>
        {self.get_rift_icon(100, 50, 1.0, COLORS['gold'])}
        {self.get_rift_text_geometric(68, 240, 50, COLORS['white'], 'bold')}
        '''
        self.save_logo('rift-logo-02-vertical-stacked.svg', 
                      self.create_svg(300, 400, content))
    
    def logo_3_horizontal_with_tagline(self):
        """Horizontal with tagline below"""
        content = f'''
        <rect width="600" height="250" fill="{COLORS['emerald_dark']}"/>
        {self.get_rift_icon(20, 50, 1.0, COLORS['gold'])}
        {self.get_rift_text_geometric(180, 70, 60, COLORS['white'], 'bold')}
        {self.get_tagline(300, 200, 14, COLORS['gold'])}
        '''
        self.save_logo('rift-logo-03-horizontal-tagline.svg', 
                      self.create_svg(600, 250, content))
    
    def logo_4_icon_only_square(self):
        """Icon only - Square format"""
        content = f'''
        <rect width="200" height="200" fill="{COLORS['emerald_dark']}"/>
        {self.get_rift_icon(50, 50, 1.0, COLORS['gold'])}
        '''
        self.save_logo('rift-logo-04-icon-only-square.svg', 
                      self.create_svg(200, 200, content))
    
    def logo_5_text_only_horizontal(self):
        """Text only - No icon"""
        content = f'''
        <rect width="400" height="150" fill="{COLORS['emerald_mid']}"/>
        {self.get_rift_text_geometric(50, 70, 60, COLORS['gold'], 'bold')}
        '''
        self.save_logo('rift-logo-05-text-only.svg', 
                      self.create_svg(400, 150, content))
    
    def logo_6_circle_badge(self):
        """Circular badge design"""
        content = f'''
        <circle cx="200" cy="200" r="195" fill="{COLORS['emerald_dark']}" 
                stroke="{COLORS['gold']}" stroke-width="5"/>
        {self.get_rift_icon(150, 80, 0.5, COLORS['gold'])}
        {self.get_rift_text_geometric(83, 200, 40, COLORS['white'], 'bold')}
        <text x="200" y="290" font-family="Arial, sans-serif" font-size="12" 
              fill="{COLORS['gold']}" text-anchor="middle" letter-spacing="3">
            CUSTOM BIKES
        </text>
        '''
        self.save_logo('rift-logo-06-circle-badge.svg', 
                      self.create_svg(400, 400, content))
    
    def logo_7_compact_square(self):
        """Compact version for small spaces"""
        content = f'''
        <rect width="150" height="150" fill="{COLORS['emerald_dark']}"/>
        {self.get_rift_icon(37.5, 20, 0.5, COLORS['gold'])}
        {self.get_rift_text_geometric(25, 90, 30, COLORS['white'], 'bold')}
        '''
        self.save_logo('rift-logo-07-compact-square.svg', 
                      self.create_svg(150, 150, content))
    
    def logo_8_wide_banner(self):
        """Wide banner format"""
        content = f'''
        <rect width="1200" height="200" fill="{COLORS['emerald_dark']}"/>
        <line x1="0" y1="195" x2="1200" y2="195" stroke="{COLORS['gold']}" stroke-width="5"/>
        {self.get_rift_icon(100, 50, 1.0, COLORS['gold'])}
        {self.get_rift_text_geometric(300, 70, 70, COLORS['white'], 'bold')}
        {self.get_tagline(850, 120, 16, COLORS['gold'])}
        '''
        self.save_logo('rift-logo-08-wide-banner.svg', 
                      self.create_svg(1200, 200, content))
    
    def logo_9_minimal_transparent(self):
        """Minimal - Transparent background"""
        content = f'''
        {self.get_rift_icon(0, 0, 0.8, COLORS['emerald_dark'])}
        {self.get_rift_text_geometric(100, 40, 45, COLORS['emerald_dark'], 'bold')}
        '''
        self.save_logo('rift-logo-09-minimal-transparent.svg', 
                      self.create_svg(350, 120, content))
    
    def logo_10_watermark(self):
        """Watermark version - Semi-transparent"""
        content = f'''
        <g opacity="0.15">
            {self.get_rift_icon(50, 50, 1.5, COLORS['black'])}
            {self.get_rift_text_geometric(220, 100, 80, COLORS['black'], 'bold')}
        </g>
        '''
        self.save_logo('rift-logo-10-watermark.svg', 
                      self.create_svg(600, 300, content))
    
    def logo_11_inverted_colors(self):
        """Inverted color scheme"""
        content = f'''
        <rect width="600" height="200" fill="{COLORS['gold']}"/>
        {self.get_rift_icon(20, 50, 1.0, COLORS['emerald_dark'])}
        {self.get_rift_text_geometric(180, 70, 60, COLORS['emerald_dark'], 'bold')}
        '''
        self.save_logo('rift-logo-11-inverted-colors.svg', 
                      self.create_svg(600, 200, content))
    
    def logo_12_vertical_with_tagline(self):
        """Vertical with tagline"""
        content = f'''
        <rect width="300" height="450" fill="{COLORS['emerald_dark']}"/>
        {self.get_rift_icon(100, 50, 1.0, COLORS['gold'])}
        {self.get_rift_text_geometric(68, 240, 50, COLORS['white'], 'bold')}
        {self.get_tagline(150, 350, 12, COLORS['gold'])}
        '''
        self.save_logo('rift-logo-12-vertical-tagline.svg', 
                      self.create_svg(300, 450, content))
    
    def logo_13_square_badge(self):
        """Square badge with border"""
        content = f'''
        <rect width="400" height="400" fill="{COLORS['emerald_dark']}" 
              stroke="{COLORS['gold']}" stroke-width="8"/>
        {self.get_rift_icon(150, 80, 1.0, COLORS['gold'])}
        {self.get_rift_text_geometric(100, 230, 55, COLORS['white'], 'bold')}
        <text x="200" y="340" font-family="Arial, sans-serif" font-size="14" 
              fill="{COLORS['gold']}" text-anchor="middle" letter-spacing="4">
            EST. 2025
        </text>
        '''
        self.save_logo('rift-logo-13-square-badge.svg', 
                      self.create_svg(400, 400, content))
    
    def logo_14_horizontal_reversed(self):
        """Horizontal - Text left, icon right"""
        content = f'''
        <rect width="600" height="200" fill="{COLORS['emerald_mid']}"/>
        {self.get_rift_text_geometric(50, 70, 60, COLORS['white'], 'bold')}
        {self.get_rift_icon(450, 50, 1.0, COLORS['gold'])}
        '''
        self.save_logo('rift-logo-14-horizontal-reversed.svg', 
                      self.create_svg(600, 200, content))
    
    def logo_15_icon_with_border(self):
        """Icon only with decorative border"""
        content = f'''
        <rect width="250" height="250" fill="{COLORS['emerald_dark']}" 
              stroke="{COLORS['gold']}" stroke-width="3"/>
        <rect x="15" y="15" width="220" height="220" fill="none" 
              stroke="{COLORS['gold']}" stroke-width="1"/>
        {self.get_rift_icon(75, 75, 1.0, COLORS['gold'])}
        '''
        self.save_logo('rift-logo-15-icon-bordered.svg', 
                      self.create_svg(250, 250, content))
    
    def logo_16_text_outlined(self):
        """Text with outline effect"""
        content = f'''
        <rect width="450" height="180" fill="{COLORS['emerald_dark']}"/>
        <!-- Background text (outline) -->
        {self.get_rift_text_geometric(60, 70, 65, 'none', 'bold').replace('fill="none"', f'fill="none" stroke="{COLORS["gold"]}" stroke-width="2"')}
        <!-- Foreground text -->
        {self.get_rift_text_geometric(60, 70, 65, COLORS['emerald_dark'], 'bold').replace('stroke=', 'fill=').replace(f'{COLORS["emerald_dark"]}', COLORS['white'])}
        '''
        self.save_logo('rift-logo-16-text-outlined.svg', 
                      self.create_svg(450, 180, content))
    
    def logo_17_angled_dynamic(self):
        """Dynamic angled layout"""
        content = f'''
        <rect width="700" height="250" fill="{COLORS['emerald_dark']}"/>
        <polygon points="0,0 700,0 650,250 0,250" fill="{COLORS['emerald_mid']}"/>
        <g transform="translate(50, 50) rotate(-5)">
            {self.get_rift_icon(0, 0, 1.0, COLORS['gold'])}
        </g>
        <g transform="translate(200, 20) rotate(-3)">
            {self.get_rift_text_geometric(0, 70, 70, COLORS['white'], 'bold')}
        </g>
        '''
        self.save_logo('rift-logo-17-angled-dynamic.svg', 
                      self.create_svg(700, 250, content))
    
    def logo_18_monochrome_gold(self):
        """Monochrome gold version"""
        content = f'''
        {self.get_rift_icon(0, 0, 1.2, COLORS['gold'])}
        {self.get_rift_text_geometric(140, 50, 70, COLORS['gold'], 'bold')}
        '''
        self.save_logo('rift-logo-18-monochrome-gold.svg', 
                      self.create_svg(500, 170, content))
    
    def logo_19_stacked_centered(self):
        """Centered stacked with accent lines"""
        content = f'''
        <rect width="400" height="450" fill="{COLORS['emerald_dark']}"/>
        <line x1="50" y1="40" x2="350" y2="40" stroke="{COLORS['gold']}" stroke-width="2"/>
        {self.get_rift_icon(150, 80, 1.0, COLORS['gold'])}
        {self.get_rift_text_geometric(100, 250, 55, COLORS['white'], 'bold')}
        <line x1="50" y1="360" x2="350" y2="360" stroke="{COLORS['gold']}" stroke-width="2"/>
        {self.get_tagline(200, 400, 13, COLORS['gold'])}
        '''
        self.save_logo('rift-logo-19-stacked-centered.svg', 
                      self.create_svg(400, 450, content))
    
    def logo_20_minimal_icon_text(self):
        """Ultra minimal - Small icon + text"""
        content = f'''
        {self.get_rift_icon(0, 0, 0.4, COLORS['emerald_dark'])}
        {self.get_rift_text_geometric(60, 20, 30, COLORS['emerald_dark'], 'bold')}
        '''
        self.save_logo('rift-logo-20-minimal-icon-text.svg', 
                      self.create_svg(250, 70, content))
    
    def generate_all(self):
        """Generate all 20 logo variations"""
        print("\n🎨 RIFT Logo Generator")
        print("=" * 50)
        print(f"Output directory: {self.output_dir}\n")
        
        # Generate all logos
        self.logo_1_horizontal_primary()
        self.logo_2_vertical_stacked()
        self.logo_3_horizontal_with_tagline()
        self.logo_4_icon_only_square()
        self.logo_5_text_only_horizontal()
        self.logo_6_circle_badge()
        self.logo_7_compact_square()
        self.logo_8_wide_banner()
        self.logo_9_minimal_transparent()
        self.logo_10_watermark()
        self.logo_11_inverted_colors()
        self.logo_12_vertical_with_tagline()
        self.logo_13_square_badge()
        self.logo_14_horizontal_reversed()
        self.logo_15_icon_with_border()
        self.logo_16_text_outlined()
        self.logo_17_angled_dynamic()
        self.logo_18_monochrome_gold()
        self.logo_19_stacked_centered()
        self.logo_20_minimal_icon_text()
        
        # Generate preview HTML
        self.generate_preview_html()
        
        print("\n" + "=" * 50)
        print("✅ All 20 logos generated successfully!")
        print(f"📁 Files saved to: {self.output_dir}")
        print(f"🌐 Preview: {os.path.join(self.output_dir, 'preview.html')}")
    
    def generate_preview_html(self):
        """Generate HTML preview of all logos"""
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RIFT Logo Variations Preview</title>
    <style>
        body {
            font-family: 'Inter', Arial, sans-serif;
            background: #1a1a1a;
            color: #ffffff;
            padding: 40px;
            margin: 0;
        }
        h1 {
            text-align: center;
            color: #fbbf24;
            font-size: 3em;
            margin-bottom: 20px;
        }
        .subtitle {
            text-align: center;
            color: #10b981;
            margin-bottom: 50px;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 30px;
            max-width: 1600px;
            margin: 0 auto;
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
            min-height: 200px;
            margin-bottom: 15px;
        }
        .logo-container img {
            max-width: 100%;
            height: auto;
        }
        .logo-name {
            color: #fbbf24;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .logo-description {
            color: #aaa;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <h1>RIFT LOGO VARIATIONS</h1>
    <p class="subtitle">20 Professional Logo Designs for Custom Bike Shop</p>
    
    <div class="grid">
'''
        
        logos = [
            ('rift-logo-01-horizontal-primary.svg', 'Horizontal Primary', 'Icon left, text right - Main logo'),
            ('rift-logo-02-vertical-stacked.svg', 'Vertical Stacked', 'Icon above text'),
            ('rift-logo-03-horizontal-tagline.svg', 'Horizontal with Tagline', 'Includes custom bike shop tagline'),
            ('rift-logo-04-icon-only-square.svg', 'Icon Only Square', 'Perfect for social media avatars'),
            ('rift-logo-05-text-only.svg', 'Text Only', 'No icon, typography focus'),
            ('rift-logo-06-circle-badge.svg', 'Circle Badge', 'Circular design with border'),
            ('rift-logo-07-compact-square.svg', 'Compact Square', 'Small space optimized'),
            ('rift-logo-08-wide-banner.svg', 'Wide Banner', 'Website header format'),
            ('rift-logo-09-minimal-transparent.svg', 'Minimal Transparent', 'Clean background'),
            ('rift-logo-10-watermark.svg', 'Watermark', 'Semi-transparent for overlays'),
            ('rift-logo-11-inverted-colors.svg', 'Inverted Colors', 'Gold background variation'),
            ('rift-logo-12-vertical-tagline.svg', 'Vertical with Tagline', 'Tall format with subtitle'),
            ('rift-logo-13-square-badge.svg', 'Square Badge', 'Bordered with EST. date'),
            ('rift-logo-14-horizontal-reversed.svg', 'Horizontal Reversed', 'Text left, icon right'),
            ('rift-logo-15-icon-bordered.svg', 'Icon with Border', 'Decorative frame'),
            ('rift-logo-16-text-outlined.svg', 'Text Outlined', 'Outline effect typography'),
            ('rift-logo-17-angled-dynamic.svg', 'Angled Dynamic', 'Energetic slanted design'),
            ('rift-logo-18-monochrome-gold.svg', 'Monochrome Gold', 'Single color version'),
            ('rift-logo-19-stacked-centered.svg', 'Stacked Centered', 'Accent lines top/bottom'),
            ('rift-logo-20-minimal-icon-text.svg', 'Minimal Icon + Text', 'Ultra compact version'),
        ]
        
        for filename, name, description in logos:
            html += f'''
        <div class="logo-card">
            <div class="logo-container">
                <img src="{filename}" alt="{name}">
            </div>
            <div class="logo-name">{name}</div>
            <div class="logo-description">{description}</div>
        </div>
'''
        
        html += '''
    </div>
</body>
</html>'''
        
        preview_path = os.path.join(self.output_dir, 'preview.html')
        with open(preview_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✓ Generated: preview.html")


def main():
    """Main execution function"""
    # You can customize the output directory here
    generator = RIFTLogoGenerator(output_dir='output/logos')
    
    # Generate all 20 logos
    generator.generate_all()


if __name__ == '__main__':
    main()
