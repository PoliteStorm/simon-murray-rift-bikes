#!/usr/bin/env python3
"""
RIFT Comprehensive Brand Asset Generator
Generates all logo variations, social media assets, banners, overlays, and specialized assets
Based on logo-generation-prompt.md specifications
"""

import os
from typing import Dict, List, Tuple
from pathlib import Path

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

# Tagline options
TAGLINES = [
    "Edge of Biking Technology",
    "Custom Crafted Excellence",
    "Premium Performance"
]


class RIFTBrandAssetGenerator:
    """Comprehensive generator for all RIFT brand assets"""
    
    def __init__(self, output_dir: str = 'output'):
        self.base_output_dir = output_dir
        self.setup_directories()
    
    def setup_directories(self):
        """Create all necessary output directories"""
        dirs = [
            'logos/horizontal',
            'logos/vertical',
            'logos/icon-only',
            'logos/text-only',
            'social-media',
            'banners',
            'overlays',
            'specialized/favicons',
            'specialized/app-icons',
            'specialized/business-cards',
        ]
        for dir_path in dirs:
            os.makedirs(os.path.join(self.base_output_dir, dir_path), exist_ok=True)
    
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
    
    def get_rift_text_geometric(self, x: float, y: float, size: float = 60, 
                                color: str = COLORS['white'], weight: str = 'bold',
                                fill: bool = True) -> str:
        """Generate custom geometric RIFT letterforms as SVG paths"""
        scale = size / 60  # Base size is 60
        stroke_width = 8 if weight == 'bold' else 6
        
        # Custom geometric letterforms for R-I-F-T (as closed paths for filling)
        # R: Closed path
        r_path = f"M {x + 0*scale} {y + 60*scale} L {x + 0*scale} {y + 0*scale} L {x + 25*scale} {y + 0*scale} L {x + 30*scale} {y + 15*scale} L {x + 25*scale} {y + 30*scale} L {x + 0*scale} {y + 30*scale} Z M {x + 12*scale} {y + 30*scale} L {x + 30*scale} {y + 60*scale}"
        
        # I: Vertical line with caps
        i_path = f"M {x + 50*scale} {y + 0*scale} L {x + 50*scale} {y + 60*scale} M {x + 40*scale} {y + 0*scale} L {x + 60*scale} {y + 0*scale} M {x + 40*scale} {y + 60*scale} L {x + 60*scale} {y + 60*scale}"
        
        # F: Vertical with horizontals
        f_path = f"M {x + 80*scale} {y + 60*scale} L {x + 80*scale} {y + 0*scale} L {x + 110*scale} {y + 0*scale} M {x + 80*scale} {y + 28*scale} L {x + 105*scale} {y + 28*scale}"
        
        # T: Horizontal top + vertical
        t_path = f"M {x + 125*scale} {y + 0*scale} L {x + 165*scale} {y + 0*scale} M {x + 145*scale} {y + 0*scale} L {x + 145*scale} {y + 60*scale}"
        
        if fill:
            # Use stroke for letterforms (they're line-based, not filled shapes)
            return f'''<g>
            <path d="{r_path}" fill="none" stroke="{color}" stroke-width="{stroke_width*scale}" stroke-linecap="square" stroke-linejoin="miter"/>
            <path d="{i_path}" fill="none" stroke="{color}" stroke-width="{stroke_width*scale}" stroke-linecap="square"/>
            <path d="{f_path}" fill="none" stroke="{color}" stroke-width="{stroke_width*scale}" stroke-linecap="square"/>
            <path d="{t_path}" fill="none" stroke="{color}" stroke-width="{stroke_width*scale}" stroke-linecap="square"/>
        </g>'''
        else:
            return f'''<g>
            <path d="{r_path}" fill="none" stroke="{color}" stroke-width="{stroke_width*scale}" stroke-linecap="square" stroke-linejoin="miter"/>
            <path d="{i_path}" fill="none" stroke="{color}" stroke-width="{stroke_width*scale}" stroke-linecap="square"/>
            <path d="{f_path}" fill="none" stroke="{color}" stroke-width="{stroke_width*scale}" stroke-linecap="square"/>
            <path d="{t_path}" fill="none" stroke="{color}" stroke-width="{stroke_width*scale}" stroke-linecap="square"/>
        </g>'''
    
    def get_tagline(self, x: float, y: float, size: float = 12, 
                   color: str = COLORS['gold'], text: str = None) -> str:
        """Generate tagline text"""
        tagline = text or TAGLINES[0]
        return f'''
        <text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" 
              fill="{color}" text-anchor="middle" font-weight="300" letter-spacing="2">
            {tagline.upper()}
        </text>
        '''
    
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
    
    def save_asset(self, filepath: str, svg_content: str):
        """Save SVG content to file"""
        full_path = os.path.join(self.base_output_dir, filepath)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"✓ Generated: {filepath}")
    
    # ==================== PRIMARY LOGOS ====================
    
    def logo_horizontal_standard(self):
        """1.1 Horizontal Logo (Standard) - 400×120px"""
        content = f'''
        {self.get_rift_icon(20, 30, 0.8, COLORS['gold'])}
        {self.get_rift_text_geometric(120, 40, 50, COLORS['white'], 'bold')}
        '''
        self.save_asset('logos/horizontal/rift-logo-horizontal-standard.svg',
                       self.create_svg(400, 120, content, background=COLORS['emerald_dark']))
    
    def logo_vertical_stacked(self):
        """1.2 Vertical/Stacked Logo - 200×300px"""
        content = f'''
        {self.get_rift_icon(50, 30, 1.0, COLORS['gold'])}
        {self.get_rift_text_geometric(20, 180, 45, COLORS['white'], 'bold')}
        '''
        self.save_asset('logos/vertical/rift-logo-vertical-stacked.svg',
                       self.create_svg(200, 300, content, background=COLORS['emerald_dark']))
    
    def logo_icon_only(self):
        """1.3 Icon Only - 200×200px"""
        content = self.get_rift_icon(50, 50, 1.0, COLORS['gold'])
        self.save_asset('logos/icon-only/rift-logo-icon-only.svg',
                       self.create_svg(200, 200, content, background=COLORS['emerald_dark']))
    
    def logo_text_only(self):
        """1.4 Text Only - 400×150px"""
        content = self.get_rift_text_geometric(50, 70, 60, COLORS['gold'], 'bold')
        self.save_asset('logos/text-only/rift-logo-text-only.svg',
                       self.create_svg(400, 150, content, background=COLORS['emerald_dark']))
    
    def logo_compact(self):
        """1.5 Compact Logo - 180×60px"""
        content = f'''
        {self.get_rift_icon(10, 15, 0.5, COLORS['gold'])}
        {self.get_rift_text_geometric(60, 25, 35, COLORS['white'], 'bold')}
        '''
        self.save_asset('logos/horizontal/rift-logo-compact.svg',
                       self.create_svg(180, 60, content, background=COLORS['emerald_dark']))
    
    # ==================== SOCIAL MEDIA ASSETS ====================
    
    def social_twitter_banner(self):
        """2.1 Twitter/X Header Banner - 1500×500px"""
        content = f'''
        <rect width="1500" height="500" fill="{COLORS['emerald_dark']}"/>
        <rect x="150" y="50" width="1200" height="400" fill="{COLORS['emerald_mid']}" opacity="0.3"/>
        {self.get_rift_icon(200, 150, 1.5, COLORS['gold'])}
        {self.get_rift_text_geometric(450, 200, 80, COLORS['white'], 'bold')}
        {self.get_tagline(1050, 350, 24, COLORS['gold'])}
        '''
        self.save_asset('social-media/rift-twitter-banner.svg',
                       self.create_svg(1500, 500, content))
    
    def social_facebook_cover(self):
        """2.2 Facebook Cover Photo - 1200×630px"""
        content = f'''
        <rect width="1200" height="630" fill="{COLORS['emerald_dark']}"/>
        <rect x="190" y="159" width="820" height="312" fill="{COLORS['emerald_mid']}" opacity="0.2"/>
        {self.get_rift_icon(300, 200, 1.2, COLORS['gold'])}
        {self.get_rift_text_geometric(550, 280, 70, COLORS['white'], 'bold')}
        {self.get_tagline(850, 450, 20, COLORS['gold'])}
        '''
        self.save_asset('social-media/rift-facebook-cover.svg',
                       self.create_svg(1200, 630, content))
    
    def social_instagram_pfp(self):
        """2.3 Instagram Profile Picture - 400×400px"""
        content = f'''
        <circle cx="200" cy="200" r="200" fill="{COLORS['emerald_dark']}"/>
        <circle cx="200" cy="200" r="160" fill="none" stroke="{COLORS['gold']}" stroke-width="3"/>
        {self.get_rift_icon(150, 150, 1.0, COLORS['gold'])}
        '''
        self.save_asset('social-media/rift-instagram-pfp.svg',
                       self.create_svg(400, 400, content))
    
    def social_linkedin_banner(self):
        """2.4 LinkedIn Company Banner - 1128×191px"""
        content = f'''
        <rect width="1128" height="191" fill="{COLORS['emerald_dark']}"/>
        {self.get_rift_icon(100, 45, 0.8, COLORS['gold'])}
        {self.get_rift_text_geometric(300, 80, 50, COLORS['white'], 'bold')}
        {self.get_tagline(850, 140, 14, COLORS['gold'])}
        '''
        self.save_asset('social-media/rift-linkedin-banner.svg',
                       self.create_svg(1128, 191, content))
    
    def social_youtube_channel_art(self):
        """2.5 YouTube Channel Art - 2560×1440px"""
        content = f'''
        <rect width="2560" height="1440" fill="{COLORS['emerald_dark']}"/>
        <rect x="507" y="508" width="1546" height="423" fill="{COLORS['emerald_mid']}" opacity="0.2"/>
        {self.get_rift_icon(800, 500, 2.5, COLORS['gold'])}
        {self.get_rift_text_geometric(1400, 650, 120, COLORS['white'], 'bold')}
        {self.get_tagline(1773, 850, 36, COLORS['gold'])}
        '''
        self.save_asset('social-media/rift-youtube-channel-art.svg',
                       self.create_svg(2560, 1440, content))
    
    def social_tiktok_pfp(self):
        """2.6 TikTok Profile Picture - 400×400px"""
        content = f'''
        <circle cx="200" cy="200" r="200" fill="{COLORS['emerald_dark']}"/>
        {self.get_rift_icon(150, 150, 1.0, COLORS['gold'])}
        '''
        self.save_asset('social-media/rift-tiktok-pfp.svg',
                       self.create_svg(400, 400, content))
    
    # ==================== PROFILE PICTURES ====================
    
    def pfp_standard(self):
        """3.1 Standard Profile Picture - 400×400px"""
        content = f'''
        <rect width="400" height="400" fill="{COLORS['emerald_dark']}"/>
        {self.get_rift_icon(150, 150, 1.0, COLORS['gold'])}
        '''
        self.save_asset('social-media/rift-pfp-standard.svg',
                       self.create_svg(400, 400, content))
    
    def pfp_premium(self):
        """3.2 Premium Profile Picture - 400×400px"""
        content = f'''
        <rect width="400" height="400" fill="{COLORS['emerald_dark']}"/>
        <rect x="50" y="50" width="300" height="300" fill="none" stroke="{COLORS['gold']}" stroke-width="4"/>
        {self.get_rift_icon(150, 120, 1.0, COLORS['gold'])}
        {self.get_rift_text_geometric(100, 280, 30, COLORS['gold'], 'bold')}
        '''
        self.save_asset('social-media/rift-pfp-premium.svg',
                       self.create_svg(400, 400, content))
    
    def pfp_minimal(self):
        """3.3 Minimal Profile Picture - 400×400px"""
        content = f'''
        <rect width="400" height="400" fill="{COLORS['emerald_dark']}"/>
        {self.get_rift_icon(150, 150, 0.8, COLORS['gold'], stroke_width=2)}
        '''
        self.save_asset('social-media/rift-pfp-minimal.svg',
                       self.create_svg(400, 400, content))
    
    # ==================== BANNERS & HEADERS ====================
    
    def banner_website_header(self):
        """4.1 Website Header Banner - 1920×200px"""
        content = f'''
        {self.get_rift_icon(50, 50, 1.0, COLORS['gold'])}
        {self.get_rift_text_geometric(200, 80, 60, COLORS['white'], 'bold')}
        '''
        self.save_asset('banners/rift-website-header.svg',
                       self.create_svg(1920, 200, content, background=COLORS['emerald_dark']))
    
    def banner_email_header(self):
        """4.2 Email Header Banner - 600×150px"""
        content = f'''
        {self.get_rift_icon(20, 30, 0.7, COLORS['gold'])}
        {self.get_rift_text_geometric(100, 60, 45, COLORS['emerald_dark'], 'bold')}
        '''
        self.save_asset('banners/rift-email-header.svg',
                       self.create_svg(600, 150, content, background=COLORS['white']))
    
    def banner_print(self):
        """4.3 Print Banner - 2400×600px (300 DPI equivalent)"""
        content = f'''
        <rect width="2400" height="600" fill="{COLORS['emerald_dark']}"/>
        {self.get_rift_icon(200, 150, 2.0, COLORS['gold'])}
        {self.get_rift_text_geometric(600, 250, 120, COLORS['white'], 'bold')}
        {self.get_tagline(1800, 450, 32, COLORS['gold'])}
        '''
        self.save_asset('banners/rift-print-banner.svg',
                       self.create_svg(2400, 600, content))
    
    def banner_mobile(self):
        """4.4 Mobile Banner - 750×200px"""
        content = f'''
        {self.get_rift_icon(30, 40, 0.8, COLORS['gold'])}
        {self.get_rift_text_geometric(140, 80, 50, COLORS['white'], 'bold')}
        '''
        self.save_asset('banners/rift-mobile-banner.svg',
                       self.create_svg(750, 200, content, background=COLORS['emerald_dark']))
    
    # ==================== OVERLAY LOGOS ====================
    
    def overlay_video_standard(self):
        """5.1 Video Overlay Logo (Standard) - 300×100px"""
        content = f'''
        <g opacity="0.6">
            {self.get_rift_icon(20, 20, 0.6, COLORS['white'])}
            {self.get_rift_text_geometric(80, 50, 40, COLORS['white'], 'bold')}
        </g>
        '''
        self.save_asset('overlays/rift-video-overlay-standard.svg',
                       self.create_svg(300, 100, content))
    
    def overlay_video_corner(self):
        """5.2 Video Overlay Logo (Corner) - 200×66px"""
        content = f'''
        <g opacity="0.7">
            {self.get_rift_icon(10, 10, 0.4, COLORS['white'])}
            {self.get_rift_text_geometric(50, 33, 30, COLORS['white'], 'bold')}
        </g>
        '''
        self.save_asset('overlays/rift-video-overlay-corner.svg',
                       self.create_svg(200, 66, content))
    
    def overlay_image_watermark(self):
        """5.3 Image Watermark - 150×150px"""
        content = f'''
        <g opacity="0.4">
            {self.get_rift_icon(37.5, 37.5, 0.75, COLORS['black'])}
        </g>
        '''
        self.save_asset('overlays/rift-image-watermark.svg',
                       self.create_svg(150, 150, content))
    
    def overlay_transparent_badge(self):
        """5.4 Transparent Overlay Badge - 200×200px"""
        content = f'''
        <circle cx="100" cy="100" r="90" fill="none" stroke="{COLORS['gold']}" stroke-width="4"/>
        {self.get_rift_icon(50, 50, 1.0, COLORS['gold'])}
        <text x="100" y="170" font-family="Arial, sans-serif" font-size="14" 
              fill="{COLORS['gold']}" text-anchor="middle" font-weight="bold">
            PREMIUM
        </text>
        '''
        self.save_asset('overlays/rift-transparent-badge.svg',
                       self.create_svg(200, 200, content))
    
    # ==================== SPECIALIZED ASSETS ====================
    
    def specialized_favicon(self, size: int = 32):
        """6.1 Favicon - Various sizes"""
        # Simplified icon for small sizes
        scale = size / 32.0
        content = f'''
        <rect width="{size}" height="{size}" fill="{COLORS['emerald_dark']}"/>
        {self.get_rift_icon(size*0.25, size*0.25, scale*0.4, COLORS['gold'], stroke_width=2*scale)}
        '''
        filename = f'rift-favicon-{size}x{size}.svg'
        self.save_asset(f'specialized/favicons/{filename}',
                       self.create_svg(size, size, content))
    
    def specialized_app_icon_ios(self):
        """6.2 App Icon - iOS (1024×1024px)"""
        content = f'''
        <rect width="1024" height="1024" rx="180" fill="{COLORS['emerald_dark']}"/>
        <rect x="100" y="100" width="824" height="824" rx="150" fill="none" stroke="{COLORS['gold']}" stroke-width="8"/>
        {self.get_rift_icon(362, 362, 3.0, COLORS['gold'])}
        {self.get_rift_text_geometric(200, 700, 100, COLORS['gold'], 'bold')}
        '''
        self.save_asset('specialized/app-icons/rift-app-icon-ios.svg',
                       self.create_svg(1024, 1024, content))
    
    def specialized_app_icon_android(self):
        """6.2 App Icon - Android (512×512px)"""
        content = f'''
        <rect width="512" height="512" fill="{COLORS['emerald_dark']}"/>
        <rect x="50" y="50" width="412" height="412" fill="none" stroke="{COLORS['gold']}" stroke-width="4"/>
        {self.get_rift_icon(181, 181, 1.5, COLORS['gold'])}
        {self.get_rift_text_geometric(100, 350, 50, COLORS['gold'], 'bold')}
        '''
        self.save_asset('specialized/app-icons/rift-app-icon-android.svg',
                       self.create_svg(512, 512, content))
    
    def specialized_business_card(self):
        """6.3 Business Card Logo - 300×100px"""
        content = f'''
        {self.get_rift_icon(20, 20, 0.7, COLORS['gold'])}
        {self.get_rift_text_geometric(100, 50, 45, COLORS['emerald_dark'], 'bold')}
        '''
        self.save_asset('specialized/business-cards/rift-business-card-logo.svg',
                       self.create_svg(300, 100, content, background=COLORS['white']))
    
    def specialized_certificate_badge(self):
        """6.4 Certificate Badge - 300×300px"""
        content = f'''
        <circle cx="150" cy="150" r="140" fill="{COLORS['emerald_dark']}" 
                stroke="{COLORS['gold']}" stroke-width="6"/>
        <circle cx="150" cy="150" r="120" fill="none" 
                stroke="{COLORS['gold']}" stroke-width="2"/>
        {self.get_rift_icon(75, 75, 1.0, COLORS['gold'])}
        <text x="150" y="250" font-family="Arial, sans-serif" font-size="16" 
              fill="{COLORS['gold']}" text-anchor="middle" font-weight="bold" letter-spacing="2">
            CERTIFIED
        </text>
        '''
        self.save_asset('specialized/rift-certificate-badge.svg',
                       self.create_svg(300, 300, content))
    
    def specialized_product_label(self):
        """6.5 Product Label Logo - 200×80px"""
        content = f'''
        {self.get_rift_icon(10, 15, 0.5, COLORS['gold'])}
        {self.get_rift_text_geometric(50, 40, 35, COLORS['emerald_dark'], 'bold')}
        '''
        self.save_asset('specialized/rift-product-label.svg',
                       self.create_svg(200, 80, content, background=COLORS['white']))
    
    def specialized_email_signature(self):
        """6.6 Email Signature Logo - 200×60px"""
        content = f'''
        {self.get_rift_icon(10, 10, 0.5, COLORS['emerald_dark'])}
        {self.get_rift_text_geometric(50, 35, 30, COLORS['emerald_dark'], 'bold')}
        '''
        self.save_asset('specialized/rift-email-signature.svg',
                       self.create_svg(200, 60, content, background=COLORS['white']))
    
    def specialized_social_story(self):
        """6.7 Social Media Story Logo - 1080×1920px (vertical)"""
        content = f'''
        <rect width="1080" height="1920" fill="{COLORS['emerald_dark']}"/>
        {self.get_rift_icon(390, 700, 2.0, COLORS['gold'])}
        {self.get_rift_text_geometric(200, 1100, 100, COLORS['white'], 'bold')}
        {self.get_tagline(540, 1400, 28, COLORS['gold'])}
        '''
        self.save_asset('social-media/rift-social-story.svg',
                       self.create_svg(1080, 1920, content))
    
    def specialized_social_post_template(self):
        """6.8 Social Media Post Template - 1080×1080px"""
        content = f'''
        <rect width="1080" height="1080" fill="{COLORS['emerald_dark']}"/>
        <rect x="40" y="40" width="1000" height="1000" fill="none" stroke="{COLORS['gold']}" stroke-width="2" opacity="0.3"/>
        <g opacity="0.15">
            {self.get_rift_icon(400, 400, 2.0, COLORS['gold'])}
            {self.get_rift_text_geometric(200, 600, 100, COLORS['gold'], 'bold')}
        </g>
        '''
        self.save_asset('social-media/rift-social-post-template.svg',
                       self.create_svg(1080, 1080, content))
    
    # ==================== GENERATION METHODS ====================
    
    def generate_primary_logos(self):
        """Generate all primary logo variations"""
        print("\n📐 Generating Primary Logos...")
        self.logo_horizontal_standard()
        self.logo_vertical_stacked()
        self.logo_icon_only()
        self.logo_text_only()
        self.logo_compact()
    
    def generate_social_media(self):
        """Generate all social media assets"""
        print("\n📱 Generating Social Media Assets...")
        self.social_twitter_banner()
        self.social_facebook_cover()
        self.social_instagram_pfp()
        self.social_linkedin_banner()
        self.social_youtube_channel_art()
        self.social_tiktok_pfp()
    
    def generate_profile_pictures(self):
        """Generate all profile picture variations"""
        print("\n👤 Generating Profile Pictures...")
        self.pfp_standard()
        self.pfp_premium()
        self.pfp_minimal()
    
    def generate_banners(self):
        """Generate all banner and header assets"""
        print("\n🚩 Generating Banners & Headers...")
        self.banner_website_header()
        self.banner_email_header()
        self.banner_print()
        self.banner_mobile()
    
    def generate_overlays(self):
        """Generate all overlay and watermark assets"""
        print("\n💧 Generating Overlays & Watermarks...")
        self.overlay_video_standard()
        self.overlay_video_corner()
        self.overlay_image_watermark()
        self.overlay_transparent_badge()
    
    def generate_specialized(self):
        """Generate all specialized assets"""
        print("\n⭐ Generating Specialized Assets...")
        # Favicons in multiple sizes
        for size in [16, 32, 48, 64, 128, 256]:
            self.specialized_favicon(size)
        self.specialized_app_icon_ios()
        self.specialized_app_icon_android()
        self.specialized_business_card()
        self.specialized_certificate_badge()
        self.specialized_product_label()
        self.specialized_email_signature()
        self.specialized_social_story()
        self.specialized_social_post_template()
    
    def generate_all(self):
        """Generate all brand assets"""
        print("\n" + "="*60)
        print("🎨 RIFT Comprehensive Brand Asset Generator")
        print("="*60)
        print(f"📁 Output directory: {self.base_output_dir}\n")
        
        self.generate_primary_logos()
        self.generate_social_media()
        self.generate_profile_pictures()
        self.generate_banners()
        self.generate_overlays()
        self.generate_specialized()
        
        # Generate preview HTML
        self.generate_preview_html()
        
        print("\n" + "="*60)
        print("✅ All brand assets generated successfully!")
        print(f"📁 Files saved to: {self.base_output_dir}/")
        print(f"🌐 Preview: {os.path.join(self.base_output_dir, 'preview.html')}")
        print("="*60)
    
    def generate_preview_html(self):
        """Generate comprehensive HTML preview of all assets"""
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RIFT Brand Assets Preview</title>
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
        .section {
            margin-bottom: 60px;
        }
        .section-title {
            color: #fbbf24;
            font-size: 2em;
            margin-bottom: 30px;
            padding-bottom: 10px;
            border-bottom: 2px solid #0d4d3f;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            max-width: 1600px;
            margin: 0 auto;
        }
        .asset-card {
            background: #2a2a2a;
            border: 2px solid #0d4d3f;
            border-radius: 12px;
            padding: 20px;
            transition: transform 0.3s, border-color 0.3s;
        }
        .asset-card:hover {
            transform: translateY(-5px);
            border-color: #fbbf24;
        }
        .asset-container {
            background: white;
            border-radius: 8px;
            padding: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 150px;
            margin-bottom: 15px;
            overflow: hidden;
        }
        .asset-container img {
            max-width: 100%;
            max-height: 200px;
            height: auto;
        }
        .asset-name {
            color: #fbbf24;
            font-weight: bold;
            margin-bottom: 5px;
            font-size: 1.1em;
        }
        .asset-description {
            color: #aaa;
            font-size: 0.9em;
            margin-bottom: 8px;
        }
        .asset-dimensions {
            color: #10b981;
            font-size: 0.85em;
            font-family: monospace;
        }
    </style>
</head>
<body>
    <h1>RIFT BRAND ASSETS</h1>
    <p class="subtitle">Comprehensive Brand Asset Collection</p>
'''
        
        # Define all assets by category
        assets = {
            'Primary Logos': [
                ('logos/horizontal/rift-logo-horizontal-standard.svg', 'Horizontal Standard', '400×120px', 'Main horizontal logo'),
                ('logos/vertical/rift-logo-vertical-stacked.svg', 'Vertical Stacked', '200×300px', 'Stacked layout'),
                ('logos/icon-only/rift-logo-icon-only.svg', 'Icon Only', '200×200px', 'Icon only version'),
                ('logos/text-only/rift-logo-text-only.svg', 'Text Only', '400×150px', 'Typography only'),
                ('logos/horizontal/rift-logo-compact.svg', 'Compact', '180×60px', 'Small space optimized'),
            ],
            'Social Media': [
                ('social-media/rift-twitter-banner.svg', 'Twitter/X Banner', '1500×500px', 'Profile header'),
                ('social-media/rift-facebook-cover.svg', 'Facebook Cover', '1200×630px', 'Page cover photo'),
                ('social-media/rift-instagram-pfp.svg', 'Instagram PFP', '400×400px', 'Profile picture'),
                ('social-media/rift-linkedin-banner.svg', 'LinkedIn Banner', '1128×191px', 'Company page'),
                ('social-media/rift-youtube-channel-art.svg', 'YouTube Art', '2560×1440px', 'Channel banner'),
                ('social-media/rift-tiktok-pfp.svg', 'TikTok PFP', '400×400px', 'Profile picture'),
            ],
            'Profile Pictures': [
                ('social-media/rift-pfp-standard.svg', 'Standard PFP', '400×400px', 'General use'),
                ('social-media/rift-pfp-premium.svg', 'Premium PFP', '400×400px', 'With text'),
                ('social-media/rift-pfp-minimal.svg', 'Minimal PFP', '400×400px', 'Simplified'),
            ],
            'Banners & Headers': [
                ('banners/rift-website-header.svg', 'Website Header', '1920×200px', 'Full-width header'),
                ('banners/rift-email-header.svg', 'Email Header', '600×150px', 'Email marketing'),
                ('banners/rift-print-banner.svg', 'Print Banner', '2400×600px', 'Print materials'),
                ('banners/rift-mobile-banner.svg', 'Mobile Banner', '750×200px', 'Mobile optimized'),
            ],
            'Overlays & Watermarks': [
                ('overlays/rift-video-overlay-standard.svg', 'Video Overlay', '300×100px', 'Video watermark'),
                ('overlays/rift-video-overlay-corner.svg', 'Corner Overlay', '200×66px', 'Corner placement'),
                ('overlays/rift-image-watermark.svg', 'Image Watermark', '150×150px', 'Photo protection'),
                ('overlays/rift-transparent-badge.svg', 'Transparent Badge', '200×200px', 'Product overlay'),
            ],
            'Specialized Assets': [
                ('specialized/favicons/rift-favicon-32x32.svg', 'Favicon 32px', '32×32px', 'Browser favicon'),
                ('specialized/app-icons/rift-app-icon-ios.svg', 'iOS App Icon', '1024×1024px', 'iOS app store'),
                ('specialized/app-icons/rift-app-icon-android.svg', 'Android Icon', '512×512px', 'Android app'),
                ('specialized/business-cards/rift-business-card-logo.svg', 'Business Card', '300×100px', 'Print ready'),
                ('specialized/rift-certificate-badge.svg', 'Certificate Badge', '300×300px', 'Awards/certificates'),
                ('specialized/rift-product-label.svg', 'Product Label', '200×80px', 'Packaging'),
                ('specialized/rift-email-signature.svg', 'Email Signature', '200×60px', 'Email footer'),
                ('social-media/rift-social-story.svg', 'Social Story', '1080×1920px', 'Instagram/Facebook stories'),
                ('social-media/rift-social-post-template.svg', 'Post Template', '1080×1080px', 'Social media posts'),
            ],
        }
        
        for category, items in assets.items():
            html += f'''
    <div class="section">
        <h2 class="section-title">{category}</h2>
        <div class="grid">
'''
            for filepath, name, dimensions, description in items:
                html += f'''
            <div class="asset-card">
                <div class="asset-container">
                    <img src="{filepath}" alt="{name}" onerror="this.style.display='none'">
                </div>
                <div class="asset-name">{name}</div>
                <div class="asset-description">{description}</div>
                <div class="asset-dimensions">{dimensions}</div>
            </div>
'''
            html += '        </div>\n    </div>\n'
        
        html += '''
</body>
</html>'''
        
        preview_path = os.path.join(self.base_output_dir, 'preview.html')
        with open(preview_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"✓ Generated: preview.html")


def main():
    """Main execution function"""
    generator = RIFTBrandAssetGenerator(output_dir='output/brand-assets')
    generator.generate_all()


if __name__ == '__main__':
    main()
