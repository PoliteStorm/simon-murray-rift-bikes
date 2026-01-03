#!/usr/bin/env python3
"""
RIFT Icon Variations Generator
Generates multiple icon variations with different complexity, styles, sizes, and colors
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


class RIFTIconVariationGenerator:
    """Generates icon variations with different styles and configurations"""
    
    def __init__(self, output_dir: str = 'output/icon-variations'):
        self.output_dir = output_dir
        self.ensure_output_dir()
    
    def ensure_output_dir(self):
        """Create output directory if it doesn't exist"""
        os.makedirs(self.output_dir, exist_ok=True)
    
    def create_svg(self, width: int, height: int, content: str, 
                  viewbox: str = None, background: str = None) -> str:
        """Wrap content in SVG tags"""
        if viewbox is None:
            viewbox = f"0 0 {width} {height}"
        
        bg = f'<rect width="{width}" height="{height}" fill="{background}"/>' if background else ''
        
        return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}" width="{width}" height="{height}">
    {bg}
    {content}
</svg>'''
    
    def save_icon(self, filename: str, svg_content: str):
        """Save SVG content to file"""
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"✓ Generated: {filename}")
    
    # ===== COMPLEXITY VARIATIONS =====
    
    def generate_minimal_icon(self, size: int = 100, color: str = COLORS['gold'], 
                              background: str = None):
        """Ultra-simplified, just essential lines"""
        filename = f"rift-icon-minimal-{size}px.svg"
        center_x = size / 2
        scale = size / 100
        
        # Just three horizontal lines, no cracks
        content = f'''
        <g transform="translate({center_x - 40*scale}, {center_x - 20*scale}) scale({scale})">
            <path d="M10 30 L90 30" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <path d="M15 60 L85 60" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <path d="M20 90 L80 90" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
        </g>
        '''
        
        svg = self.create_svg(size, size, content, background=background)
        self.save_icon(filename, svg)
    
    def generate_standard_icon(self, size: int = 100, color: str = COLORS['gold'],
                               background: str = None):
        """Current design - standard complexity"""
        filename = f"rift-icon-standard-{size}px.svg"
        center_x = size / 2
        scale = size / 100
        
        content = f'''
        <g transform="translate({center_x - 40*scale}, {center_x - 20*scale}) scale({scale})">
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
        
        svg = self.create_svg(size, size, content, background=background)
        self.save_icon(filename, svg)
    
    def generate_enhanced_icon(self, size: int = 100, color: str = COLORS['gold'],
                               background: str = None):
        """Additional detail lines, more cracks"""
        filename = f"rift-icon-enhanced-{size}px.svg"
        center_x = size / 2
        scale = size / 100
        
        content = f'''
        <g transform="translate({center_x - 40*scale}, {center_x - 20*scale}) scale({scale})">
            <!-- Horizontal lines -->
            <path d="M10 30 L90 30" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <path d="M15 60 L85 60" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <path d="M20 90 L80 90" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <!-- Primary angular cracks -->
            <path d="M25 15 L28 30 M75 15 L72 30" stroke="{color}" stroke-width="2.5" stroke-linecap="square"/>
            <path d="M30 45 L33 60 M70 45 L67 60" stroke="{color}" stroke-width="2.5" stroke-linecap="square"/>
            <path d="M50 75 L53 90 M50 75 L47 90" stroke="{color}" stroke-width="2.5" stroke-linecap="square"/>
            <!-- Additional cracks -->
            <path d="M40 20 L42 30 M60 20 L58 30" stroke="{color}" stroke-width="2" stroke-linecap="square" opacity="0.7"/>
            <path d="M35 50 L37 60 M65 50 L63 60" stroke="{color}" stroke-width="2" stroke-linecap="square" opacity="0.7"/>
            <path d="M45 80 L47 90 M55 80 L53 90" stroke="{color}" stroke-width="2" stroke-linecap="square" opacity="0.7"/>
            <!-- Detail lines on plates -->
            <path d="M20 30 L25 30" stroke="{color}" stroke-width="1.5" stroke-linecap="square" opacity="0.5"/>
            <path d="M75 30 L80 30" stroke="{color}" stroke-width="1.5" stroke-linecap="square" opacity="0.5"/>
        </g>
        '''
        
        svg = self.create_svg(size, size, content, background=background)
        self.save_icon(filename, svg)
    
    def generate_detailed_icon(self, size: int = 100, color: str = COLORS['gold'],
                               background: str = None):
        """Complex pattern with multiple layers"""
        filename = f"rift-icon-detailed-{size}px.svg"
        center_x = size / 2
        scale = size / 100
        
        content = f'''
        <g transform="translate({center_x - 40*scale}, {center_x - 20*scale}) scale({scale})">
            <!-- Base horizontal lines -->
            <path d="M10 30 L90 30" stroke="{color}" stroke-width="3.5" stroke-linecap="square"/>
            <path d="M15 60 L85 60" stroke="{color}" stroke-width="3.5" stroke-linecap="square"/>
            <path d="M20 90 L80 90" stroke="{color}" stroke-width="3.5" stroke-linecap="square"/>
            <!-- Primary cracks -->
            <path d="M25 15 L28 30 M75 15 L72 30" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <path d="M30 45 L33 60 M70 45 L67 60" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <path d="M50 75 L53 90 M50 75 L47 90" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <!-- Secondary cracks -->
            <path d="M40 20 L42 30 M60 20 L58 30" stroke="{color}" stroke-width="2.5" stroke-linecap="square"/>
            <path d="M35 50 L37 60 M65 50 L63 60" stroke="{color}" stroke-width="2.5" stroke-linecap="square"/>
            <path d="M45 80 L47 90 M55 80 L53 90" stroke="{color}" stroke-width="2.5" stroke-linecap="square"/>
            <!-- Tertiary cracks -->
            <path d="M18 25 L20 30 M82 25 L80 30" stroke="{color}" stroke-width="2" stroke-linecap="square" opacity="0.8"/>
            <path d="M22 55 L24 60 M78 55 L76 60" stroke="{color}" stroke-width="2" stroke-linecap="square" opacity="0.8"/>
            <path d="M48 85 L50 90 M52 85 L50 90" stroke="{color}" stroke-width="2" stroke-linecap="square" opacity="0.8"/>
            <!-- Plate detail lines -->
            <path d="M20 30 L25 30 M75 30 L80 30" stroke="{color}" stroke-width="1.5" stroke-linecap="square" opacity="0.6"/>
            <path d="M25 60 L30 60 M70 60 L75 60" stroke="{color}" stroke-width="1.5" stroke-linecap="square" opacity="0.6"/>
            <path d="M30 90 L35 90 M65 90 L70 90" stroke="{color}" stroke-width="1.5" stroke-linecap="square" opacity="0.6"/>
        </g>
        '''
        
        svg = self.create_svg(size, size, content, background=background)
        self.save_icon(filename, svg)
    
    def generate_ornate_icon(self, size: int = 100, color: str = COLORS['gold'],
                             background: str = None):
        """Decorative elements, flourishes"""
        filename = f"rift-icon-ornate-{size}px.svg"
        center_x = size / 2
        scale = size / 100
        
        content = f'''
        <g transform="translate({center_x - 40*scale}, {center_x - 20*scale}) scale({scale})">
            <!-- Decorative top flourish -->
            <path d="M30 10 Q50 5 70 10" stroke="{color}" stroke-width="2" fill="none" opacity="0.6"/>
            <!-- Horizontal lines with decorative ends -->
            <path d="M5 30 L10 30 M90 30 L95 30" stroke="{color}" stroke-width="2" stroke-linecap="round" opacity="0.5"/>
            <path d="M10 30 L90 30" stroke="{color}" stroke-width="3.5" stroke-linecap="square"/>
            <path d="M5 60 L15 60 M85 60 L95 60" stroke="{color}" stroke-width="2" stroke-linecap="round" opacity="0.5"/>
            <path d="M15 60 L85 60" stroke="{color}" stroke-width="3.5" stroke-linecap="square"/>
            <path d="M5 90 L20 90 M80 90 L95 90" stroke="{color}" stroke-width="2" stroke-linecap="round" opacity="0.5"/>
            <path d="M20 90 L80 90" stroke="{color}" stroke-width="3.5" stroke-linecap="square"/>
            <!-- Angular cracks with decorative elements -->
            <path d="M25 15 L28 30 M75 15 L72 30" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <path d="M30 45 L33 60 M70 45 L67 60" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <path d="M50 75 L53 90 M50 75 L47 90" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <!-- Additional decorative cracks -->
            <path d="M40 20 L42 30 M60 20 L58 30" stroke="{color}" stroke-width="2.5" stroke-linecap="square" opacity="0.7"/>
            <path d="M35 50 L37 60 M65 50 L63 60" stroke="{color}" stroke-width="2.5" stroke-linecap="square" opacity="0.7"/>
            <!-- Bottom decorative flourish -->
            <path d="M35 95 Q50 100 65 95" stroke="{color}" stroke-width="2" fill="none" opacity="0.6"/>
        </g>
        '''
        
        svg = self.create_svg(size, size, content, background=background)
        self.save_icon(filename, svg)
    
    # ===== STYLE VARIATIONS =====
    
    def generate_geometric_icon(self, size: int = 100, color: str = COLORS['gold'],
                                background: str = None):
        """Sharp angles, precise lines"""
        filename = f"rift-icon-geometric-{size}px.svg"
        center_x = size / 2
        scale = size / 100
        
        content = f'''
        <g transform="translate({center_x - 40*scale}, {center_x - 20*scale}) scale({scale})">
            <!-- Sharp horizontal lines -->
            <path d="M10 30 L90 30" stroke="{color}" stroke-width="4" stroke-linecap="square" stroke-linejoin="miter"/>
            <path d="M15 60 L85 60" stroke="{color}" stroke-width="4" stroke-linecap="square" stroke-linejoin="miter"/>
            <path d="M20 90 L80 90" stroke="{color}" stroke-width="4" stroke-linecap="square" stroke-linejoin="miter"/>
            <!-- Sharp angular cracks -->
            <path d="M25 15 L28 30 M75 15 L72 30" stroke="{color}" stroke-width="3" stroke-linecap="square" stroke-linejoin="miter"/>
            <path d="M30 45 L33 60 M70 45 L67 60" stroke="{color}" stroke-width="3" stroke-linecap="square" stroke-linejoin="miter"/>
            <path d="M50 75 L53 90 M50 75 L47 90" stroke="{color}" stroke-width="3" stroke-linecap="square" stroke-linejoin="miter"/>
        </g>
        '''
        
        svg = self.create_svg(size, size, content, background=background)
        self.save_icon(filename, svg)
    
    def generate_organic_icon(self, size: int = 100, color: str = COLORS['gold'],
                             background: str = None):
        """Curved, flowing lines"""
        filename = f"rift-icon-organic-{size}px.svg"
        center_x = size / 2
        scale = size / 100
        
        content = f'''
        <g transform="translate({center_x - 40*scale}, {center_x - 20*scale}) scale({scale})">
            <!-- Curved horizontal lines -->
            <path d="M10 30 Q50 25 90 30" stroke="{color}" stroke-width="3" stroke-linecap="round" fill="none"/>
            <path d="M15 60 Q50 55 85 60" stroke="{color}" stroke-width="3" stroke-linecap="round" fill="none"/>
            <path d="M20 90 Q50 85 80 90" stroke="{color}" stroke-width="3" stroke-linecap="round" fill="none"/>
            <!-- Flowing cracks -->
            <path d="M25 15 Q26.5 22.5 28 30" stroke="{color}" stroke-width="2.5" stroke-linecap="round" fill="none"/>
            <path d="M75 15 Q73.5 22.5 72 30" stroke="{color}" stroke-width="2.5" stroke-linecap="round" fill="none"/>
            <path d="M30 45 Q31.5 52.5 33 60" stroke="{color}" stroke-width="2.5" stroke-linecap="round" fill="none"/>
            <path d="M70 45 Q68.5 52.5 67 60" stroke="{color}" stroke-width="2.5" stroke-linecap="round" fill="none"/>
            <path d="M50 75 Q51.5 82.5 53 90" stroke="{color}" stroke-width="2.5" stroke-linecap="round" fill="none"/>
            <path d="M50 75 Q48.5 82.5 47 90" stroke="{color}" stroke-width="2.5" stroke-linecap="round" fill="none"/>
        </g>
        '''
        
        svg = self.create_svg(size, size, content, background=background)
        self.save_icon(filename, svg)
    
    def generate_tech_icon(self, size: int = 100, color: str = COLORS['gold'],
                          background: str = None):
        """Futuristic, digital aesthetic"""
        filename = f"rift-icon-tech-{size}px.svg"
        center_x = size / 2
        scale = size / 100
        
        content = f'''
        <defs>
            <linearGradient id="tech-gold" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="{color}" stop-opacity="1"/>
                <stop offset="50%" stop-color="#ffd700" stop-opacity="1"/>
                <stop offset="100%" stop-color="{color}" stop-opacity="0.8"/>
            </linearGradient>
            <filter id="glow">
                <feGaussianBlur stdDeviation="1" result="coloredBlur"/>
                <feMerge>
                    <feMergeNode in="coloredBlur"/>
                    <feMergeNode in="SourceGraphic"/>
                </feMerge>
            </filter>
        </defs>
        <g transform="translate({center_x - 40*scale}, {center_x - 20*scale}) scale({scale})">
            <!-- Digital-style lines -->
            <path d="M10 30 L90 30" stroke="url(#tech-gold)" stroke-width="3" stroke-linecap="square" filter="url(#glow)"/>
            <path d="M15 60 L85 60" stroke="url(#tech-gold)" stroke-width="3" stroke-linecap="square" filter="url(#glow)"/>
            <path d="M20 90 L80 90" stroke="url(#tech-gold)" stroke-width="3" stroke-linecap="square" filter="url(#glow)"/>
            <!-- Angular cracks with tech aesthetic -->
            <path d="M25 15 L28 30 M75 15 L72 30" stroke="url(#tech-gold)" stroke-width="2.5" stroke-linecap="square" filter="url(#glow)"/>
            <path d="M30 45 L33 60 M70 45 L67 60" stroke="url(#tech-gold)" stroke-width="2.5" stroke-linecap="square" filter="url(#glow)"/>
            <path d="M50 75 L53 90 M50 75 L47 90" stroke="url(#tech-gold)" stroke-width="2.5" stroke-linecap="square" filter="url(#glow)"/>
            <!-- Digital grid effect -->
            <path d="M10 30 L10 90" stroke="{color}" stroke-width="0.5" stroke-opacity="0.3"/>
            <path d="M90 30 L90 90" stroke="{color}" stroke-width="0.5" stroke-opacity="0.3"/>
        </g>
        '''
        
        svg = self.create_svg(size, size, content, background=background)
        self.save_icon(filename, svg)
    
    def generate_classic_icon(self, size: int = 100, color: str = COLORS['gold'],
                             background: str = None):
        """Traditional, refined"""
        filename = f"rift-icon-classic-{size}px.svg"
        center_x = size / 2
        scale = size / 100
        
        content = f'''
        <g transform="translate({center_x - 40*scale}, {center_x - 20*scale}) scale({scale})">
            <!-- Refined horizontal lines -->
            <path d="M10 30 L90 30" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>
            <path d="M15 60 L85 60" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>
            <path d="M20 90 L80 90" stroke="{color}" stroke-width="2.5" stroke-linecap="round"/>
            <!-- Subtle angular cracks -->
            <path d="M25 15 L28 30 M75 15 L72 30" stroke="{color}" stroke-width="2" stroke-linecap="round"/>
            <path d="M30 45 L33 60 M70 45 L67 60" stroke="{color}" stroke-width="2" stroke-linecap="round"/>
            <path d="M50 75 L53 90 M50 75 L47 90" stroke="{color}" stroke-width="2" stroke-linecap="round"/>
        </g>
        '''
        
        svg = self.create_svg(size, size, content, background=background)
        self.save_icon(filename, svg)
    
    def generate_bold_icon(self, size: int = 100, color: str = COLORS['gold'],
                           background: str = None):
        """Thick strokes, high contrast"""
        filename = f"rift-icon-bold-{size}px.svg"
        center_x = size / 2
        scale = size / 100
        
        content = f'''
        <g transform="translate({center_x - 40*scale}, {center_x - 20*scale}) scale({scale})">
            <!-- Thick horizontal lines -->
            <path d="M10 30 L90 30" stroke="{color}" stroke-width="6" stroke-linecap="square"/>
            <path d="M15 60 L85 60" stroke="{color}" stroke-width="6" stroke-linecap="square"/>
            <path d="M20 90 L80 90" stroke="{color}" stroke-width="6" stroke-linecap="square"/>
            <!-- Bold angular cracks -->
            <path d="M25 15 L28 30 M75 15 L72 30" stroke="{color}" stroke-width="5" stroke-linecap="square"/>
            <path d="M30 45 L33 60 M70 45 L67 60" stroke="{color}" stroke-width="5" stroke-linecap="square"/>
            <path d="M50 75 L53 90 M50 75 L47 90" stroke="{color}" stroke-width="5" stroke-linecap="square"/>
        </g>
        '''
        
        svg = self.create_svg(size, size, content, background=background)
        self.save_icon(filename, svg)
    
    def generate_subtle_icon(self, size: int = 100, color: str = COLORS['gold'],
                            background: str = None):
        """Thin lines, delicate"""
        filename = f"rift-icon-subtle-{size}px.svg"
        center_x = size / 2
        scale = size / 100
        
        content = f'''
        <g transform="translate({center_x - 40*scale}, {center_x - 20*scale}) scale({scale})">
            <!-- Delicate horizontal lines -->
            <path d="M10 30 L90 30" stroke="{color}" stroke-width="1.5" stroke-linecap="round" opacity="0.9"/>
            <path d="M15 60 L85 60" stroke="{color}" stroke-width="1.5" stroke-linecap="round" opacity="0.9"/>
            <path d="M20 90 L80 90" stroke="{color}" stroke-width="1.5" stroke-linecap="round" opacity="0.9"/>
            <!-- Subtle angular cracks -->
            <path d="M25 15 L28 30 M75 15 L72 30" stroke="{color}" stroke-width="1" stroke-linecap="round" opacity="0.8"/>
            <path d="M30 45 L33 60 M70 45 L67 60" stroke="{color}" stroke-width="1" stroke-linecap="round" opacity="0.8"/>
            <path d="M50 75 L53 90 M50 75 L47 90" stroke="{color}" stroke-width="1" stroke-linecap="round" opacity="0.8"/>
        </g>
        '''
        
        svg = self.create_svg(size, size, content, background=background)
        self.save_icon(filename, svg)
    
    # ===== INTEGRATION VARIATIONS =====
    
    def generate_standalone_icon(self, size: int = 100, color: str = COLORS['gold'],
                                 background: str = None):
        """Icon only, no text"""
        self.generate_standard_icon(size, color, background)
        # Rename the file
        old_path = os.path.join(self.output_dir, f"rift-icon-standard-{size}px.svg")
        new_path = os.path.join(self.output_dir, f"rift-icon-standalone-{size}px.svg")
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
    
    def generate_framed_icon(self, size: int = 100, color: str = COLORS['gold'],
                            background: str = None):
        """Icon within decorative border"""
        filename = f"rift-icon-framed-{size}px.svg"
        center_x = size / 2
        scale = size / 120  # Slightly smaller to fit frame
        
        # Frame
        frame_padding = 10
        frame_content = f'''
        <rect x="{frame_padding}" y="{frame_padding}" width="{size - 2*frame_padding}" 
              height="{size - 2*frame_padding}" fill="none" stroke="{color}" 
              stroke-width="2" stroke-linecap="round" rx="4"/>
        '''
        
        # Icon
        icon_content = f'''
        <g transform="translate({center_x - 40*scale}, {center_x - 20*scale}) scale({scale})">
            <path d="M10 30 L90 30" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <path d="M15 60 L85 60" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <path d="M20 90 L80 90" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <path d="M25 15 L28 30 M75 15 L72 30" stroke="{color}" stroke-width="2.5" stroke-linecap="square"/>
            <path d="M30 45 L33 60 M70 45 L67 60" stroke="{color}" stroke-width="2.5" stroke-linecap="square"/>
            <path d="M50 75 L53 90 M50 75 L47 90" stroke="{color}" stroke-width="2.5" stroke-linecap="square"/>
        </g>
        '''
        
        svg = self.create_svg(size, size, frame_content + icon_content, background=background)
        self.save_icon(filename, svg)
    
    def generate_badge_icon(self, size: int = 100, color: str = COLORS['gold'],
                           background: str = None):
        """Icon in circular badge"""
        filename = f"rift-icon-badge-{size}px.svg"
        center_x = size / 2
        center_y = size / 2
        radius = size / 2 - 5
        scale = size / 140  # Smaller to fit in circle
        
        # Circular badge
        badge_content = f'''
        <circle cx="{center_x}" cy="{center_y}" r="{radius}" 
                fill="none" stroke="{color}" stroke-width="3"/>
        '''
        
        # Icon centered
        icon_content = f'''
        <g transform="translate({center_x - 40*scale}, {center_y - 20*scale}) scale({scale})">
            <path d="M10 30 L90 30" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <path d="M15 60 L85 60" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <path d="M20 90 L80 90" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <path d="M25 15 L28 30 M75 15 L72 30" stroke="{color}" stroke-width="2.5" stroke-linecap="square"/>
            <path d="M30 45 L33 60 M70 45 L67 60" stroke="{color}" stroke-width="2.5" stroke-linecap="square"/>
            <path d="M50 75 L53 90 M50 75 L47 90" stroke="{color}" stroke-width="2.5" stroke-linecap="square"/>
        </g>
        '''
        
        svg = self.create_svg(size, size, badge_content + icon_content, background=background)
        self.save_icon(filename, svg)
    
    def generate_square_badge_icon(self, size: int = 100, color: str = COLORS['gold'],
                                   background: str = None):
        """Icon in square badge"""
        filename = f"rift-icon-square-badge-{size}px.svg"
        center_x = size / 2
        center_y = size / 2
        padding = 8
        scale = size / 140
        
        # Square badge
        badge_content = f'''
        <rect x="{padding}" y="{padding}" width="{size - 2*padding}" 
              height="{size - 2*padding}" fill="none" stroke="{color}" 
              stroke-width="3" rx="6"/>
        '''
        
        # Icon centered
        icon_content = f'''
        <g transform="translate({center_x - 40*scale}, {center_y - 20*scale}) scale({scale})">
            <path d="M10 30 L90 30" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <path d="M15 60 L85 60" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <path d="M20 90 L80 90" stroke="{color}" stroke-width="3" stroke-linecap="square"/>
            <path d="M25 15 L28 30 M75 15 L72 30" stroke="{color}" stroke-width="2.5" stroke-linecap="square"/>
            <path d="M30 45 L33 60 M70 45 L67 60" stroke="{color}" stroke-width="2.5" stroke-linecap="square"/>
            <path d="M50 75 L53 90 M50 75 L47 90" stroke="{color}" stroke-width="2.5" stroke-linecap="square"/>
        </g>
        '''
        
        svg = self.create_svg(size, size, badge_content + icon_content, background=background)
        self.save_icon(filename, svg)
    
    # ===== COLOR VARIATIONS =====
    
    def generate_color_variations(self, size: int = 100):
        """Generate all color variations"""
        # Standard: Gold on emerald
        self.generate_standard_icon(size, COLORS['gold'], COLORS['emerald_dark'])
        
        # Inverted: Emerald on gold
        filename = f"rift-icon-inverted-{size}px.svg"
        center_x = size / 2
        scale = size / 100
        content = f'''
        <g transform="translate({center_x - 40*scale}, {center_x - 20*scale}) scale({scale})">
            <path d="M10 30 L90 30" stroke="{COLORS['emerald_dark']}" stroke-width="3" stroke-linecap="square"/>
            <path d="M15 60 L85 60" stroke="{COLORS['emerald_dark']}" stroke-width="3" stroke-linecap="square"/>
            <path d="M20 90 L80 90" stroke="{COLORS['emerald_dark']}" stroke-width="3" stroke-linecap="square"/>
            <path d="M25 15 L28 30 M75 15 L72 30" stroke="{COLORS['emerald_dark']}" stroke-width="2.5" stroke-linecap="square"/>
            <path d="M30 45 L33 60 M70 45 L67 60" stroke="{COLORS['emerald_dark']}" stroke-width="2.5" stroke-linecap="square"/>
            <path d="M50 75 L53 90 M50 75 L47 90" stroke="{COLORS['emerald_dark']}" stroke-width="2.5" stroke-linecap="square"/>
        </g>
        '''
        svg = self.create_svg(size, size, content, background=COLORS['gold'])
        self.save_icon(filename, svg)
        
        # Monochrome gold
        filename = f"rift-icon-monochrome-gold-{size}px.svg"
        content = f'''
        <g transform="translate({center_x - 40*scale}, {center_x - 20*scale}) scale({scale})">
            <path d="M10 30 L90 30" stroke="{COLORS['gold']}" stroke-width="3" stroke-linecap="square"/>
            <path d="M15 60 L85 60" stroke="{COLORS['gold']}" stroke-width="3" stroke-linecap="square"/>
            <path d="M20 90 L80 90" stroke="{COLORS['gold']}" stroke-width="3" stroke-linecap="square"/>
            <path d="M25 15 L28 30 M75 15 L72 30" stroke="{COLORS['gold']}" stroke-width="2.5" stroke-linecap="square"/>
            <path d="M30 45 L33 60 M70 45 L67 60" stroke="{COLORS['gold']}" stroke-width="2.5" stroke-linecap="square"/>
            <path d="M50 75 L53 90 M50 75 L47 90" stroke="{COLORS['gold']}" stroke-width="2.5" stroke-linecap="square"/>
        </g>
        '''
        svg = self.create_svg(size, size, content, background=None)
        self.save_icon(filename, svg)
        
        # Monochrome emerald
        filename = f"rift-icon-monochrome-emerald-{size}px.svg"
        content = f'''
        <g transform="translate({center_x - 40*scale}, {center_x - 20*scale}) scale({scale})">
            <path d="M10 30 L90 30" stroke="{COLORS['emerald_dark']}" stroke-width="3" stroke-linecap="square"/>
            <path d="M15 60 L85 60" stroke="{COLORS['emerald_dark']}" stroke-width="3" stroke-linecap="square"/>
            <path d="M20 90 L80 90" stroke="{COLORS['emerald_dark']}" stroke-width="3" stroke-linecap="square"/>
            <path d="M25 15 L28 30 M75 15 L72 30" stroke="{COLORS['emerald_dark']}" stroke-width="2.5" stroke-linecap="square"/>
            <path d="M30 45 L33 60 M70 45 L67 60" stroke="{COLORS['emerald_dark']}" stroke-width="2.5" stroke-linecap="square"/>
            <path d="M50 75 L53 90 M50 75 L47 90" stroke="{COLORS['emerald_dark']}" stroke-width="2.5" stroke-linecap="square"/>
        </g>
        '''
        svg = self.create_svg(size, size, content, background=None)
        self.save_icon(filename, svg)
        
        # Gradient
        filename = f"rift-icon-gradient-{size}px.svg"
        gradient_content = f'''
        <defs>
            <linearGradient id="grad-gold-emerald" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="{COLORS['gold']}"/>
                <stop offset="100%" stop-color="{COLORS['emerald_accent']}"/>
            </linearGradient>
        </defs>
        '''
        content = f'''
        <g transform="translate({center_x - 40*scale}, {center_x - 20*scale}) scale({scale})">
            <path d="M10 30 L90 30" stroke="url(#grad-gold-emerald)" stroke-width="3" stroke-linecap="square"/>
            <path d="M15 60 L85 60" stroke="url(#grad-gold-emerald)" stroke-width="3" stroke-linecap="square"/>
            <path d="M20 90 L80 90" stroke="url(#grad-gold-emerald)" stroke-width="3" stroke-linecap="square"/>
            <path d="M25 15 L28 30 M75 15 L72 30" stroke="url(#grad-gold-emerald)" stroke-width="2.5" stroke-linecap="square"/>
            <path d="M30 45 L33 60 M70 45 L67 60" stroke="url(#grad-gold-emerald)" stroke-width="2.5" stroke-linecap="square"/>
            <path d="M50 75 L53 90 M50 75 L47 90" stroke="url(#grad-gold-emerald)" stroke-width="2.5" stroke-linecap="square"/>
        </g>
        '''
        svg = self.create_svg(size, size, gradient_content + content, background=COLORS['emerald_dark'])
        self.save_icon(filename, svg)
    
    # ===== SIZE OPTIMIZATIONS =====
    
    def generate_size_variations(self, style: str = 'standard'):
        """Generate icons at different sizes optimized for each"""
        sizes = [16, 32, 64, 128, 256]
        
        for size in sizes:
            if style == 'minimal':
                self.generate_minimal_icon(size, COLORS['gold'], COLORS['emerald_dark'])
            elif style == 'standard':
                self.generate_standard_icon(size, COLORS['gold'], COLORS['emerald_dark'])
            elif style == 'enhanced':
                self.generate_enhanced_icon(size, COLORS['gold'], COLORS['emerald_dark'])
            elif style == 'detailed':
                self.generate_detailed_icon(size, COLORS['gold'], COLORS['emerald_dark'])
            elif style == 'bold':
                self.generate_bold_icon(size, COLORS['gold'], COLORS['emerald_dark'])
    
    def generate_all_variations(self):
        """Generate all icon variations"""
        print("\n" + "="*60)
        print("🎨 RIFT Icon Variations Generator")
        print("="*60)
        print(f"📁 Output directory: {self.output_dir}\n")
        
        total = 0
        
        # Complexity variations (standard size 100px)
        print("📝 Generating Complexity Variations...")
        self.generate_minimal_icon(100, COLORS['gold'], COLORS['emerald_dark'])
        self.generate_standard_icon(100, COLORS['gold'], COLORS['emerald_dark'])
        self.generate_enhanced_icon(100, COLORS['gold'], COLORS['emerald_dark'])
        self.generate_detailed_icon(100, COLORS['gold'], COLORS['emerald_dark'])
        self.generate_ornate_icon(100, COLORS['gold'], COLORS['emerald_dark'])
        total += 5
        
        # Style variations (standard size 100px)
        print("\n📝 Generating Style Variations...")
        self.generate_geometric_icon(100, COLORS['gold'], COLORS['emerald_dark'])
        self.generate_organic_icon(100, COLORS['gold'], COLORS['emerald_dark'])
        self.generate_tech_icon(100, COLORS['gold'], COLORS['emerald_dark'])
        self.generate_classic_icon(100, COLORS['gold'], COLORS['emerald_dark'])
        self.generate_bold_icon(100, COLORS['gold'], COLORS['emerald_dark'])
        self.generate_subtle_icon(100, COLORS['gold'], COLORS['emerald_dark'])
        total += 6
        
        # Integration variations (standard size 100px)
        print("\n📝 Generating Integration Variations...")
        self.generate_standalone_icon(100, COLORS['gold'], COLORS['emerald_dark'])
        self.generate_framed_icon(100, COLORS['gold'], COLORS['emerald_dark'])
        self.generate_badge_icon(100, COLORS['gold'], COLORS['emerald_dark'])
        self.generate_square_badge_icon(100, COLORS['gold'], COLORS['emerald_dark'])
        total += 4
        
        # Color variations (standard size 100px)
        print("\n📝 Generating Color Variations...")
        self.generate_color_variations(100)
        total += 4
        
        # Size optimizations (minimal and standard styles)
        print("\n📝 Generating Size Optimizations...")
        self.generate_size_variations('minimal')
        self.generate_size_variations('standard')
        self.generate_size_variations('bold')
        total += 15  # 3 styles × 5 sizes
        
        # Generate preview HTML
        self.generate_preview_html()
        
        print("\n" + "="*60)
        print(f"✅ Generated {total} icon variations!")
        print(f"📁 Files saved to: {self.output_dir}/")
        print(f"🌐 Preview: {os.path.join(self.output_dir, 'preview.html')}")
        print("="*60)
    
    def generate_preview_html(self):
        """Generate HTML preview of all icon variations"""
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RIFT Icon Variations Preview</title>
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
            margin-bottom: 50px;
            font-size: 1.2em;
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
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 25px;
            max-width: 1600px;
            margin: 0 auto 40px;
        }
        .icon-card {
            background: #2a2a2a;
            border: 2px solid #0d4d3f;
            border-radius: 12px;
            padding: 20px;
            transition: transform 0.3s, border-color 0.3s;
            text-align: center;
        }
        .icon-card:hover {
            transform: translateY(-5px);
            border-color: #fbbf24;
        }
        .icon-container {
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
        .icon-container img {
            max-width: 100%;
            max-height: 150px;
            height: auto;
        }
        .icon-name {
            color: #fbbf24;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .icon-size {
            color: #aaa;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <h1>RIFT ICON VARIATIONS</h1>
    <p class="subtitle">Explore Different Icon Styles and Applications</p>
'''
        
        # Get all SVG files
        svg_files = [f for f in os.listdir(self.output_dir) if f.endswith('.svg') and f != 'preview.html']
        svg_files.sort()
        
        # Organize by category
        categories = {
            'Complexity': [f for f in svg_files if any(x in f for x in ['minimal', 'standard', 'enhanced', 'detailed', 'ornate'])],
            'Style': [f for f in svg_files if any(x in f for x in ['geometric', 'organic', 'tech', 'classic', 'bold', 'subtle'])],
            'Integration': [f for f in svg_files if any(x in f for x in ['standalone', 'framed', 'badge'])],
            'Color': [f for f in svg_files if any(x in f for x in ['inverted', 'monochrome', 'gradient'])],
            'Size': [f for f in svg_files if any(x in f for x in ['16px', '32px', '64px', '128px', '256px'])]
        }
        
        for category, files in categories.items():
            if not files:
                continue
            html += f'''
    <div class="category-section">
        <h2 class="category-title">{category}</h2>
        <div class="grid">
'''
            for filename in files:
                name = filename.replace('rift-icon-', '').replace('.svg', '').replace('-', ' ').title()
                html += f'''
            <div class="icon-card">
                <div class="icon-container">
                    <img src="{filename}" alt="{name}">
                </div>
                <div class="icon-name">{name}</div>
            </div>
'''
            html += '''
        </div>
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
    generator = RIFTIconVariationGenerator(output_dir='output/icon-variations')
    generator.generate_all_variations()


if __name__ == '__main__':
    main()
