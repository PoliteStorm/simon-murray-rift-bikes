#!/usr/bin/env python3
"""
RIFT Logo Generator - Enhanced Typography Edition
Generates 20+ unique SVG logo variations with elegant, flowing, modern fonts
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
    """Generates RIFT logo variations with elegant, modern typography"""
    
    def __init__(self, output_dir: str = 'output/logos-enhanced'):
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
    
    # ==================== ELEGANT TYPOGRAPHY STYLES ====================
    
    def get_rift_text_elegant_serif(self, x: float, y: float, size: float = 60, color: str = COLORS['white']) -> str:
        """Elegant serif with refined curves and sharp accents"""
        scale = size / 60
        sw = 3 * scale  # Stroke width for thin elegant lines
        
        # R: Elegant with curved top bowl and flowing diagonal
        r_path = f'''
            M {x} {y + 60*scale} L {x} {y}
            Q {x + 20*scale} {y} {x + 25*scale} {y + 12*scale}
            Q {x + 28*scale} {y + 20*scale} {x + 25*scale} {y + 28*scale}
            L {x} {y + 28*scale}
            M {x + 10*scale} {y + 28*scale} Q {x + 25*scale} {y + 45*scale} {x + 32*scale} {y + 60*scale}
        '''
        
        # I: Elegant with subtle curves at caps
        i_path = f'''
            M {x + 52*scale} {y} L {x + 52*scale} {y + 60*scale}
            M {x + 42*scale} {y} Q {x + 47*scale} {y + 3*scale} {x + 52*scale} {y + 3*scale}
            Q {x + 57*scale} {y + 3*scale} {x + 62*scale} {y}
            M {x + 42*scale} {y + 60*scale} Q {x + 47*scale} {y + 57*scale} {x + 52*scale} {y + 57*scale}
            Q {x + 57*scale} {y + 57*scale} {x + 62*scale} {y + 60*scale}
        '''
        
        # F: Flowing with elegant crossbar
        f_path = f'''
            M {x + 82*scale} {y + 60*scale} L {x + 82*scale} {y}
            Q {x + 95*scale} {y} {x + 108*scale} {y}
            M {x + 82*scale} {y + 28*scale} Q {x + 92*scale} {y + 28*scale} {x + 102*scale} {y + 28*scale}
        '''
        
        # T: Sophisticated with curved top and sharp vertical
        t_path = f'''
            M {x + 120*scale} {y} Q {x + 138*scale} {y} {x + 158*scale} {y}
            M {x + 139*scale} {y} L {x + 139*scale} {y + 60*scale}
        '''
        
        return f'''
        <g>
            <path d="{r_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="{i_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="{f_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="{t_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        </g>
        '''
    
    def get_rift_text_flowing_script(self, x: float, y: float, size: float = 60, color: str = COLORS['white']) -> str:
        """Flowing connected script style with smooth curves"""
        scale = size / 60
        sw = 3.5 * scale
        
        # R: Flowing script with connected curves
        r_path = f'''
            M {x} {y + 60*scale}
            Q {x} {y + 50*scale} {x} {y + 20*scale}
            Q {x} {y} {x + 15*scale} {y}
            Q {x + 28*scale} {y} {x + 28*scale} {y + 15*scale}
            Q {x + 28*scale} {y + 25*scale} {x + 15*scale} {y + 28*scale}
            Q {x + 5*scale} {y + 28*scale} {x + 5*scale} {y + 35*scale}
            Q {x + 12*scale} {y + 42*scale} {x + 25*scale} {y + 60*scale}
        '''
        
        # I: Simple flowing vertical with subtle curve
        i_path = f'''
            M {x + 48*scale} {y + 2*scale}
            Q {x + 48*scale} {y + 30*scale} {x + 48*scale} {y + 60*scale}
        '''
        
        # F: Flowing F with connected strokes
        f_path = f'''
            M {x + 68*scale} {y + 60*scale}
            Q {x + 68*scale} {y + 40*scale} {x + 68*scale} {y + 15*scale}
            Q {x + 68*scale} {y} {x + 82*scale} {y}
            Q {x + 95*scale} {y} {x + 105*scale} {y}
            M {x + 68*scale} {y + 28*scale}
            Q {x + 75*scale} {y + 27*scale} {x + 88*scale} {y + 28*scale}
        '''
        
        # T: Elegant flowing T
        t_path = f'''
            M {x + 115*scale} {y + 3*scale}
            Q {x + 130*scale} {y} {x + 148*scale} {y + 3*scale}
            M {x + 132*scale} {y + 2*scale}
            Q {x + 132*scale} {y + 30*scale} {x + 132*scale} {y + 60*scale}
        '''
        
        return f'''
        <g>
            <path d="{r_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="{i_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="{f_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="{t_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round" stroke-linejoin="round"/>
        </g>
        '''
    
    def get_rift_text_modern_sans(self, x: float, y: float, size: float = 60, color: str = COLORS['white']) -> str:
        """Modern sans-serif with elegant proportions and subtle curves"""
        scale = size / 60
        sw = 4 * scale
        
        # R: Modern with subtle curve at top
        r_path = f'''
            M {x} {y + 60*scale} L {x} {y + 5*scale}
            Q {x} {y} {x + 5*scale} {y}
            L {x + 20*scale} {y}
            Q {x + 30*scale} {y} {x + 30*scale} {y + 14*scale}
            Q {x + 30*scale} {y + 26*scale} {x + 18*scale} {y + 26*scale}
            L {x} {y + 26*scale}
            M {x + 8*scale} {y + 26*scale} L {x + 30*scale} {y + 60*scale}
        '''
        
        # I: Clean minimal I
        i_path = f'''
            M {x + 52*scale} {y} L {x + 52*scale} {y + 60*scale}
        '''
        
        # F: Modern clean F
        f_path = f'''
            M {x + 74*scale} {y + 60*scale} L {x + 74*scale} {y}
            L {x + 105*scale} {y}
            M {x + 74*scale} {y + 28*scale} L {x + 98*scale} {y + 28*scale}
        '''
        
        # T: Clean modern T
        t_path = f'''
            M {x + 117*scale} {y} L {x + 155*scale} {y}
            M {x + 136*scale} {y} L {x + 136*scale} {y + 60*scale}
        '''
        
        return f'''
        <g>
            <path d="{r_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="{i_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round"/>
            <path d="{f_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round"/>
            <path d="{t_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round"/>
        </g>
        '''
    
    def get_rift_text_italic_dynamic(self, x: float, y: float, size: float = 60, color: str = COLORS['white']) -> str:
        """Italic style with forward lean and dynamic energy"""
        scale = size / 60
        sw = 3.5 * scale
        
        # R: Italic with dynamic flow
        r_path = f'''
            M {x + 8*scale} {y + 60*scale} L {x + 18*scale} {y}
            L {x + 38*scale} {y}
            Q {x + 43*scale} {y + 12*scale} {x + 38*scale} {y + 25*scale}
            L {x + 18*scale} {y + 25*scale}
            M {x + 23*scale} {y + 25*scale} L {x + 38*scale} {y + 60*scale}
        '''
        
        # I: Slanted I
        i_path = f'''
            M {x + 60*scale} {y} L {x + 50*scale} {y + 60*scale}
        '''
        
        # F: Italic F
        f_path = f'''
            M {x + 70*scale} {y + 60*scale} L {x + 80*scale} {y}
            L {x + 108*scale} {y}
            M {x + 75*scale} {y + 28*scale} L {x + 98*scale} {y + 28*scale}
        '''
        
        # T: Italic T
        t_path = f'''
            M {x + 120*scale} {y} L {x + 155*scale} {y}
            M {x + 138*scale} {y} L {x + 128*scale} {y + 60*scale}
        '''
        
        return f'''
        <g>
            <path d="{r_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="{i_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round"/>
            <path d="{f_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round"/>
            <path d="{t_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round"/>
        </g>
        '''
    
    def get_rift_text_brush_stroke(self, x: float, y: float, size: float = 60, color: str = COLORS['white']) -> str:
        """Brush stroke style with organic, hand-drawn feel"""
        scale = size / 60
        sw = 5 * scale
        
        # R: Organic brush strokes
        r_path = f'''
            M {x} {y + 60*scale}
            Q {x - 2*scale} {y + 40*scale} {x} {y + 10*scale}
            Q {x + 2*scale} {y} {x + 18*scale} {y}
            Q {x + 30*scale} {y + 5*scale} {x + 28*scale} {y + 18*scale}
            Q {x + 26*scale} {y + 28*scale} {x + 12*scale} {y + 28*scale}
            M {x + 12*scale} {y + 30*scale}
            Q {x + 20*scale} {y + 45*scale} {x + 30*scale} {y + 60*scale}
        '''
        
        # I: Organic I
        i_path = f'''
            M {x + 50*scale} {y}
            Q {x + 51*scale} {y + 30*scale} {x + 49*scale} {y + 60*scale}
        '''
        
        # F: Brush stroke F
        f_path = f'''
            M {x + 69*scale} {y + 60*scale}
            Q {x + 70*scale} {y + 30*scale} {x + 69*scale} {y + 3*scale}
            Q {x + 80*scale} {y} {x + 98*scale} {y + 2*scale}
            M {x + 69*scale} {y + 28*scale}
            Q {x + 78*scale} {y + 27*scale} {x + 88*scale} {y + 29*scale}
        '''
        
        # T: Organic T
        t_path = f'''
            M {x + 108*scale} {y + 2*scale}
            Q {x + 125*scale} {y} {x + 148*scale} {y + 2*scale}
            M {x + 128*scale} {y + 2*scale}
            Q {x + 129*scale} {y + 30*scale} {x + 128*scale} {y + 60*scale}
        '''
        
        return f'''
        <g>
            <path d="{r_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="{i_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round"/>
            <path d="{f_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round"/>
            <path d="{t_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round"/>
        </g>
        '''
    
    def get_rift_text_condensed_elegant(self, x: float, y: float, size: float = 60, color: str = COLORS['white']) -> str:
        """Condensed elegant style - tall and refined"""
        scale = size / 60
        sw = 3 * scale
        
        # R: Tall condensed R
        r_path = f'''
            M {x} {y + 60*scale} L {x} {y}
            L {x + 15*scale} {y}
            Q {x + 22*scale} {y + 8*scale} {x + 15*scale} {y + 22*scale}
            L {x} {y + 22*scale}
            M {x + 7*scale} {y + 22*scale} L {x + 22*scale} {y + 60*scale}
        '''
        
        # I: Tall I
        i_path = f'''
            M {x + 40*scale} {y} L {x + 40*scale} {y + 60*scale}
        '''
        
        # F: Condensed F
        f_path = f'''
            M {x + 58*scale} {y + 60*scale} L {x + 58*scale} {y}
            L {x + 78*scale} {y}
            M {x + 58*scale} {y + 28*scale} L {x + 73*scale} {y + 28*scale}
        '''
        
        # T: Condensed T
        t_path = f'''
            M {x + 88*scale} {y} L {x + 118*scale} {y}
            M {x + 103*scale} {y} L {x + 103*scale} {y + 60*scale}
        '''
        
        return f'''
        <g>
            <path d="{r_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="{i_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round"/>
            <path d="{f_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round"/>
            <path d="{t_path}" stroke="{color}" stroke-width="{sw}" 
                  fill="none" stroke-linecap="round"/>
        </g>
        '''
    
    def get_tagline(self, x: float, y: float, size: float = 12, color: str = COLORS['gold']) -> str:
        """Generate tagline text"""
        return f'''
        <text x="{x}" y="{y}" font-family="'Inter', 'Helvetica Neue', sans-serif" font-size="{size}" 
              fill="{color}" text-anchor="middle" font-weight="300" letter-spacing="3">
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
    
    # ==================== LOGO VARIATIONS WITH ELEGANT TYPOGRAPHY ====================
    
    def logo_1_elegant_serif_horizontal(self):
        """Elegant serif - Horizontal layout"""
        content = f'''
        <rect width="600" height="200" fill="{COLORS['emerald_dark']}"/>
        {self.get_rift_icon(20, 50, 1.0, COLORS['gold'])}
        {self.get_rift_text_elegant_serif(180, 70, 60, COLORS['white'])}
        '''
        self.save_logo('rift-logo-01-elegant-serif-horizontal.svg', 
                      self.create_svg(600, 200, content))
    
    def logo_2_flowing_script_vertical(self):
        """Flowing script - Vertical stacked"""
        content = f'''
        <rect width="300" height="400" fill="{COLORS['emerald_mid']}"/>
        {self.get_rift_icon(100, 50, 1.0, COLORS['gold'])}
        {self.get_rift_text_flowing_script(75, 220, 45, COLORS['white'])}
        '''
        self.save_logo('rift-logo-02-flowing-script-vertical.svg', 
                      self.create_svg(300, 400, content))
    
    def logo_3_modern_sans_with_tagline(self):
        """Modern sans-serif with tagline"""
        content = f'''
        <rect width="600" height="250" fill="{COLORS['emerald_dark']}"/>
        {self.get_rift_icon(20, 50, 1.0, COLORS['gold'])}
        {self.get_rift_text_modern_sans(180, 70, 60, COLORS['white'])}
        {self.get_tagline(300, 200, 14, COLORS['gold'])}
        '''
        self.save_logo('rift-logo-03-modern-sans-tagline.svg', 
                      self.create_svg(600, 250, content))
    
    def logo_4_italic_dynamic_horizontal(self):
        """Italic dynamic - Horizontal"""
        content = f'''
        <rect width="600" height="200" fill="{COLORS['emerald_mid']}"/>
        {self.get_rift_icon(20, 50, 1.0, COLORS['gold'])}
        {self.get_rift_text_italic_dynamic(180, 70, 60, COLORS['white'])}
        '''
        self.save_logo('rift-logo-04-italic-dynamic.svg', 
                      self.create_svg(600, 200, content))
    
    def logo_5_brush_stroke_artistic(self):
        """Brush stroke - Artistic feel"""
        content = f'''
        <rect width="600" height="200" fill="{COLORS['emerald_dark']}"/>
        {self.get_rift_icon(20, 50, 1.0, COLORS['gold'])}
        {self.get_rift_text_brush_stroke(180, 70, 60, COLORS['white'])}
        '''
        self.save_logo('rift-logo-05-brush-stroke.svg', 
                      self.create_svg(600, 200, content))
    
    def logo_6_condensed_elegant_circle(self):
        """Condensed elegant in circle badge"""
        content = f'''
        <circle cx="200" cy="200" r="195" fill="{COLORS['emerald_dark']}" 
                stroke="{COLORS['gold']}" stroke-width="5"/>
        {self.get_rift_icon(150, 80, 0.5, COLORS['gold'])}
        {self.get_rift_text_condensed_elegant(140, 200, 35, COLORS['white'])}
        <text x="200" y="290" font-family="'Inter', sans-serif" font-size="12" 
              fill="{COLORS['gold']}" text-anchor="middle" letter-spacing="3">
            CUSTOM BIKES
        </text>
        '''
        self.save_logo('rift-logo-06-condensed-circle.svg', 
                      self.create_svg(400, 400, content))
    
    def logo_7_elegant_serif_vertical(self):
        """Elegant serif - Vertical with tagline"""
        content = f'''
        <rect width="280" height="450" fill="{COLORS['emerald_dark']}"/>
        {self.get_rift_icon(90, 50, 1.0, COLORS['gold'])}
        {self.get_rift_text_elegant_serif(60, 220, 50, COLORS['white'])}
        {self.get_tagline(140, 340, 12, COLORS['gold'])}
        '''
        self.save_logo('rift-logo-07-elegant-serif-vertical.svg', 
                      self.create_svg(280, 450, content))
    
    def logo_8_flowing_script_banner(self):
        """Flowing script - Wide banner"""
        content = f'''
        <rect width="1200" height="200" fill="{COLORS['emerald_mid']}"/>
        <line x1="0" y1="195" x2="1200" y2="195" stroke="{COLORS['gold']}" stroke-width="5"/>
        {self.get_rift_icon(100, 50, 1.0, COLORS['gold'])}
        {self.get_rift_text_flowing_script(300, 70, 65, COLORS['white'])}
        {self.get_tagline(850, 120, 16, COLORS['gold'])}
        '''
        self.save_logo('rift-logo-08-flowing-banner.svg', 
                      self.create_svg(1200, 200, content))
    
    def logo_9_modern_sans_minimal(self):
        """Modern sans - Minimal transparent"""
        content = f'''
        {self.get_rift_icon(0, 0, 0.8, COLORS['emerald_dark'])}
        {self.get_rift_text_modern_sans(100, 35, 42, COLORS['emerald_dark'])}
        '''
        self.save_logo('rift-logo-09-modern-minimal.svg', 
                      self.create_svg(350, 110, content))
    
    def logo_10_italic_gold_on_transparent(self):
        """Italic dynamic - Gold on transparent"""
        content = f'''
        {self.get_rift_icon(0, 0, 0.9, COLORS['gold'])}
        {self.get_rift_text_italic_dynamic(110, 40, 50, COLORS['gold'])}
        '''
        self.save_logo('rift-logo-10-italic-gold.svg', 
                      self.create_svg(370, 120, content))
    
    def logo_11_brush_stroke_inverted(self):
        """Brush stroke - Inverted colors"""
        content = f'''
        <rect width="600" height="200" fill="{COLORS['gold']}"/>
        {self.get_rift_icon(20, 50, 1.0, COLORS['emerald_dark'])}
        {self.get_rift_text_brush_stroke(180, 70, 60, COLORS['emerald_dark'])}
        '''
        self.save_logo('rift-logo-11-brush-inverted.svg', 
                      self.create_svg(600, 200, content))
    
    def logo_12_condensed_square_badge(self):
        """Condensed elegant - Square badge"""
        content = f'''
        <rect width="350" height="350" fill="{COLORS['emerald_dark']}" 
              stroke="{COLORS['gold']}" stroke-width="8"/>
        {self.get_rift_icon(125, 70, 1.0, COLORS['gold'])}
        {self.get_rift_text_condensed_elegant(125, 200, 45, COLORS['white'])}
        <text x="175" y="300" font-family="'Inter', sans-serif" font-size="12" 
              fill="{COLORS['gold']}" text-anchor="middle" letter-spacing="4">
            EST. 2025
        </text>
        '''
        self.save_logo('rift-logo-12-condensed-badge.svg', 
                      self.create_svg(350, 350, content))
    
    def logo_13_elegant_serif_gold(self):
        """Elegant serif - All gold version"""
        content = f'''
        {self.get_rift_icon(0, 0, 1.0, COLORS['gold'])}
        {self.get_rift_text_elegant_serif(120, 45, 55, COLORS['gold'])}
        '''
        self.save_logo('rift-logo-13-elegant-gold.svg', 
                      self.create_svg(400, 140, content))
    
    def logo_14_flowing_script_compact(self):
        """Flowing script - Compact square"""
        content = f'''
        <rect width="200" height="200" fill="{COLORS['emerald_dark']}"/>
        {self.get_rift_icon(50, 30, 0.6, COLORS['gold'])}
        {self.get_rift_text_flowing_script(30, 120, 35, COLORS['white'])}
        '''
        self.save_logo('rift-logo-14-flowing-compact.svg', 
                      self.create_svg(200, 200, content))
    
    def logo_15_modern_sans_watermark(self):
        """Modern sans - Watermark version"""
        content = f'''
        <g opacity="0.2">
            {self.get_rift_icon(50, 50, 1.5, COLORS['black'])}
            {self.get_rift_text_modern_sans(220, 100, 80, COLORS['black'])}
        </g>
        '''
        self.save_logo('rift-logo-15-modern-watermark.svg', 
                      self.create_svg(600, 300, content))
    
    def logo_16_italic_dynamic_reversed(self):
        """Italic dynamic - Text left, icon right"""
        content = f'''
        <rect width="600" height="200" fill="{COLORS['emerald_mid']}"/>
        {self.get_rift_text_italic_dynamic(50, 70, 60, COLORS['white'])}
        {self.get_rift_icon(450, 50, 1.0, COLORS['gold'])}
        '''
        self.save_logo('rift-logo-16-italic-reversed.svg', 
                      self.create_svg(600, 200, content))
    
    def logo_17_brush_stroke_text_only(self):
        """Brush stroke - Text only"""
        content = f'''
        <rect width="450" height="180" fill="{COLORS['emerald_dark']}"/>
        {self.get_rift_text_brush_stroke(50, 70, 65, COLORS['white'])}
        '''
        self.save_logo('rift-logo-17-brush-text-only.svg', 
                      self.create_svg(450, 180, content))
    
    def logo_18_condensed_elegant_stacked(self):
        """Condensed elegant - Stacked centered"""
        content = f'''
        <rect width="400" height="450" fill="{COLORS['emerald_dark']}"/>
        <line x1="50" y1="40" x2="350" y2="40" stroke="{COLORS['gold']}" stroke-width="2"/>
        {self.get_rift_icon(150, 80, 1.0, COLORS['gold'])}
        {self.get_rift_text_condensed_elegant(100, 250, 55, COLORS['white'])}
        <line x1="50" y1="360" x2="350" y2="360" stroke="{COLORS['gold']}" stroke-width="2"/>
        {self.get_tagline(200, 400, 13, COLORS['gold'])}
        '''
        self.save_logo('rift-logo-18-condensed-stacked.svg', 
                      self.create_svg(400, 450, content))
    
    def logo_19_elegant_serif_icon_bordered(self):
        """Elegant serif - Icon with decorative border"""
        content = f'''
        <rect width="250" height="250" fill="{COLORS['emerald_dark']}" 
              stroke="{COLORS['gold']}" stroke-width="3"/>
        <rect x="15" y="15" width="220" height="220" fill="none" 
              stroke="{COLORS['gold']}" stroke-width="1"/>
        {self.get_rift_icon(75, 75, 1.0, COLORS['gold'])}
        {self.get_rift_text_elegant_serif(50, 180, 30, COLORS['white'])}
        '''
        self.save_logo('rift-logo-19-elegant-bordered.svg', 
                      self.create_svg(250, 250, content))
    
    def logo_20_flowing_script_minimal(self):
        """Flowing script - Ultra minimal"""
        content = f'''
        {self.get_rift_icon(0, 0, 0.4, COLORS['emerald_dark'])}
        {self.get_rift_text_flowing_script(60, 20, 30, COLORS['emerald_dark'])}
        '''
        self.save_logo('rift-logo-20-flowing-minimal.svg', 
                      self.create_svg(250, 70, content))
    
    def generate_all(self):
        """Generate all 20 logo variations"""
        print("\n🎨 RIFT Logo Generator - Enhanced Typography Edition")
        print("=" * 60)
        print(f"Output directory: {self.output_dir}\n")
        
        # Generate all logos
        self.logo_1_elegant_serif_horizontal()
        self.logo_2_flowing_script_vertical()
        self.logo_3_modern_sans_with_tagline()
        self.logo_4_italic_dynamic_horizontal()
        self.logo_5_brush_stroke_artistic()
        self.logo_6_condensed_elegant_circle()
        self.logo_7_elegant_serif_vertical()
        self.logo_8_flowing_script_banner()
        self.logo_9_modern_sans_minimal()
        self.logo_10_italic_gold_on_transparent()
        self.logo_11_brush_stroke_inverted()
        self.logo_12_condensed_square_badge()
        self.logo_13_elegant_serif_gold()
        self.logo_14_flowing_script_compact()
        self.logo_15_modern_sans_watermark()
        self.logo_16_italic_dynamic_reversed()
        self.logo_17_brush_stroke_text_only()
        self.logo_18_condensed_elegant_stacked()
        self.logo_19_elegant_serif_icon_bordered()
        self.logo_20_flowing_script_minimal()
        
        # Generate preview HTML
        self.generate_preview_html()
        
        print("\n" + "=" * 60)
        print("✅ All 20 elegant typography logos generated successfully!")
        print(f"📁 Files saved to: {self.output_dir}")
        print(f"🌐 Preview: {os.path.join(self.output_dir, 'preview.html')}")
    
    def generate_preview_html(self):
        """Generate HTML preview of all logos"""
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RIFT Logo Variations - Enhanced Typography</title>
    <style>
        body {
            font-family: 'Inter', Arial, sans-serif;
            background: #0a1f1a;
            color: #ffffff;
            padding: 40px;
            margin: 0;
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
            margin-bottom: 50px;
            font-size: 1.2em;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 30px;
            max-width: 1600px;
            margin: 0 auto;
        }
        .logo-card {
            background: #0f3d32;
            border: 2px solid #065f46;
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
            font-size: 1.1em;
        }
        .logo-description {
            color: #aaa;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <h1>RIFT LOGO VARIATIONS</h1>
    <p class="subtitle">Enhanced Typography Edition - 20 Elegant Designs</p>
    
    <div class="grid">
'''
        
        logos = [
            ('rift-logo-01-elegant-serif-horizontal.svg', 'Elegant Serif Horizontal', 'Refined serif with curved accents'),
            ('rift-logo-02-flowing-script-vertical.svg', 'Flowing Script Vertical', 'Connected script style'),
            ('rift-logo-03-modern-sans-tagline.svg', 'Modern Sans with Tagline', 'Clean modern sans-serif'),
            ('rift-logo-04-italic-dynamic.svg', 'Italic Dynamic', 'Forward-leaning dynamic style'),
            ('rift-logo-05-brush-stroke.svg', 'Brush Stroke Artistic', 'Organic hand-drawn feel'),
            ('rift-logo-06-condensed-circle.svg', 'Condensed Circle Badge', 'Tall refined in circle'),
            ('rift-logo-07-elegant-serif-vertical.svg', 'Elegant Serif Vertical', 'Vertical with tagline'),
            ('rift-logo-08-flowing-banner.svg', 'Flowing Script Banner', 'Wide banner format'),
            ('rift-logo-09-modern-minimal.svg', 'Modern Sans Minimal', 'Clean transparent background'),
            ('rift-logo-10-italic-gold.svg', 'Italic Gold', 'Gold on transparent'),
            ('rift-logo-11-brush-inverted.svg', 'Brush Inverted', 'Gold background variation'),
            ('rift-logo-12-condensed-badge.svg', 'Condensed Square Badge', 'Bordered with EST. date'),
            ('rift-logo-13-elegant-gold.svg', 'Elegant Serif Gold', 'All gold monochrome'),
            ('rift-logo-14-flowing-compact.svg', 'Flowing Script Compact', 'Compact square format'),
            ('rift-logo-15-modern-watermark.svg', 'Modern Sans Watermark', 'Semi-transparent overlay'),
            ('rift-logo-16-italic-reversed.svg', 'Italic Reversed', 'Text left, icon right'),
            ('rift-logo-17-brush-text-only.svg', 'Brush Text Only', 'Typography focus'),
            ('rift-logo-18-condensed-stacked.svg', 'Condensed Stacked', 'Centered with accent lines'),
            ('rift-logo-19-elegant-bordered.svg', 'Elegant Bordered', 'Icon with decorative frame'),
            ('rift-logo-20-flowing-minimal.svg', 'Flowing Minimal', 'Ultra compact version'),
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
    generator = RIFTLogoGenerator(output_dir='output/logos-enhanced')
    generator.generate_all()


if __name__ == '__main__':
    main()
