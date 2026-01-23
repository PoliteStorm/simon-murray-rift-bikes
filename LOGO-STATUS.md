# Brand Logo Status

## Current Status

### ✅ Downloaded/Found:
- **Maxxis** - Downloaded from Simple Icons (needs verification if official)
- **JAGWIRE** - Custom logo exists (needs official replacement)
- **Bafang** - Custom logo exists (needs official replacement)  
- **Tektro** - Custom logo exists (needs official replacement)

### ❌ Missing Official Logos:
- **Shimano** - User mentioned it's in RIFT folder, but not found in partners directory
- **SRAM** - Not downloaded yet
- **Campagnolo** - Not downloaded yet
- **RockShox** - Not downloaded yet

## Action Required

### 1. Find Shimano SVG
The user mentioned the Shimano SVG is in the RIFT folder. Please:
- Check if it's in a different location
- Or provide the exact path to the file
- We'll copy it to: `public/logos/partners/shimano.svg`

### 2. Download Remaining Logos

Run the download script:
```bash
cd /home/tau/RIFT
./scripts/download-logos-final.sh
```

Or download manually from:
- **SRAM**: https://www.sram.com (Media/Press section)
- **Campagnolo**: https://www.campagnolo.com (Corporate/Media)
- **RockShox**: https://www.rockshox.com (Brand Assets)

### 3. Replace Custom Logos

Current custom logos that need official versions:
- `maxxis.svg` - Currently custom, needs official
- `jagwire.svg` - Currently custom, needs official
- `bafang.svg` - Currently custom, needs official
- `tektro.svg` - Currently custom, needs official

## File Locations

- **Current logos**: `/home/tau/RIFT/public/logos/partners/`
- **Component references**: `components/PartnerLogos.tsx`
- **Component database**: `lib/components.ts`

## Next Steps

1. ✅ Locate Shimano SVG file in RIFT folder
2. ⏳ Download SRAM, Campagnolo, RockShox logos
3. ⏳ Replace all custom logos with official versions
4. ⏳ Verify all logos display correctly on website
