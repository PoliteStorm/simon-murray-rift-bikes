#!/usr/bin/env python3
"""
RIFT Advanced Press Package Generator
Creates more sophisticated, cutting-edge designs for social media
Includes animated-style static designs, modern layouts, and innovative compositions
"""

import os
import math
from typing import Dict, List, Tuple

# Brand Colors
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

SOCIAL_DIMENSIONS = {
    'twitter_banner': (1500, 500),
    'facebook_cover': (1200, 630),
    'instagram_post': (1080, 1080),
    'instagram_story': (1080, 1920),
}


class RIFTAdvancedPressGenerator:
    """Advanced press package generator with cutting-edge designs"""
    
    def __init__(self, output_dir: str = 'output/press-package'):
        self.output_dir = output_dir
        self.ensure_output_dirs()
    
    def ensure_output_dirs(self):
        """Create output directories"""
        dirs = [
            f'{self.output_dir}/ads/advanced',
            f'{self.output_dir}/social-media/advanced',
            f'{self.output_dir}/banners/premium',
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
    
    def get_rift_icon_advanced(self, x: float, y: float, scale: float = 1.0) -> str:
        """Advanced rift icon with bike elements"""
        s = scale
        return f'''
        <g transform="translate({x}, {y})">
            <!-- Main lines -->
            <path d="M{10*s} {30*s} L{90*s} {30*s}" stroke="{COLORS['gold']}" stroke-width="{3*s}" stroke-linecap="square"/>
            <path d="M{15*s} {60*s} L{85*s} {60*s}" stroke="{COLORS['gold']}" stroke-width="{3*s}" stroke-linecap="square"/>
            <path d="M{20*s} {90*s} L{80*s} {90*s}" stroke="{COLORS['gold']}" stroke-width="{3*s}" stroke-linecap="square"/>
            <!-- Cracks with bike elements -->
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
    
    def get_rift_text_advanced(self, x: float, y: float, size: float = 60) -> str:
        """Advanced RIFT text"""
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
    
    def generate_split_screen_ad(self):
        """Modern split-screen ad design"""
        w, h = 1200, 800
        content = f'''
        <defs>
            <linearGradient id="split-left" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:{COLORS['dark']};stop-opacity:1" />
                <stop offset="100%" style="stop-color:{COLORS['emerald_dark']};stop-opacity:1" />
            </linearGradient>
            <linearGradient id="split-right" x1="0%" y1="0%" x2="100%" y2="0%">
                <stop offset="0%" style="stop-color:{COLORS['emerald_dark']};stop-opacity:1" />
                <stop offset="100%" style="stop-color:{COLORS['dark']};stop-opacity:1" />
            </linearGradient>
        </defs>
        <rect x="0" y="0" width="{w/2}" height="{h}" fill="url(#split-left)"/>
        <rect x="{w/2}" y="0" width="{w/2}" height="{h}" fill="url(#split-right)"/>
        
        <!-- Left side: Logo -->
        {self.get_rift_icon_advanced(w/4 - 50, h/2 - 60, 2.5)}
        {self.get_rift_text_advanced(w/4 - 40, h/2 - 20, 70)}
        
        <!-- Right side: Slogan -->
        <text x="{w*3/4}" y="{h/2 - 40}" font-family="system-ui, sans-serif" font-size="48" 
              font-weight="700" fill="{COLORS['gold']}" text-anchor="middle" letter-spacing="0.1em">
            I can, you can, we can
        </text>
        <text x="{w*3/4}" y="{h/2 + 40}" font-family="system-ui, sans-serif" font-size="72" 
              font-weight="900" fill="{COLORS['gold']}" text-anchor="middle" letter-spacing="0.25em">
            RIDE IT
        </text>
        '''
        svg = self.create_svg(w, h, content)
        self.save_file('ad-split-screen.svg', svg, 'ads/advanced')
    
    def generate_minimal_modern_ad(self):
        """Ultra-minimal modern ad"""
        w, h = 1200, 800
        content = f'''
        <rect width="{w}" height="{h}" fill="{COLORS['dark']}"/>
        
        <!-- Minimal logo top left -->
        {self.get_rift_icon_advanced(50, 50, 1.5)}
        
        <!-- Large slogan center -->
        <text x="{w/2}" y="{h/2}" font-family="system-ui, sans-serif" font-size="120" 
              font-weight="900" fill="{COLORS['gold']}" text-anchor="middle" letter-spacing="0.3em">
            RIDE IT
        </text>
        
        <!-- Subtle tagline -->
        <text x="{w/2}" y="{h/2 + 100}" font-family="system-ui, sans-serif" font-size="20" 
              fill="{COLORS['white']}" text-anchor="middle" opacity="0.6" letter-spacing="0.2em">
            PREMIUM ROAD CYCLING
        </text>
        '''
        svg = self.create_svg(w, h, content)
        self.save_file('ad-minimal-modern.svg', svg, 'ads/advanced')
    
    def generate_instagram_reel_template(self):
        """Instagram Reel template (1080x1920)"""
        w, h = 1080, 1920
        content = f'''
        <defs>
            <linearGradient id="reel-bg" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:{COLORS['emerald_dark']};stop-opacity:1" />
                <stop offset="50%" style="stop-color:{COLORS['dark']};stop-opacity:1" />
                <stop offset="100%" style="stop-color:{COLORS['emerald_dark']};stop-opacity:1" />
            </linearGradient>
        </defs>
        <rect width="{w}" height="{h}" fill="url(#reel-bg)"/>
        
        <!-- Logo top center -->
        {self.get_rift_icon_advanced(w/2 - 50, 100, 2.0)}
        {self.get_rift_text_advanced(w/2 - 40, 180, 50)}
        
        <!-- Slogan center -->
        <text x="{w/2}" y="{h/2}" font-family="system-ui, sans-serif" font-size="64" 
              font-weight="900" fill="{COLORS['gold']}" text-anchor="middle" letter-spacing="0.2em">
            RIDE IT
        </text>
        
        <!-- Full slogan bottom -->
        <text x="{w/2}" y="{h - 300}" font-family="system-ui, sans-serif" font-size="36" 
              font-weight="700" fill="{COLORS['white']}" text-anchor="middle" opacity="0.9">
            I can, you can, we can
        </text>
        <text x="{w/2}" y="{h - 200}" font-family="system-ui, sans-serif" font-size="24" 
              fill="{COLORS['white']}" text-anchor="middle" opacity="0.7">
            Premium Road Cycling. Custom Built.
        </text>
        '''
        svg = self.create_svg(w, h, content)
        self.save_file('instagram-reel-template.svg', svg, 'social-media/advanced')
    
    def generate_all(self):
        """Generate all advanced designs"""
        print("\n🚀 RIFT Advanced Press Package Generator")
        print("=" * 60)
        
        print("\n📐 Generating Advanced Ad Designs...")
        self.generate_split_screen_ad()
        self.generate_minimal_modern_ad()
        
        print("\n📱 Generating Advanced Social Media...")
        self.generate_instagram_reel_template()
        
        print("\n" + "=" * 60)
        print("✅ Advanced designs complete!")


if __name__ == '__main__':
    generator = RIFTAdvancedPressGenerator()
    generator.generate_all()
