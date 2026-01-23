#!/usr/bin/env python3
"""
RIFT Extended Press Package Generator
Creates additional variations and content-integrated designs
Supports adding user images/videos to templates
"""

import os
import math
from typing import Dict, List, Tuple, Optional

COLORS = {
    'emerald_dark': '#0d4d3f',
    'emerald_mid': '#0f3d32',
    'emerald_bright': '#065f46',
    'emerald_accent': '#10b981',
    'gold': '#fbbf24',
    'white': '#ffffff',
    'black': '#000000',
    'dark': '#0a1f1a',
}

# Extended slogan variations
SLOGAN_VARIATIONS = [
    "I can, you can, we can\nRide It",
    "Ride It",
    "I can, you can, we can\nRide It",
    "Premium Road Cycling.\nCustom Built.",
    "Ride It\nPremium Road Cycling",
    "Custom Built.\nRide It",
]


class RIFTExtendedPressGenerator:
    """Extended press package with more variations"""
    
    def __init__(self, output_dir: str = 'output/press-package'):
        self.output_dir = output_dir
        self.ensure_output_dirs()
    
    def ensure_output_dirs(self):
        """Create output directories"""
        dirs = [
            f'{self.output_dir}/ads/variations',
            f'{self.output_dir}/banners/variations',
            f'{self.output_dir}/social-media/variations',
        ]
        for d in dirs:
            os.makedirs(d, exist_ok=True)
    
    def create_svg(self, width: int, height: int, content: str, viewbox: str = None) -> str:
        """Create SVG wrapper"""
        if viewbox is None:
            viewbox = f"0 0 {width} {height}"
        return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}" width="{width}" height="{height}">
    {content}
</svg>'''
    
    def save_file(self, filename: str, content: str, subdir: str = ''):
        """Save file"""
        if subdir:
            filepath = os.path.join(self.output_dir, subdir, filename)
        else:
            filepath = os.path.join(self.output_dir, filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Generated: {subdir}/{filename}" if subdir else f"✓ Generated: {filename}")
    
    def get_rift_icon_bike(self, x: float, y: float, scale: float = 1.0) -> str:
        """Rift icon with bike elements"""
        s = scale
        return f'''
        <g transform="translate({x}, {y})">
            <path d="M{10*s} {30*s} L{90*s} {30*s}" stroke="{COLORS['gold']}" stroke-width="{3*s}" stroke-linecap="square"/>
            <path d="M{15*s} {60*s} L{85*s} {60*s}" stroke="{COLORS['gold']}" stroke-width="{3*s}" stroke-linecap="square"/>
            <path d="M{20*s} {90*s} L{80*s} {90*s}" stroke="{COLORS['gold']}" stroke-width="{3*s}" stroke-linecap="square"/>
            <path d="M{25*s} {15*s} L{28*s} {30*s}" stroke="{COLORS['gold']}" stroke-width="{2.5*s}" stroke-linecap="square"/>
            <circle cx="{26.5*s}" cy="{22.5*s}" r="{3*s}" fill="none" stroke="{COLORS['gold']}" stroke-width="{1.5*s}"/>
            <path d="M{30*s} {45*s} L{33*s} {60*s}" stroke="{COLORS['gold']}" stroke-width="{2.5*s}" stroke-linecap="square"/>
            <g transform="translate({31.5*s}, {52.5*s})">
                <circle r="{4*s}" fill="none" stroke="{COLORS['gold']}" stroke-width="{1.5*s}"/>
                <circle r="{2*s}" fill="{COLORS['gold']}"/>
            </g>
            <path d="M{50*s} {75*s} L{53*s} {90*s} M{50*s} {75*s} L{47*s} {90*s}" stroke="{COLORS['gold']}" stroke-width="{2.5*s}" stroke-linecap="square"/>
        </g>
        '''
    
    def get_rift_text(self, x: float, y: float, size: float = 60) -> str:
        """RIFT text"""
        scale = size / 60
        r_path = f'M {x} {y+60*scale} L {x} {y} L {x+25*scale} {y} L {x+30*scale} {y+15*scale} L {x+25*scale} {y+30*scale} L {x} {y+30*scale} M {x+12*scale} {y+30*scale} L {x+30*scale} {y+60*scale}'
        i_path = f'M {x+50*scale} {y} L {x+50*scale} {y+60*scale} M {x+40*scale} {y} L {x+60*scale} {y} M {x+40*scale} {y+60*scale} L {x+60*scale} {y+60*scale}'
        f_path = f'M {x+80*scale} {y+60*scale} L {x+80*scale} {y} L {x+110*scale} {y} M {x+80*scale} {y+28*scale} L {x+105*scale} {y+28*scale}'
        t_path = f'M {x+125*scale} {y} L {x+165*scale} {y} M {x+145*scale} {y} L {x+145*scale} {y+60*scale}'
        return f'''
        <g>
            <path d="{r_path}" stroke="{COLORS['white']}" stroke-width="{8*scale}" fill="none" stroke-linecap="square"/>
            <path d="{i_path}" stroke="{COLORS['white']}" stroke-width="{8*scale}" fill="none" stroke-linecap="square"/>
            <path d="{f_path}" stroke="{COLORS['white']}" stroke-width="{8*scale}" fill="none" stroke-linecap="square"/>
            <path d="{t_path}" stroke="{COLORS['white']}" stroke-width="{8*scale}" fill="none" stroke-linecap="square"/>
        </g>
        '''
    
    def generate_slogan_variations(self):
        """Generate ads with different slogan variations"""
        w, h = 1200, 800
        
        for i, slogan in enumerate(SLOGAN_VARIATIONS):
            lines = slogan.split('\n')
            content = f'''
            <defs>
                <linearGradient id="grad-{i}" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" style="stop-color:{COLORS['dark']};stop-opacity:1" />
                    <stop offset="100%" style="stop-color:{COLORS['emerald_dark']};stop-opacity:1" />
                </linearGradient>
            </defs>
            <rect width="{w}" height="{h}" fill="url(#grad-{i})"/>
            
            {self.get_rift_icon_bike(w/2 - 80, h/2 - 100, 2.5)}
            {self.get_rift_text(w/2 - 70, h/2 - 30, 70)}
            '''
            
            # Add slogan text
            y_offset = h/2 + 100
            for j, line in enumerate(lines):
                font_size = 64 if j == 0 and 'Ride It' in line else 48
                content += f'''
                <text x="{w/2}" y="{y_offset + j*60}" font-family="system-ui, sans-serif" font-size="{font_size}" 
                      font-weight="900" fill="{COLORS['gold']}" text-anchor="middle" letter-spacing="0.15em">
                    {line}
                </text>
                '''
            
            svg = self.create_svg(w, h, content)
            safe_name = slogan.replace('\n', '-').replace(' ', '-').replace('.', '').lower()[:30]
            self.save_file(f'ad-slogan-{i+1}-{safe_name}.svg', svg, 'ads/variations')
    
    def generate_instagram_carousel_templates(self):
        """Instagram carousel post templates"""
        w, h = 1080, 1080
        
        # Template 1: Logo focus
        content1 = f'''
        <defs>
            <radialGradient id="carousel1" cx="50%" cy="50%" r="70%">
                <stop offset="0%" style="stop-color:{COLORS['emerald_dark']};stop-opacity:1" />
                <stop offset="100%" style="stop-color:{COLORS['dark']};stop-opacity:1" />
            </radialGradient>
        </defs>
        <rect width="{w}" height="{h}" fill="url(#carousel1)"/>
        
        {self.get_rift_icon_bike(w/2 - 60, h/2 - 80, 3.5)}
        {self.get_rift_text(w/2 - 50, h/2 - 20, 90)}
        
        <text x="{w/2}" y="{h/2 + 120}" font-family="system-ui, sans-serif" font-size="52" 
              font-weight="900" fill="{COLORS['gold']}" text-anchor="middle" letter-spacing="0.2em">
            RIDE IT
        </text>
        '''
        svg1 = self.create_svg(w, h, content1)
        self.save_file('instagram-carousel-1-logo.svg', svg1, 'social-media/variations')
        
        # Template 2: Slogan focus
        content2 = f'''
        <rect width="{w}" height="{h}" fill="{COLORS['dark']}"/>
        
        <text x="{w/2}" y="{h/2 - 60}" font-family="system-ui, sans-serif" font-size="42" 
              font-weight="700" fill="{COLORS['white']}" text-anchor="middle" opacity="0.9">
            I can, you can, we can
        </text>
        <text x="{w/2}" y="{h/2 + 40}" font-family="system-ui, sans-serif" font-size="96" 
              font-weight="900" fill="{COLORS['gold']}" text-anchor="middle" letter-spacing="0.25em">
            RIDE IT
        </text>
        
        {self.get_rift_icon_bike(w - 120, 40, 1.2)}
        '''
        svg2 = self.create_svg(w, h, content2)
        self.save_file('instagram-carousel-2-slogan.svg', svg2, 'social-media/variations')
    
    def generate_banner_variations(self):
        """Various banner designs"""
        w, h = 1920, 400
        
        # Wide banner 1: Minimal
        content1 = f'''
        <rect width="{w}" height="{h}" fill="{COLORS['dark']}"/>
        {self.get_rift_icon_bike(50, h/2 - 40, 2.0)}
        {self.get_rift_text(200, h/2 - 30, 60)}
        <text x="{w - 300}" y="{h/2 + 20}" font-family="system-ui, sans-serif" font-size="48" 
              font-weight="900" fill="{COLORS['gold']}" text-anchor="end" letter-spacing="0.2em">
            RIDE IT
        </text>
        '''
        svg1 = self.create_svg(w, h, content1)
        self.save_file('banner-wide-minimal.svg', svg1, 'banners/variations')
        
        # Wide banner 2: Full slogan
        content2 = f'''
        <defs>
            <linearGradient id="banner2" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:{COLORS['emerald_dark']};stop-opacity:1" />
                <stop offset="100%" style="stop-color:{COLORS['dark']};stop-opacity:1" />
            </linearGradient>
        </defs>
        <rect width="{w}" height="{h}" fill="url(#banner2)"/>
        
        {self.get_rift_icon_bike(100, h/2 - 50, 2.5)}
        {self.get_rift_text(300, h/2 - 30, 70)}
        
        <text x="{w/2 + 200}" y="{h/2 - 20}" font-family="system-ui, sans-serif" font-size="36" 
              font-weight="700" fill="{COLORS['white']}" text-anchor="start">
            I can, you can, we can
        </text>
        <text x="{w/2 + 200}" y="{h/2 + 40}" font-family="system-ui, sans-serif" font-size="56" 
              font-weight="900" fill="{COLORS['gold']}" text-anchor="start" letter-spacing="0.2em">
            RIDE IT
        </text>
        '''
        svg2 = self.create_svg(w, h, content2)
        self.save_file('banner-wide-full-slogan.svg', svg2, 'banners/variations')
    
    def generate_all(self):
        """Generate all extended designs"""
        print("\n🎨 RIFT Extended Press Package Generator")
        print("=" * 60)
        
        print("\n📢 Generating Slogan Variations...")
        self.generate_slogan_variations()
        
        print("\n📱 Generating Instagram Carousel Templates...")
        self.generate_instagram_carousel_templates()
        
        print("\n🎴 Generating Banner Variations...")
        self.generate_banner_variations()
        
        print("\n" + "=" * 60)
        print("✅ Extended designs complete!")


if __name__ == '__main__':
    generator = RIFTExtendedPressGenerator()
    generator.generate_all()
