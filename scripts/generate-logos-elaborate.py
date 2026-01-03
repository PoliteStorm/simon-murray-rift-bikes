#!/usr/bin/env python3
# generate-logos-elaborate.py
# Highly elaborate SVG logo generator for RIFT

import os
from textwrap import dedent

# -------------------------
# Paths / constants
# -------------------------

OUTPUT_DIR = os.path.join("output", "logos-elaborate")
PREVIEW_HTML = os.path.join(OUTPUT_DIR, "preview.html")

# Brand colors
EMERALD_DARK = "#0d4d3f"
EMERALD_MID = "#0f3d32"
EMERALD_BRIGHT = "#065f46"
EMERALD_ACCENT = "#10b981"
GOLD = "#fbbf24"
WHITE = "#ffffff"

SVG_HEADER = (
    '<svg xmlns="http://www.w3.org/2000/svg" '
    'width="800" height="300" viewBox="0 0 800 300">'
)
SVG_FOOTER = "</svg>"


# -------------------------
# Core helpers
# -------------------------

def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def base_defs():
    """
    Common <defs> shared across multiple logos:
    - Metallic gold & emerald gradients
    - Glow / shadow filters
    - Carbon fiber pattern
    - Brushed metal texture
    - Spotlight gradient
    - Inner-light mask for RIFT word
    - Volcanic rift icon symbol
    """
    return dedent(
        f"""
        <defs>
          <!-- Gold metallic gradient -->
          <linearGradient id="grad-gold-metal" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="{GOLD}" stop-opacity="0.7"/>
            <stop offset="40%" stop-color="#ffe39c" stop-opacity="1"/>
            <stop offset="70%" stop-color="{GOLD}" stop-opacity="1"/>
            <stop offset="100%" stop-color="#ad7a14" stop-opacity="1"/>
          </linearGradient>

          <!-- Emerald depth gradient -->
          <linearGradient id="grad-emerald-depth" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="{EMERALD_BRIGHT}"/>
            <stop offset="50%" stop-color="{EMERALD_MID}"/>
            <stop offset="100%" stop-color="{EMERALD_DARK}"/>
          </linearGradient>

          <!-- Soft glow filter - more subtle -->
          <filter id="soft-glow" x="-40%" y="-40%" width="180%" height="180%">
            <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur"/>
            <feColorMatrix in="blur" type="matrix"
              values="0 0 0 0 1   0 0 0 0 0.85   0 0 0 0 0.3   0 0 0 0.6 0"
              result="colored"/>
            <feMerge>
              <feMergeNode in="colored"/>
              <feMergeNode in="SourceGraphic"/>
            </feMerge>
          </filter>

          <!-- Multi-layer shadow - softer and more blended -->
          <filter id="multi-shadow" x="-40%" y="-40%" width="200%" height="200%">
            <feDropShadow dx="1" dy="1" stdDeviation="1.5"
              flood-color="#000000" flood-opacity="0.3"/>
            <feDropShadow dx="3" dy="3" stdDeviation="3"
              flood-color="#000000" flood-opacity="0.25"/>
            <feDropShadow dx="6" dy="6" stdDeviation="4"
              flood-color="#000000" flood-opacity="0.15"/>
          </filter>

          <!-- Carbon fiber pattern -->
          <pattern id="carbon-fiber" x="0" y="0" width="8" height="8"
                   patternUnits="userSpaceOnUse">
            <rect width="8" height="8" fill="#111"/>
            <path d="M0 4 L4 0 L8 4 L4 8 Z" fill="#222"/>
            <path d="M0 0 L4 4 L0 8 Z" fill="#333"/>
            <path d="M8 0 L4 4 L8 8 Z" fill="#000"/>
          </pattern>

          <!-- Brushed metal texture (to be applied as filter) -->
          <filter id="brushed-metal" x="0" y="0" width="100%" height="100%">
            <feTurbulence type="fractalNoise"
                          baseFrequency="0.8 0"
                          numOctaves="2"
                          result="noise"/>
            <feColorMatrix in="noise" type="matrix"
              values="0 0 0 0 1   0 0 0 0 0.9   0 0 0 0 0.6   0 0 0 1 0"
              result="goldish"/>
            <feComposite in="goldish" in2="SourceGraphic" operator="in"/>
          </filter>

          <!-- Spotlight radial gradient -->
          <radialGradient id="spotlight" cx="50%" cy="10%" r="70%">
            <stop offset="0%" stop-color="#ffffff" stop-opacity="0.9"/>
            <stop offset="35%" stop-color="#ffffff" stop-opacity="0.0"/>
            <stop offset="100%" stop-color="#000000" stop-opacity="0.8"/>
          </radialGradient>

          <!-- Inner light mask for RIFT -->
          <mask id="inner-light-mask">
            <rect width="800" height="300" fill="black"/>
            <text x="140" y="170"
                  font-family="'Orbitron', sans-serif"
                  font-size="130"
                  font-weight="700"
                  fill="white">RIFT</text>
          </mask>

          <!-- Volcanic rift icon symbol -->
          <symbol id="rift-icon" viewBox="0 0 100 110">
            <g stroke="url(#grad-gold-metal)" stroke-linecap="square">
              <!-- Three horizontal lines -->
              <path d="M10 30 L90 30" stroke-width="3"/>
              <path d="M15 60 L85 60" stroke-width="3"/>
              <path d="M20 90 L80 90" stroke-width="3"/>
              <!-- Angular cracks -->
              <path d="M25 15 L28 30 M75 15 L72 30" stroke-width="2.5"/>
              <path d="M30 45 L33 60 M70 45 L67 60" stroke-width="2.5"/>
              <path d="M50 75 L53 90 M50 75 L47 90" stroke-width="2.5"/>
            </g>
          </symbol>
        </defs>
        """
    )


def text_path_RIFT(id_suffix=""):
    """
    Custom geometric RIFT lettering (R, I, F, T) as paths.
    Clean, legible letterforms that clearly spell "RIFT"
    Based on the working horizontal logo design
    """
    return dedent(
        f"""
        <g id="rift-text{id_suffix}" transform="translate(160,80) scale(1.2)">
          <!-- R - Geometric with angular leg -->
          <path d="
            M0 0 L0 100 L18 100
            Q28 100 28 85
            Q28 70 22 60
            Q28 50 28 35
            Q28 20 18 20
            L0 20 Z
            M8 25 L18 25
            Q22 25 22 30
            Q22 35 18 35
            L8 35 Z
            M12 50 L22 80 L12 80 Z
          " fill="url(#grad-emerald-depth)"/>

          <!-- I - Clean with angular top/bottom -->
          <g transform="translate(38, 0)">
            <path d="
              M0 0 L20 0 L20 12 L12 12 L12 88 L20 88 L20 100 L0 100 L0 88 L8 88 L8 12 L0 12 Z
            " fill="url(#grad-emerald-depth)"/>
          </g>

          <!-- F - Angular with geometric cut -->
          <g transform="translate(66, 0)">
            <path d="
              M0 0 L0 100 L20 100 L20 88 L12 88 L12 70 L20 70 L20 58 L12 58 L12 0 Z
            " fill="url(#grad-emerald-depth)"/>
          </g>

          <!-- T - Bold with angular top -->
          <g transform="translate(94, 0)">
            <path d="
              M0 0 L30 0 L30 12 L19 12 L19 100 L13 100 L13 12 L0 12 Z
            " fill="url(#grad-emerald-depth)"/>
          </g>
        </g>
        """
    )


# -------------------------
# Category 1: 3D & Dimensional
# -------------------------

def logo_3d_extruded():
    bg = f'<rect width="800" height="300" fill="{EMERALD_DARK}"/>'

    # Subtle, blended extrusion with smooth gradient
    extrusion_defs = dedent(
        """
        <defs>
          <linearGradient id="extrude-grad" x1="0" y1="0" x2="0.3" y2="0.3">
            <stop offset="0%" stop-color="#021511" stop-opacity="0.8"/>
            <stop offset="100%" stop-color="#021511" stop-opacity="0.3"/>
          </linearGradient>
        </defs>
        """
    )
    
    # Subtle offset for depth - much smaller and smoother
    extrusion = dedent(
        """
        <g transform="translate(162,82) scale(1.2)" fill="url(#extrude-grad)" opacity="0.4">
          <path d="
            M0 0 L0 100 L18 100
            Q28 100 28 85
            Q28 70 22 60
            Q28 50 28 35
            Q28 20 18 20
            L0 20 Z
            M8 25 L18 25
            Q22 25 22 30
            Q22 35 18 35
            L8 35 Z
            M12 50 L22 80 L12 80 Z
          "/>
          <g transform="translate(38, 0)">
            <path d="
              M0 0 L20 0 L20 12 L12 12 L12 88 L20 88 L20 100 L0 100 L0 88 L8 88 L8 12 L0 12 Z
            "/>
          </g>
          <g transform="translate(66, 0)">
            <path d="
              M0 0 L0 100 L20 100 L20 88 L12 88 L12 70 L20 70 L20 58 L12 58 L12 0 Z
            "/>
          </g>
          <g transform="translate(94, 0)">
            <path d="
              M0 0 L30 0 L30 12 L19 12 L19 100 L13 100 L13 12 L0 12 Z
            "/>
          </g>
        </g>
        """
    )

    front = '<g filter="url(#multi-shadow)">' + text_path_RIFT("-3d") + "</g>"
    icon = (
        '<use href="#rift-icon" x="40" y="95" width="80" height="88" '
        'filter="url(#multi-shadow)" opacity="0.9"/>'
    )

    return SVG_HEADER + base_defs() + extrusion_defs + bg + extrusion + front + icon + SVG_FOOTER


def logo_isometric():
    bg = f'<rect width="800" height="300" fill="{EMERALD_MID}"/>'

    # Subtle isometric feel - much less extreme skew
    iso_group = (
        '<g transform="translate(150,70) skewX(-8) scale(1,0.98)">'
        + text_path_RIFT("-iso")
        + "</g>"
    )

    # Softer overlay gradient
    overlay = (
        '<rect x="0" y="200" width="800" height="120" '
        'fill="url(#spotlight)" opacity="0.4"/>'
    )
    icon = '<use href="#rift-icon" x="560" y="80" width="120" height="120" opacity="0.9"/>'

    return SVG_HEADER + base_defs() + bg + iso_group + overlay + icon + SVG_FOOTER


def logo_floating_elements():
    bg = f'<rect width="800" height="300" fill="{EMERALD_DARK}"/>'
    text = '<g filter="url(#multi-shadow)">' + text_path_RIFT("-float") + "</g>"
    icon = (
        '<use href="#rift-icon" x="520" y="70" width="120" height="120" '
        'filter="url(#soft-glow)" opacity="0.95"/>'
    )

    # Softer, more blended shadows with gradient
    shadow_defs = dedent(
        """
        <defs>
          <radialGradient id="float-shadow-grad" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="#000000" stop-opacity="0.5"/>
            <stop offset="100%" stop-color="#000000" stop-opacity="0.0"/>
          </radialGradient>
        </defs>
        """
    )
    
    float_shadows = dedent(
        """
        <ellipse cx="300" cy="250" rx="220" ry="12"
                 fill="url(#float-shadow-grad)"/>
        <ellipse cx="580" cy="235" rx="85"  ry="8"
                 fill="url(#float-shadow-grad)"/>
        """
    )

    return SVG_HEADER + base_defs() + shadow_defs + bg + text + icon + float_shadows + SVG_FOOTER


def logo_layered_depth():
    bg = f'<rect width="800" height="300" fill="{EMERALD_MID}"/>'

    # More subtle, blended layers with smoother transitions
    back_layer = (
        '<g opacity="0.15" transform="translate(5,10) scale(1.02)">'
        + text_path_RIFT("-back")
        + "</g>"
    )
    mid_layer = (
        '<g opacity="0.4" transform="translate(10,15) scale(1.01)">'
        + text_path_RIFT("-mid")
        + "</g>"
    )
    front_layer = (
        '<g filter="url(#multi-shadow)">' + text_path_RIFT("-front") + "</g>"
    )
    icon = '<use href="#rift-icon" x="40" y="25" width="80" height="88" opacity="0.8"/>'

    return (
        SVG_HEADER
        + base_defs()
        + bg
        + back_layer
        + mid_layer
        + front_layer
        + icon
        + SVG_FOOTER
    )


# -------------------------
# Category 2: Ornamental & Decorative
# -------------------------

def logo_art_nouveau():
    bg = f'<rect width="800" height="300" fill="{EMERALD_DARK}"/>'

    vines = dedent(
        f"""
        <g fill="none" stroke="{EMERALD_ACCENT}" stroke-width="2" opacity="0.9">
          <path d="M40 260 C120 200 80 120 180 80 S320 40 380 110"/>
          <path d="M760 40 C660 80 640 140 520 160 S420 240 360 260"/>
          <path d="M120 40 C160 80 150 130 200 160 S260 210 260 260"/>
          <circle cx="200" cy="160" r="6" fill="{GOLD}"/>
          <circle cx="520" cy="160" r="6" fill="{GOLD}"/>
        </g>
        """
    )

    decorative = dedent(
        f"""
        <g fill="none" stroke="{GOLD}" stroke-width="3" opacity="0.85">
          <path d="M90 40 Q130 10 170 40 T250 40"/>
          <path d="M550 260 Q600 290 650 260 T730 260"/>
        </g>
        """
    )

    text = '<g filter="url(#multi-shadow)">' + text_path_RIFT("-nouveau") + "</g>"
    icon = '<use href="#rift-icon" x="40" y="100" width="80" height="88"/>'

    return SVG_HEADER + base_defs() + bg + vines + decorative + text + icon + SVG_FOOTER


def logo_victorian_ornamental():
    bg = f'<rect width="800" height="300" fill="{EMERALD_MID}"/>'

    frame = dedent(
        f"""
        <g fill="none" stroke="{GOLD}" stroke-width="3" opacity="0.95">
          <rect x="40" y="35" width="720" height="230" rx="24" ry="24"/>
          <rect x="65" y="60" width="670" height="180" rx="18" ry="18"
                stroke-width="1.5" opacity="0.8"/>
          <path d="M80 60  Q60 100 80 140"/>
          <path d="M720 60 Q740 100 720 140"/>
          <path d="M80 200 Q60 230 80 260"/>
          <path d="M720 200 Q740 230 720 260"/>
          <circle cx="80"  cy="60"  r="4" fill="{GOLD}"/>
          <circle cx="720" cy="60"  r="4" fill="{GOLD}"/>
          <circle cx="80"  cy="260" r="4" fill="{GOLD}"/>
          <circle cx="720" cy="260" r="4" fill="{GOLD}"/>
        </g>
        """
    )

    filigree = dedent(
        f"""
        <g fill="none" stroke="{EMERALD_ACCENT}" stroke-width="1.6" opacity="0.9">
          <path d="M150 210 C190 180 210 150 230 130 S270 110 300 110"/>
          <path d="M650 90  C610 120 590 150 570 170 S530 210 500 220"/>
        </g>
        """
    )

    text = '<g filter="url(#multi-shadow)">' + text_path_RIFT("-victorian") + "</g>"
    icon = '<use href="#rift-icon" x="600" y="80" width="110" height="110"/>'

    return SVG_HEADER + base_defs() + bg + frame + filigree + text + icon + SVG_FOOTER


def logo_geometric_patterns():
    # Extra geometric pattern
    defs_extra = dedent(
        f"""
        <defs>
          <pattern id="geo-pattern" x="0" y="0" width="20" height="20"
                   patternUnits="userSpaceOnUse">
            <rect width="20" height="20" fill="{EMERALD_DARK}"/>
            <path d="M0 10 L10 0 L20 10 L10 20 Z" fill="{EMERALD_MID}"/>
            <circle cx="10" cy="10" r="3" fill="{GOLD}"/>
          </pattern>
        </defs>
        """
    )

    bg = '<rect width="800" height="300" fill="url(#geo-pattern)"/>'
    # Note: rgba() is not valid in SVG, so use hex with opacity instead
    panel = (
        f'<rect x="80" y="50" width="640" height="200" rx="18" '
        f'fill="{EMERALD_DARK}" fill-opacity="0.7" '
        f'stroke="{GOLD}" stroke-width="2"/>'
    )
    text = '<g filter="url(#multi-shadow)">' + text_path_RIFT("-geo") + "</g>"
    icon = '<use href="#rift-icon" x="90" y="90" width="90" height="100" opacity="0.9"/>'

    return SVG_HEADER + base_defs() + defs_extra + bg + panel + text + icon + SVG_FOOTER


def logo_decorative_borders():
    bg = f'<rect width="800" height="300" fill="{EMERALD_DARK}"/>'

    border = dedent(
        f"""
        <g fill="none" stroke="{GOLD}" stroke-width="2" opacity="0.9">
          <rect x="30" y="30" width="740" height="240" rx="30"/>
          <path d="M120 30 L200 30"/>
          <path d="M600 30 L680 30"/>
          <path d="M120 270 L200 270"/>
          <path d="M600 270 L680 270"/>
        </g>
        <g fill="none" stroke="{EMERALD_ACCENT}" stroke-width="1.5" opacity="0.8">
          <path d="M60 60 H740" stroke-dasharray="6 8"/>
          <path d="M60 240 H740" stroke-dasharray="6 8"/>
        </g>
        """
    )

    text = '<g filter="url(#multi-shadow)">' + text_path_RIFT("-border") + "</g>"
    icon = '<use href="#rift-icon" x="640" y="90" width="90" height="100"/>'

    return SVG_HEADER + base_defs() + bg + border + text + icon + SVG_FOOTER


# -------------------------
# Category 3: Material & Texture
# -------------------------

def logo_metallic_chrome():
    defs_extra = dedent(
        """
        <defs>
          <linearGradient id="chrome-grad" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%"   stop-color="#dfe5ea"/>
            <stop offset="30%"  stop-color="#f8fbff"/>
            <stop offset="50%"  stop-color="#9da4ad"/>
            <stop offset="70%"  stop-color="#f8fbff"/>
            <stop offset="100%" stop-color="#c2c9d2"/>
          </linearGradient>
        </defs>
        """
    )

    bg = f'<rect width="800" height="300" fill="{EMERALD_DARK}"/>'
    text = text_path_RIFT("-chrome").replace(
        "url(#grad-emerald-depth)", "url(#chrome-grad)"
    )
    text = '<g filter="url(#multi-shadow)">' + text + "</g>"
    icon = '<use href="#rift-icon" x="60" y="90" width="100" height="100"/>'

    return SVG_HEADER + base_defs() + defs_extra + bg + text + icon + SVG_FOOTER


def logo_brushed_gold():
    bg = f'<rect width="800" height="300" fill="{EMERALD_MID}"/>'
    text = text_path_RIFT("-brushed").replace(
        "url(#grad-emerald-depth)", "url(#grad-gold-metal)"
    )
    # apply brushed-metal filter to whole group
    text = '<g filter="url(#brushed-metal)">' + text + "</g>"
    icon = '<use href="#rift-icon" x="600" y="80" width="110" height="110"/>'

    return SVG_HEADER + base_defs() + bg + text + icon + SVG_FOOTER


def logo_carbon_fiber():
    bg = '<rect width="800" height="300" fill="url(#carbon-fiber)"/>'
    plate = (
        f'<rect x="70" y="50" width="660" height="200" rx="16" '
        f'fill="{EMERALD_DARK}" fill-opacity="0.92" '
        f'stroke="{GOLD}" stroke-width="2"/>'
    )
    text = '<g filter="url(#multi-shadow)">' + text_path_RIFT("-carbon") + "</g>"
    icon = '<use href="#rift-icon" x="80" y="90" width="90" height="100"/>'

    return SVG_HEADER + base_defs() + bg + plate + text + icon + SVG_FOOTER


def logo_gradient_mesh_like():
    # Complex radial gradient to mimic mesh
    defs_extra = dedent(
        f"""
        <defs>
          <radialGradient id="mesh-metal" cx="30%" cy="20%" r="80%">
            <stop offset="0%"   stop-color="#fff7d6"/>
            <stop offset="35%"  stop-color="{GOLD}"/>
            <stop offset="75%"  stop-color="#b07a18"/>
            <stop offset="100%" stop-color="#3b2508"/>
          </radialGradient>
        </defs>
        """
    )

    bg = f'<rect width="800" height="300" fill="{EMERALD_MID}"/>'
    text = text_path_RIFT("-mesh").replace(
        "url(#grad-emerald-depth)", "url(#mesh-metal)"
    )
    text = '<g filter="url(#multi-shadow)">' + text + "</g>"
    icon = '<use href="#rift-icon" x="600" y="80" width="110" height="110"/>'

    return SVG_HEADER + base_defs() + defs_extra + bg + text + icon + SVG_FOOTER


# -------------------------
# Category 4: Light & Glow Effects
# -------------------------

def logo_neon_glow():
    bg = f'<rect width="800" height="300" fill="{EMERALD_DARK}"/>'

    neon_defs = dedent(
        """
        <defs>
          <filter id="neon-glow">
            <feGaussianBlur stdDeviation="4" result="blur"/>
            <feColorMatrix in="blur" type="matrix"
              values="0 0 0 0 0   0 0 0 0 0.9   0 0 0 0 0.6   0 0 0 1 0"/>
          </filter>
        </defs>
        """
    )

    text_group = text_path_RIFT("-neon")
    glow = '<g filter="url(#neon-glow)" opacity="0.8">' + text_group + "</g>"

    # Slightly brighter, more neutral front fill for readability
    solid = (
        "<g>"
        + text_group.replace("url(#grad-emerald-depth)", WHITE)
        + "</g>"
    )

    icon = (
        '<use href="#rift-icon" x="60" y="80" width="100" height="110" '
        'filter="url(#neon-glow)"/>'
    )

    return SVG_HEADER + base_defs() + neon_defs + bg + glow + solid + icon + SVG_FOOTER


def logo_inner_light():
    bg = f'<rect width="800" height="300" fill="{EMERALD_MID}"/>'

    # Light emanates from inside letters via mask
    inner = (
        '<rect width="800" height="300" fill="#ffecc0" '
        'mask="url(#inner-light-mask)" opacity="0.9"/>'
    )

    outline = (
        f'<g stroke="{GOLD}" stroke-width="3" fill="none">'
        + text_path_RIFT("-inner")
        + "</g>"
    )
    icon = '<use href="#rift-icon" x="600" y="80" width="110" height="110" opacity="0.85"/>'

    return SVG_HEADER + base_defs() + bg + inner + outline + icon + SVG_FOOTER


def logo_halo_effect():
    bg = f'<rect width="800" height="300" fill="{EMERALD_DARK}"/>'
    halo = '<circle cx="400" cy="150" r="190" fill="url(#spotlight)" opacity="0.95"/>'
    text = '<g filter="url(#multi-shadow)">' + text_path_RIFT("-halo") + "</g>"
    icon = '<use href="#rift-icon" x="80" y="80" width="100" height="110"/>'

    return SVG_HEADER + base_defs() + bg + halo + text + icon + SVG_FOOTER


def logo_spotlight():
    bg = f'<rect width="800" height="300" fill="{EMERALD_MID}"/>'
    spot = (
        '<rect width="800" height="300" fill="url(#spotlight)" opacity="0.9"/>'
    )
    text = '<g filter="url(#multi-shadow)">' + text_path_RIFT("-spot") + "</g>"
    icon = '<use href="#rift-icon" x="600" y="80" width="110" height="110"/>'

    return SVG_HEADER + base_defs() + bg + spot + text + icon + SVG_FOOTER


# -------------------------
# Category 5: Fusion & Integration
# -------------------------

def logo_icon_text_fusion():
    bg = f'<rect width="800" height="300" fill="{EMERALD_DARK}"/>'

    # Icon clipped inside the R counter-shape
    fused = dedent(
        """
        <g transform="translate(160,80)">
          <clipPath id="rift-clip">
            <path d="
              M0 0 L0 120 L40 120
              Q70 120 70 90
              Q70 70 55 60
              Q70 50 70 30
              Q70 0 40 0 Z
              M20 20 L40 20
              Q50 20 50 35
              Q50 50 40 50
              L20 50 Z
              M35 70 L55 100 L35 100 Z
            "/>
          </clipPath>
          <g clip-path="url(#rift-clip)">
            <use href="#rift-icon" x="-10" y="-5" width="140" height="140"/>
          </g>
        </g>
        """
    )

    text = '<g filter="url(#multi-shadow)">' + text_path_RIFT("-fusion") + "</g>"

    return SVG_HEADER + base_defs() + bg + fused + text + SVG_FOOTER


def logo_breaking_through():
    bg = f'<rect width="800" height="300" fill="{EMERALD_MID}"/>'
    crack = '<use href="#rift-icon" x="320" y="80" width="140" height="140"/>'

    # Mask that hides a central band of text where icon "breaks through"
    mask_defs = dedent(
        """
        <defs>
          <mask id="break-mask">
            <rect width="800" height="300" fill="white"/>
            <rect x="330" y="80" width="130" height="140" fill="black"/>
          </mask>
        </defs>
        """
    )

    text = (
        '<g mask="url(#break-mask)" filter="url(#multi-shadow)">'
        + text_path_RIFT("-break")
        + "</g>"
    )

    return SVG_HEADER + base_defs() + mask_defs + bg + text + crack + SVG_FOOTER


def logo_wrapped_integration():
    bg = f'<rect width="800" height="300" fill="{EMERALD_DARK}"/>'

    # Gold S-curve wraps icon area
    wrap_paths = dedent(
        f"""
        <g fill="none" stroke="{GOLD}" stroke-width="3" opacity="0.9">
          <path d="M520 90 C560 110 560 190 520 210"/>
          <path d="M520 90 C480 110 480 190 520 210"/>
        </g>
        """
    )

    text = '<g filter="url(#multi-shadow)">' + text_path_RIFT("-wrap") + "</g>"
    icon = '<use href="#rift-icon" x="510" y="90" width="110" height="110"/>'

    return SVG_HEADER + base_defs() + bg + wrap_paths + text + icon + SVG_FOOTER


def logo_morphing_elements():
    bg = f'<rect width="800" height="300" fill="{EMERALD_MID}"/>'

    # Gradient stripe behind text to imply morphing energy
    grad_defs = dedent(
        f"""
        <defs>
          <linearGradient id="morph-grad" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%"   stop-color="{EMERALD_BRIGHT}"/>
            <stop offset="50%"  stop-color="{GOLD}"/>
            <stop offset="100%" stop-color="#ff9b24"/>
          </linearGradient>
        </defs>
        """
    )
    grad_stripe = (
        '<rect x="140" y="120" width="520" height="25" '
        'fill="url(#morph-grad)" opacity="0.85"/>'
    )

    # Icon chain that scales along the text for morph feel
    icon_chain = dedent(
        """
        <g opacity="0.9">
          <use href="#rift-icon" x="130" y="60" width="60"  height="60"/>
          <use href="#rift-icon" x="210" y="70" width="70"  height="70"/>
          <use href="#rift-icon" x="310" y="80" width="80"  height="80"/>
        </g>
        """
    )

    text = '<g filter="url(#multi-shadow)">' + text_path_RIFT("-morph") + "</g>"

    return (
        SVG_HEADER
        + base_defs()
        + grad_defs
        + bg
        + grad_stripe
        + icon_chain
        + text
        + SVG_FOOTER
    )


# -------------------------
# Registry of all 20 logos
# -------------------------

LOGO_GENERATORS = [
    # Category 1: 3D & Dimensional
    ("3d-extruded",        logo_3d_extruded),
    ("isometric",          logo_isometric),
    ("floating",           logo_floating_elements),
    ("layered-depth",      logo_layered_depth),
    # Category 2: Ornamental & Decorative
    ("art-nouveau",        logo_art_nouveau),
    ("victorian-ornamental", logo_victorian_ornamental),
    ("geometric-patterns", logo_geometric_patterns),
    ("decorative-borders", logo_decorative_borders),
    # Category 3: Material & Texture
    ("metallic-chrome",    logo_metallic_chrome),
    ("brushed-gold",       logo_brushed_gold),
    ("carbon-fiber",       logo_carbon_fiber),
    ("gradient-mesh",      logo_gradient_mesh_like),
    # Category 4: Light & Glow Effects
    ("neon-glow",          logo_neon_glow),
    ("inner-light",        logo_inner_light),
    ("halo-effect",        logo_halo_effect),
    ("spotlight",          logo_spotlight),
    # Category 5: Fusion & Integration
    ("icon-text-fusion",   logo_icon_text_fusion),
    ("breaking-through",   logo_breaking_through),
    ("wrapped-integration", logo_wrapped_integration),
    ("morphing-elements",  logo_morphing_elements),
]


# -------------------------
# File writing
# -------------------------

def write_svg_files():
    ensure_output_dir()
    for name, fn in LOGO_GENERATORS:
        path = os.path.join(OUTPUT_DIR, f"rift-logo-{name}.svg")
        svg = fn()
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"✓ Generated: rift-logo-{name}.svg")


def write_preview_html():
    """
    Dark-theme preview page, logos grouped by category.
    """
    ensure_output_dir()

    sections = {
        "3D & Dimensional": LOGO_GENERATORS[0:4],
        "Ornamental & Decorative": LOGO_GENERATORS[4:8],
        "Material & Texture": LOGO_GENERATORS[8:12],
        "Light & Glow Effects": LOGO_GENERATORS[12:16],
        "Fusion & Integration": LOGO_GENERATORS[16:20],
    }

    html_parts = [
        "<!DOCTYPE html>",
        '<html lang="en">',
        "<head>",
        '<meta charset="UTF-8"/>',
        "<title>RIFT Elaborate Logos Preview</title>",
        "<style>",
        "body{background:#020908;color:#f9fafb;"
        'font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;'
        "padding:40px;}",
        "h1{color:#fbbf24;margin-bottom:0.25rem;}",
        "h2{color:#10b981;margin-top:2.5rem;"
        "border-bottom:1px solid #065f46;padding-bottom:0.25rem;}",
        ".grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(360px,1fr));"
        "gap:24px;margin-top:1.5rem;}",
        ".card{background:#020617;border:1px solid #0f172a;border-radius:16px;"
        "padding:16px;box-shadow:0 18px 45px rgba(0,0,0,0.7);}",
        ".card-title{font-size:0.9rem;letter-spacing:0.08em;text-transform:uppercase;"
        "color:#9ca3af;margin-bottom:0.75rem;}",
        ".thumb{background:#020617;border-radius:12px;padding:8px;display:flex;"
        "align-items:center;justify-content:center;}",
        ".thumb img{max-width:100%;height:auto;border-radius:8px;background:#020617;}",
        "a{color:#e5e7eb;text-decoration:none;}",
        "a:hover{color:#fbbf24;}",
        "</style>",
        "</head>",
        "<body>",
        "<h1>RIFT Elaborate Logo Suite</h1>",
        '<p style="color:#9ca3af;max-width:720px;">'
        "A collection of 20 elaborately layered, expressive SVG logo explorations "
        "for the RIFT premium custom bike brand."
        "</p>",
    ]

    for section_title, items in sections.items():
        html_parts.append(f"<h2>{section_title}</h2>")
        html_parts.append('<div class="grid">')
        for name, _fn in items:
            svg_file = f"rift-logo-{name}.svg"
            html_parts.append('<div class="card">')
            html_parts.append(
                f'<div class="card-title">'
                f'{name.replace("-", " ").title()}</div>'
            )
            html_parts.append('<div class="thumb">')
            html_parts.append(
                f'<a href="{svg_file}" target="_blank">'
                f'<img src="{svg_file}" alt="{name} logo"/></a>'
            )
            html_parts.append("</div></div>")
        html_parts.append("</div>")

    html_parts.append("</body></html>")

    with open(PREVIEW_HTML, "w", encoding="utf-8") as f:
        f.write("\n".join(html_parts))
    print(f"✓ Generated: preview.html")


def main():
    print("\n🎨 RIFT Elaborate Logo Generator")
    print("=" * 60)
    print(f"Output directory: {OUTPUT_DIR}\n")
    write_svg_files()
    write_preview_html()
    print("\n" + "=" * 60)
    print("✅ All 20 elaborate logos generated successfully!")
    print(f"📁 Files saved to: {OUTPUT_DIR}")
    print(f"🌐 Preview: {PREVIEW_HTML}")


if __name__ == "__main__":
    main()
