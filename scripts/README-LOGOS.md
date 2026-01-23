# Brand Logo Management

## Current Situation

The website currently uses **custom-made logos** that need to be replaced with **official brand logos**.

## What You Need to Do

### Option 1: Manual Download (Recommended)

1. Visit each brand's official website
2. Find their Media/Press/Brand Assets section
3. Download official SVG or PNG logo files
4. Save to: `public/logos/partners/`
5. Replace existing custom logos

### Option 2: Use Download Script

```bash
cd /home/tau/RIFT
python3 scripts/download-official-logos.py
```

**Note:** Automatic downloads may not work for all brands due to website restrictions.

### Option 3: Contact Brands Directly

Email brand marketing departments:
- Explain you're a bicycle dealer/reseller
- Request official logo files
- Ask for brand usage guidelines

## Brands Required

See `OFFICIAL-LOGOS-REQUIRED.md` for complete list and download instructions.

## File Locations

- **Current logos:** `public/logos/partners/`
- **Component references:** `components/PartnerLogos.tsx`
- **Component database:** `lib/components.ts`

## After Downloading

1. Replace custom logos with official ones
2. Test website display
3. Verify all logos show correctly
4. Check mobile responsiveness

## Legal Notes

- Always verify usage rights
- Follow brand guidelines
- Some brands require permission for commercial use
- Do not modify official logos
