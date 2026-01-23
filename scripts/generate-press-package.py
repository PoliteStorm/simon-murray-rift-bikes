#!/usr/bin/env python3
"""
RIFT Press Package Generator
Comprehensive system for generating marketing assets:
- Enhanced logos with bike/cog elements in rift
- Social media banners (Twitter, Facebook, Instagram)
- Ad designs with slogan variations
- Overlay images and frame templates
- Video frame templates

Author: Marketing Team
License: MIT
"""

import os
import math
from typing import Dict, List, Tuple, Optional

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

# Slogan Variations
SLOGANS = {
    'primary': "I can, you can, we can\nRide It",
    'short': "Ride It",
    'full': "I can, you can, we can\nRide It",
    'tagline': "Premium Road Cycling. Custom Built.",
}

# Social Media Dimensions (in pixels)
SOCIAL_DIMENSIONS = {
    'twitter_banner': (1500, 500),
    'facebook_cover': (1200, 630),
    'facebook_post': (1200, 1200),
    'instagram_post': (1080, 1080),
    'instagram_story': (1080, 1920),
    'instagram_reel': (1080, 1920),
    'youtube_thumbnail': (1280, 720),
    'linkedin_banner': (1584, 396),
}


class RIFTPressPackageGenerator:
    """Generates comprehensive press package assets"""
    
    def __init__(self, output_dir: str = 'output/press-package'):
        self.output_dir = output_dir
        self.ensure_output_dirs()
    
    def ensure_output_dirs(self):
        """Create all necessary output directories"""
        dirs = [
            self.output_dir,
            f'{self.output_dir}/logos',
            f'{self.output_dir}/logos/bike-rift',
            f'{self.output_dir}/social-media',
            f'{self.output_dir}/social-media/twitter',
            f'{self.output_dir}/social-media/facebook',
            f'{self.output_dir}/social-media/instagram',
            f'{self.output_dir}/ads',
            f'{self.output_dir}/overlays',
            f'{self.output_dir}/frames',
            f'{self.output_dir}/banners',
        ]
        for d in dirs:
            os.makedirs(d, exist_ok=True)
    
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
    
    def save_file(self, filename: str, content: str, subdir: str = ''):
        """Save content to file"""
        if subdir:
            filepath = os.path.join(self.output_dir, subdir, filename)
        else:
            filepath = os.path.join(self.output_dir, filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Generated: {subdir}/{filename}" if subdir else f"✓ Generated: {filename}")
    
    # ===== ENHANCED RIFT ICON WITH BIKE/COG ELEMENTS =====
    
    def get_rift_icon_with_bike_elements(self, x: float, y: float, scale: float = 1.0, 
                                        color: str = COLORS['gold']) -> str:
        """Generate rift icon with bike/cog elements integrated into the crack (zip-like)"""
        s = scale
        # Main horizontal rift lines
        main_lines = f'''
        <path d="M{x+10*s} {y+30*s} L{x+90*s} {y+30*s}" stroke="{color}" stroke-width="{3*s}" stroke-linecap="square"/>
        <path d="M{x+15*s} {y+60*s} L{x+85*s} {y+60*s}" stroke="{color}" stroke-width="{3*s}" stroke-linecap="square"/>
        <path d="M{x+20*s} {y+90*s} L{x+80*s} {y+90*s}" stroke="{color}" stroke-width="{3*s}" stroke-linecap="square"/>
        '''
        
        # Zip-like crack with bike chain/cog elements
        # Top crack with chain links
        top_crack = f'''
        <!-- Top crack with chain elements -->
        <path d="M{x+25*s} {y+15*s} L{x+28*s} {y+30*s}" stroke="{color}" stroke-width="{2.5*s}" stroke-linecap="square"/>
        <path d="M{x+75*s} {y+15*s} L{x+72*s} {y+30*s}" stroke="{color}" stroke-width="{2.5*s}" stroke-linecap="square"/>
        <!-- Chain link in top crack -->
        <circle cx="{x+26.5*s}" cy="{y+22.5*s}" r="{3*s}" fill="none" stroke="{color}" stroke-width="{1.5*s}"/>
        <circle cx="{x+73.5*s}" cy="{y+22.5*s}" r="{3*s}" fill="none" stroke="{color}" stroke-width="{1.5*s}"/>
        '''
        
        # Middle crack with cog/gear elements
        middle_crack = f'''
        <!-- Middle crack with cog elements -->
        <path d="M{x+30*s} {y+45*s} L{x+33*s} {y+60*s}" stroke="{color}" stroke-width="{2.5*s}" stroke-linecap="square"/>
        <path d="M{x+70*s} {y+45*s} L{x+67*s} {y+60*s}" stroke="{color}" stroke-width="{2.5*s}" stroke-linecap="square"/>
        <!-- Cog/gear in middle crack -->
        <g transform="translate({x+31.5*s}, {y+52.5*s})">
            <circle r="{4*s}" fill="none" stroke="{color}" stroke-width="{1.5*s}"/>
            <circle r="{2*s}" fill="{color}"/>
            <!-- Gear teeth -->
            <path d="M{-4*s} 0 L{-5.5*s} {-1.5*s} M{4*s} 0 L{5.5*s} {-1.5*s}" stroke="{color}" stroke-width="{1.2*s}" stroke-linecap="round"/>
            <path d="M0 {-4*s} L{-1.5*s} {-5.5*s} M0 {4*s} L{1.5*s} {5.5*s}" stroke="{color}" stroke-width="{1.2*s}" stroke-linecap="round"/>
        </g>
        <g transform="translate({x+68.5*s}, {y+52.5*s})">
            <circle r="{4*s}" fill="none" stroke="{color}" stroke-width="{1.5*s}"/>
            <circle r="{2*s}" fill="{color}"/>
            <path d="M{-4*s} 0 L{-5.5*s} {-1.5*s} M{4*s} 0 L{5.5*s} {-1.5*s}" stroke="{color}" stroke-width="{1.2*s}" stroke-linecap="round"/>
            <path d="M0 {-4*s} L{-1.5*s} {-5.5*s} M0 {4*s} L{1.5*s} {5.5*s}" stroke="{color}" stroke-width="{1.2*s}" stroke-linecap="round"/>
        </g>
        '''
        
        # Bottom crack with bike chain
        bottom_crack = f'''
        <!-- Bottom crack with bike chain -->
        <path d="M{x+50*s} {y+75*s} L{x+53*s} {y+90*s}" stroke="{color}" stroke-width="{2.5*s}" stroke-linecap="square"/>
        <path d="M{x+50*s} {y+75*s} L{x+47*s} {y+90*s}" stroke="{color}" stroke-width="{2.5*s}" stroke-linecap="square"/>
        <!-- Chain links in bottom crack -->
        <g transform="translate({x+51.5*s}, {y+82.5*s})">
            <rect x="{-3*s}" y="{-2*s}" width="{6*s}" height="{4*s}" rx="{1*s}" fill="none" stroke="{color}" stroke-width="{1.5*s}"/>
            <circle cx="{-3.5*s}" cy="0" r="{1.5*s}" fill="none" stroke="{color}" stroke-width="{1.2*s}"/>
            <circle cx="{3.5*s}" cy="0" r="{1.5*s}" fill="none" stroke="{color}" stroke-width="{1.2*s}"/>
        </g>
        '''
        
        # Additional zip-like detail lines
        detail_lines = f'''
        <path d="M{x+16*s} {y+10*s} L{x+18*s} {y+14*s}" stroke="{color}" stroke-width="{1.5*s}" stroke-linecap="square" opacity="0.7"/>
        <path d="M{x+32*s} {y+10*s} L{x+30*s} {y+14*s}" stroke="{color}" stroke-width="{1.5*s}" stroke-linecap="square" opacity="0.7"/>
        '''
        
        return f'''
        <g>
            {main_lines}
            {top_crack}
            {middle_crack}
            {bottom_crack}
            {detail_lines}
        </g>
        '''
    
    def get_rift_text(self, x: float, y: float, size: float = 60, 
                     color: str = COLORS['white'], style: str = 'bold') -> str:
        """Generate RIFT text with various styles"""
        scale = size / 60
        stroke_width = 8 if style == 'bold' else 6
        
        # Geometric letterforms
        r_path = f'''
            M {x + 0*scale} {y + 60*scale} L {x + 0*scale} {y + 0*scale}
            L {x + 25*scale} {y + 0*scale} L {x + 30*scale} {y + 15*scale}
            L {x + 25*scale} {y + 30*scale} L {x + 0*scale} {y + 30*scale}
            M {x + 12*scale} {y + 30*scale} L {x + 30*scale} {y + 60*scale}
        '''
        i_path = f'''
            M {x + 50*scale} {y + 0*scale} L {x + 50*scale} {y + 60*scale}
            M {x + 40*scale} {y + 0*scale} L {x + 60*scale} {y + 0*scale}
            M {x + 40*scale} {y + 60*scale} L {x + 60*scale} {y + 60*scale}
        '''
        f_path = f'''
            M {x + 80*scale} {y + 60*scale} L {x + 80*scale} {y + 0*scale}
            L {x + 110*scale} {y + 0*scale}
            M {x + 80*scale} {y + 28*scale} L {x + 105*scale} {y + 28*scale}
        '''
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
    
    # ===== ENHANCED LOGOS WITH BIKE RIFT =====
    
    def logo_bike_rift_horizontal(self):
        """Horizontal logo with bike elements in rift"""
        icon = self.get_rift_icon_with_bike_elements(20, 20, 1.0)
        text = self.get_rift_text(120, 30, 50)
        content = f'''
        {icon}
        {text}
        '''
        svg = self.create_svg(400, 120, content)
        self.save_file('rift-logo-bike-rift-horizontal.svg', svg, 'logos/bike-rift')
    
    def logo_bike_rift_vertical(self):
        """Vertical stacked logo with bike elements"""
        icon = self.get_rift_icon_with_bike_elements(50, 20, 1.2)
        text = self.get_rift_text(80, 100, 45)
        content = f'''
        {icon}
        {text}
        '''
        svg = self.create_svg(200, 200, content)
        self.save_file('rift-logo-bike-rift-vertical.svg', svg, 'logos/bike-rift')
    
    def logo_bike_rift_icon_only(self):
        """Icon only with bike elements"""
        icon = self.get_rift_icon_with_bike_elements(10, 10, 1.5)
        content = f'''
        {icon}
        '''
        svg = self.create_svg(120, 120, content)
        self.save_file('rift-logo-bike-rift-icon-only.svg', svg, 'logos/bike-rift')
    
    def logo_bike_rift_with_slogan(self):
        """Logo with 'Ride It' slogan"""
        icon = self.get_rift_icon_with_bike_elements(20, 20, 1.0)
        text = self.get_rift_text(120, 30, 50)
        slogan = f'''
        <text x="120" y="100" font-family="system-ui, sans-serif" font-size="24" 
              font-weight="700" fill="{COLORS['gold']}" letter-spacing="0.1em">
            RIDE IT
        </text>
        '''
        content = f'''
        {icon}
        {text}
        {slogan}
        '''
        svg = self.create_svg(400, 140, content)
        self.save_file('rift-logo-bike-rift-with-slogan.svg', svg, 'logos/bike-rift')
    
    # ===== SOCIAL MEDIA BANNERS =====
    
    def generate_twitter_banner(self):
        """Twitter banner (1500x500)"""
        w, h = SOCIAL_DIMENSIONS['twitter_banner']
        # Background gradient
        bg = f'''
        <defs>
            <linearGradient id="bg-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:{COLORS['dark']};stop-opacity:1" />
                <stop offset="100%" style="stop-color:{COLORS['emerald_dark']};stop-opacity:1" />
            </linearGradient>
        </defs>
        <rect width="{w}" height="{h}" fill="url(#bg-gradient)"/>
        '''
        
        # Logo centered
        icon = self.get_rift_icon_with_bike_elements(w/2 - 100, h/2 - 40, 2.0)
        text = self.get_rift_text(w/2 - 50, h/2 - 20, 60)
        
        # Slogan
        slogan = f'''
        <text x="{w/2}" y="{h/2 + 80}" font-family="system-ui, sans-serif" font-size="36" 
              font-weight="900" fill="{COLORS['gold']}" text-anchor="middle" letter-spacing="0.15em">
            RIDE IT
        </text>
        <text x="{w/2}" y="{h/2 + 120}" font-family="system-ui, sans-serif" font-size="20" 
              fill="{COLORS['white']}" text-anchor="middle" opacity="0.9">
            Premium Road Cycling. Custom Built.
        </text>
        '''
        
        content = f'''
        {bg}
        {icon}
        {text}
        {slogan}
        '''
        svg = self.create_svg(w, h, content, background=None)
        self.save_file('twitter-banner.svg', svg, 'social-media/twitter')
    
    def generate_facebook_cover(self):
        """Facebook cover (1200x630)"""
        w, h = SOCIAL_DIMENSIONS['facebook_cover']
        bg = f'''
        <defs>
            <linearGradient id="fb-bg" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:{COLORS['dark']};stop-opacity:1" />
                <stop offset="100%" style="stop-color:{COLORS['emerald_dark']};stop-opacity:1" />
            </linearGradient>
        </defs>
        <rect width="{w}" height="{h}" fill="url(#fb-bg)"/>
        '''
        
        icon = self.get_rift_icon_with_bike_elements(50, h/2 - 60, 2.5)
        text = self.get_rift_text(200, h/2 - 30, 70)
        
        slogan = f'''
        <text x="200" y="{h/2 + 80}" font-family="system-ui, sans-serif" font-size="32" 
              font-weight="900" fill="{COLORS['gold']}" letter-spacing="0.1em">
            RIDE IT
        </text>
        <text x="200" y="{h/2 + 115}" font-family="system-ui, sans-serif" font-size="18" 
              fill="{COLORS['white']}" opacity="0.9">
            Premium Road Cycling. Custom Built.
        </text>
        '''
        
        content = f'''
        {bg}
        {icon}
        {text}
        {slogan}
        '''
        svg = self.create_svg(w, h, content, background=None)
        self.save_file('facebook-cover.svg', svg, 'social-media/facebook')
    
    def generate_instagram_post(self):
        """Instagram square post (1080x1080)"""
        w, h = SOCIAL_DIMENSIONS['instagram_post']
        bg = f'''
        <defs>
            <radialGradient id="ig-bg" cx="50%" cy="50%" r="70%">
                <stop offset="0%" style="stop-color:{COLORS['emerald_dark']};stop-opacity:1" />
                <stop offset="100%" style="stop-color:{COLORS['dark']};stop-opacity:1" />
            </radialGradient>
        </defs>
        <rect width="{w}" height="{h}" fill="url(#ig-bg)"/>
        '''
        
        icon = self.get_rift_icon_with_bike_elements(w/2 - 80, h/2 - 100, 3.0)
        text = self.get_rift_text(w/2 - 70, h/2 - 20, 80)
        
        slogan = f'''
        <text x="{w/2}" y="{h/2 + 120}" font-family="system-ui, sans-serif" font-size="42" 
              font-weight="900" fill="{COLORS['gold']}" text-anchor="middle" letter-spacing="0.15em">
            RIDE IT
        </text>
        '''
        
        content = f'''
        {bg}
        {icon}
        {text}
        {slogan}
        '''
        svg = self.create_svg(w, h, content, background=None)
        self.save_file('instagram-post.svg', svg, 'social-media/instagram')
    
    def generate_instagram_story(self):
        """Instagram story (1080x1920)"""
        w, h = SOCIAL_DIMENSIONS['instagram_story']
        bg = f'''
        <defs>
            <linearGradient id="story-bg" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" style="stop-color:{COLORS['emerald_dark']};stop-opacity:1" />
                <stop offset="100%" style="stop-color:{COLORS['dark']};stop-opacity:1" />
            </linearGradient>
        </defs>
        <rect width="{w}" height="{h}" fill="url(#story-bg)"/>
        '''
        
        icon = self.get_rift_icon_with_bike_elements(w/2 - 60, h/3 - 50, 2.5)
        text = self.get_rift_text(w/2 - 50, h/3 + 20, 70)
        
        slogan = f'''
        <text x="{w/2}" y="{h/2 + 40}" font-family="system-ui, sans-serif" font-size="48" 
              font-weight="900" fill="{COLORS['gold']}" text-anchor="middle" letter-spacing="0.15em">
            RIDE IT
        </text>
        <text x="{w/2}" y="{h/2 + 100}" font-family="system-ui, sans-serif" font-size="24" 
              fill="{COLORS['white']}" text-anchor="middle" opacity="0.9">
            I can, you can, we can
        </text>
        '''
        
        content = f'''
        {bg}
        {icon}
        {text}
        {slogan}
        '''
        svg = self.create_svg(w, h, content, background=None)
        self.save_file('instagram-story.svg', svg, 'social-media/instagram')
    
    # ===== AD DESIGNS WITH SLOGANS =====
    
    def generate_ad_full_slogan(self):
        """Full slogan ad design"""
        w, h = 1200, 800
        bg = f'''
        <defs>
            <linearGradient id="ad-bg" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:{COLORS['dark']};stop-opacity:1" />
                <stop offset="100%" style="stop-color:{COLORS['emerald_dark']};stop-opacity:1" />
            </linearGradient>
        </defs>
        <rect width="{w}" height="{h}" fill="url(#ad-bg)"/>
        '''
        
        icon = self.get_rift_icon_with_bike_elements(w/2 - 100, 150, 3.0)
        text = self.get_rift_text(w/2 - 80, 250, 90)
        
        slogan = f'''
        <text x="{w/2}" y="450" font-family="system-ui, sans-serif" font-size="56" 
              font-weight="900" fill="{COLORS['gold']}" text-anchor="middle" letter-spacing="0.1em">
            I can, you can, we can
        </text>
        <text x="{w/2}" y="520" font-family="system-ui, sans-serif" font-size="72" 
              font-weight="900" fill="{COLORS['gold']}" text-anchor="middle" letter-spacing="0.2em">
            RIDE IT
        </text>
        <text x="{w/2}" y="650" font-family="system-ui, sans-serif" font-size="24" 
              fill="{COLORS['white']}" text-anchor="middle" opacity="0.9">
            Premium Road Cycling. Custom Built.
        </text>
        '''
        
        content = f'''
        {bg}
        {icon}
        {text}
        {slogan}
        '''
        svg = self.create_svg(w, h, content, background=None)
        self.save_file('ad-full-slogan.svg', svg, 'ads')
    
    def generate_ad_ride_it_only(self):
        """Simple 'Ride It' ad"""
        w, h = 1200, 800
        bg = f'''
        <defs>
            <radialGradient id="ride-bg" cx="50%" cy="50%" r="60%">
                <stop offset="0%" style="stop-color:{COLORS['emerald_dark']};stop-opacity:1" />
                <stop offset="100%" style="stop-color:{COLORS['dark']};stop-opacity:1" />
            </radialGradient>
        </defs>
        <rect width="{w}" height="{h}" fill="url(#ride-bg)"/>
        '''
        
        icon = self.get_rift_icon_with_bike_elements(w/2 - 80, h/2 - 120, 3.5)
        text = self.get_rift_text(w/2 - 70, h/2 - 30, 100)
        
        slogan = f'''
        <text x="{w/2}" y="{h/2 + 150}" font-family="system-ui, sans-serif" font-size="96" 
              font-weight="900" fill="{COLORS['gold']}" text-anchor="middle" letter-spacing="0.25em">
            RIDE IT
        </text>
        '''
        
        content = f'''
        {bg}
        {icon}
        {text}
        {slogan}
        '''
        svg = self.create_svg(w, h, content, background=None)
        self.save_file('ad-ride-it-only.svg', svg, 'ads')
    
    # ===== OVERLAY IMAGES =====
    
    def generate_video_overlay(self):
        """Overlay for video content"""
        w, h = 1920, 1080
        # Transparent background with logo watermark
        icon = self.get_rift_icon_with_bike_elements(w - 200, 50, 1.5)
        text = self.get_rift_text(w - 180, 80, 40)
        
        # Slogan overlay (bottom)
        slogan = f'''
        <text x="{w/2}" y="{h - 100}" font-family="system-ui, sans-serif" font-size="48" 
              font-weight="900" fill="{COLORS['gold']}" text-anchor="middle" letter-spacing="0.15em" 
              opacity="0.95">
            RIDE IT
        </text>
        '''
        
        content = f'''
        {icon}
        {text}
        {slogan}
        '''
        svg = self.create_svg(w, h, content)
        self.save_file('video-overlay.svg', svg, 'overlays')
    
    # ===== FRAME TEMPLATES =====
    
    def generate_frame_template(self):
        """Frame template for ads"""
        w, h = 1200, 800
        # Frame border
        frame = f'''
        <rect x="0" y="0" width="{w}" height="{h}" fill="none" stroke="{COLORS['gold']}" stroke-width="8"/>
        <rect x="20" y="20" width="{w-40}" height="{h-40}" fill="none" stroke="{COLORS['emerald_accent']}" stroke-width="4" opacity="0.5"/>
        '''
        
        # Corner decorations
        corners = f'''
        <path d="M 0 0 L 60 0 M 0 0 L 0 60" stroke="{COLORS['gold']}" stroke-width="6" stroke-linecap="round"/>
        <path d="M {w} 0 L {w-60} 0 M {w} 0 L {w} 60" stroke="{COLORS['gold']}" stroke-width="6" stroke-linecap="round"/>
        <path d="M 0 {h} L 60 {h} M 0 {h} L 0 {h-60}" stroke="{COLORS['gold']}" stroke-width="6" stroke-linecap="round"/>
        <path d="M {w} {h} L {w-60} {h} M {w} {h} L {w} {h-60}" stroke="{COLORS['gold']}" stroke-width="6" stroke-linecap="round"/>
        '''
        
        # Logo in corner
        icon = self.get_rift_icon_with_bike_elements(40, 40, 1.0)
        
        content = f'''
        {frame}
        {corners}
        {icon}
        '''
        svg = self.create_svg(w, h, content)
        self.save_file('frame-template.svg', svg, 'frames')
    
    # ===== GENERATE ALL =====
    
    def generate_all(self):
        """Generate all press package assets"""
        print("\n🎨 RIFT Press Package Generator")
        print("=" * 60)
        print(f"Output directory: {self.output_dir}\n")
        
        print("📐 Generating Enhanced Logos with Bike Rift...")
        self.logo_bike_rift_horizontal()
        self.logo_bike_rift_vertical()
        self.logo_bike_rift_icon_only()
        self.logo_bike_rift_with_slogan()
        
        print("\n📱 Generating Social Media Assets...")
        self.generate_twitter_banner()
        self.generate_facebook_cover()
        self.generate_instagram_post()
        self.generate_instagram_story()
        
        print("\n📢 Generating Ad Designs...")
        self.generate_ad_full_slogan()
        self.generate_ad_ride_it_only()
        
        print("\n🎬 Generating Overlays & Frames...")
        self.generate_video_overlay()
        self.generate_frame_template()
        
        print("\n" + "=" * 60)
        print("✅ Press package generation complete!")
        print(f"📁 All assets saved to: {self.output_dir}")
        print("\n📋 Generated Assets:")
        print("  • Enhanced logos with bike/cog elements")
        print("  • Social media banners (Twitter, Facebook, Instagram)")
        print("  • Ad designs with slogan variations")
        print("  • Video overlays and frame templates")


if __name__ == '__main__':
    generator = RIFTPressPackageGenerator()
    generator.generate_all()
