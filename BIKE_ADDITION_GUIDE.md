# Bike Addition Guide

## 🔍 Bike Name Matching Results

**Potential Matches Found:**
- `R10pro-disc` might match `RIFT Aero Pro` (both are road bikes with disc brakes)
- `R5pro-Term` might match `RIFT Aero Pro` (both are road bikes)

**New Bikes (No Matches):**
- `CYCLONE-3rd` - New model
- `T10pro-2rd` - New model

**Action Required:** Please verify if `R10pro-disc` and `R5pro-Term` are:
1. The same as `RIFT Aero Pro` (just different naming) → Skip adding, or update existing
2. Different models → Add as new bikes

---

## 📸 Available Assets Summary

### CYCLONE-3rd
- **Clean Images:** 8 (Suggested: `4.jpg`)
- **Detail Images:** 1
- **Videos:** 1 (Suggested: `CYCLONE-3rd (105 big).mp4`)
- **Specs:** 1 file

### R10pro-disc
- **Clean Images:** 0
- **Detail Images:** 8
- **Color Images:** 3 (White, MatteBlack, MatteDarkGray)
- **Videos:** 0
- **Specs:** 1 file

### R5pro-Term
- **Clean Images:** 1 (Suggested: `7.jpg`)
- **Detail Images:** 7
- **Color Images:** 6 (BlackRed, MatteBlack, MatteGray, WhiteBlack, WhiteRed, Yellow)
- **Videos:** 1 (Suggested: `1.mp4`)
- **Specs:** 1 file

### T10pro-2rd
- **Clean Images:** 0
- **Detail Images:** 5
- **Color Images:** 7
- **Videos:** 2 (Suggested: `Video (2).mp4`)
- **Specs:** 1 file

---

## 🛠️ How to Add Bikes

### Step 1: Review and Choose Display Images/Videos

For each bike, decide:
- **Display Image:** The main image shown on the bikes listing page
- **Display Video:** Optional video shown on the bike detail page
- **Additional Images:** All other images to include in the gallery

### Step 2: Copy Assets to Public Folder

```bash
npx tsx scripts/prepare-bike-assets.ts copy
```

This will copy all images and videos from `organized_bikes_refined/` to `public/bikes/`.

### Step 3: Update Bike Data

Edit `scripts/add-bikes-with-images.ts`:
1. Review the suggested display images/videos
2. Update `suggestedDisplayImage` and `suggestedDisplayVideo` for each bike if needed
3. Adjust prices, descriptions, and categories as needed
4. For potential duplicates (R10pro-disc, R5pro-Term), decide whether to add or skip

### Step 4: Add to Database

Uncomment the database insert code in `scripts/add-bikes-with-images.ts` and run:

```bash
npx tsx scripts/add-bikes-with-images.ts
```

---

## ✅ Scrollbar Fix

The scrollbar on the custom order page has been fixed to stay within the component selection box. The scrollable area is now properly contained within the border and won't extend the page.

**Changes made:**
- Added `overflow: hidden` to the parent container
- Set proper height constraints on the scrollable area
- Scrollbar now appears inside the component selection box only

---

## 📝 Notes

- All bike assets are organized in `organized_bikes_refined/`
- Images are categorized: `clean/`, `details/`, `colors/`
- Videos are in `videos/` folder
- Spec files are in `specs/` folder (may need manual extraction)

---

## 🚀 Quick Start

1. **Review potential duplicates:**
   - Check if R10pro-disc and R5pro-Term are the same as RIFT Aero Pro

2. **Copy assets:**
   ```bash
   npx tsx scripts/prepare-bike-assets.ts copy
   ```

3. **Review and update bike data:**
   - Edit `scripts/add-bikes-with-images.ts`
   - Choose display images/videos
   - Set prices and descriptions

4. **Add to database:**
   - Uncomment insert code in `add-bikes-with-images.ts`
   - Run: `npx tsx scripts/add-bikes-with-images.ts`
