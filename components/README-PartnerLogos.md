# Partner Logos Component

## Overview

The `PartnerLogos` component displays premium component and feature logos to showcase RIFT's quality custom builds. It includes logos for Shimano groupsets, materials, features, and services.

## Usage

```tsx
import PartnerLogos from '@/components/PartnerLogos';

// Compact variant (for home page, bike pages)
<PartnerLogos variant="compact" />

// Grid variant with categories (for about page)
<PartnerLogos variant="grid" showCategories={true} />

// Default variant (grouped by category)
<PartnerLogos variant="default" showCategories={false} />
```

## Variants

### `compact`
- Horizontal row of logos
- Best for: Home page footer, bike detail pages
- Minimal space usage
- Hover effects for interactivity

### `grid`
- Grid layout with all logos
- Best for: About page, dedicated components page
- Shows all logos in organized grid
- Optional category labels

### `default`
- Grouped by category
- Best for: Detailed component showcase
- Shows categories with organized sections
- Most comprehensive display

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| `variant` | `'default' \| 'compact' \| 'grid'` | `'default'` | Display variant |
| `showCategories` | `boolean` | `false` | Show category labels |

## Logos Included

### Components
- **Shimano** - Main component brand

### Groupsets
- **Dura Ace** - Top-tier groupset
- **Ultegra** - Professional groupset
- **105** - Performance groupset

### Electronic Shifting
- **Di2** - Electronic shifting system

### Materials
- **T1000 Carbon** - Aerospace-grade carbon fibre

### Features
- **Disc Brakes** - Premium braking system
- **Electric Shifting** - Electronic shifting technology

### Services
- **Lifetime Warranty** - Frame warranty guarantee

### Upgrades
- **Holographic Paint** - Premium paint upgrade

## Logo Files

All logos are stored in `/public/logos/partners/`:
- `shimano.svg`
- `dura-ace.svg`
- `ultegra.svg`
- `105.svg`
- `di2.svg`
- `t1000-carbon.svg`
- `disc-brakes.svg`
- `electric-shifting.svg`
- `lifetime-warranty.svg`
- `holographic-paint.svg`

## Adding New Logos

1. Create SVG file in `/public/logos/partners/`
2. Add entry to `partnerLogos` array in component:
```tsx
{
  name: 'New Logo',
  category: 'Category',
  imagePath: '/logos/partners/new-logo.svg'
}
```

## Styling

The component uses RIFT brand colors:
- Background: `rift-card` (emerald dark)
- Border: `rift-emerald` (emerald accent)
- Hover: `rift-gold` (gold accent)
- Text: White with gold accents

## Current Usage

- **Home Page**: Compact variant in footer section
- **About Page**: Grid variant with categories
- **Bike Detail Pages**: Compact variant below specifications

## Design Notes

- All logos are SVG for scalability
- Hover effects provide interactivity
- Responsive grid layouts for all screen sizes
- Maintains brand consistency with RIFT color scheme
