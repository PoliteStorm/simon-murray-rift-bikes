# 🚲 Instructions to Add 3 New Bikes

## What's Ready:
✅ Red logo image copied to `/public/red-logo.jpg`
✅ Flashing logo now uses the red logo
✅ Bike images copied:
   - `/public/bikes/rift-ultimate.jpg` (RIFT ULTIMATE)
   - `/public/bikes/rift-gravel-extreme.jpg` (RIFT GRAVEL EXTREME)
   - `/public/bikes/rift-gravel-v3.jpg` (RIFT GRAVEL V3 – from GRAVEL zip)
✅ Script ready to add bikes: `scripts/add-new-bikes.js`
✅ All 3 bikes added to initialBikes fallback (same labelling and display)

---

## 🎯 How to Add the Bikes to Your Website

### Option 1: Run the Script (Easiest)

After you deploy to Netlify, you need to add these bikes to your database.

**On your local machine or server:**

```bash
cd /home/kronos777333/website
node scripts/add-new-bikes.js
```

This will add:
1. **RIFT ULTIMATE** - £4,500 (Road)
2. **RIFT GRAVEL EXTREME** - £4,200 (Gravel)
3. **RIFT GRAVEL V3** - £4,100 (Gravel, model: Gravel V3 wireless 105)

---

### Option 2: Add Manually via Admin Panel

If you have an admin panel on your site:

1. Go to your admin page
2. Click "Add New Bike"
3. Fill in the details below

#### RIFT ULTIMATE:
- **Name:** RIFT ULTIMATE
- **Price:** £4,500
- **Category:** Road
- **Image:** /bikes/rift-ultimate.jpg
- **Description:** The ultimate performance road bike featuring T1000 aerospace carbon throughout, Di2 electronic gears with Shimano Ultegra setup. Complete with pedals, seat, and water bottle with carrier. Custom built just for you.
- **Specifications:**
  - Frame: T1000 Aerospace Carbon
  - Gears: Shimano Ultegra Di2 Electronic
  - Wheels: Carbon Wheelset
  - Brakes: Hydraulic Disc
  - Weight: Ultra-lightweight
  - Included: Pedals, Seat, Water Bottle with Carrier

#### RIFT GRAVEL EXTREME:
- **Name:** RIFT GRAVEL EXTREME
- **Price:** £4,200
- **Category:** Gravel
- **Image:** /bikes/rift-gravel-extreme.jpg
- **Description:** Extreme gravel performance with T1000 aerospace carbon, Di2 electronic gears with Shimano Ultegra. Built for adventure on any terrain. Complete with pedals, seat, and water bottle with carrier. Custom built just for you.
- **Specifications:**
  - Frame: T1000 Aerospace Carbon
  - Gears: Shimano Ultegra Di2 Electronic
  - Wheels: Gravel Wheelset
  - Brakes: Hydraulic Disc
  - Tires: All-terrain
  - Included: Pedals, Seat, Water Bottle with Carrier

#### RIFT GRAVEL V3 (3rd bike – from GRAVEL zip):
- **Name:** RIFT GRAVEL V3
- **Model:** Gravel V3 wireless (25yr 105 big)
- **Price:** £4,100
- **Category:** Gravel
- **Image:** /bikes/rift-gravel-v3.jpg
- **Description:** Gravel V3 wireless with T1000 aerospace carbon and Shimano 105 groupset. Built for mixed terrain and adventure. Complete with pedals, seat, and water bottle with carrier. Every bike is custom built just for you.
- **Specifications:**
  - Model: Gravel V3 wireless (25yr 105 big)
  - Frame: T1000 Aerospace Carbon
  - Gears: Shimano 105
  - Wheels: Gravel Wheelset
  - Brakes: Hydraulic Disc
  - Tires: All-terrain
  - Included: Pedals, Seat, Water Bottle with Carrier

---

### Option 3: Direct Database Insert (Advanced)

If you have access to the database directly:

```sql
-- Add RIFT ULTIMATE
INSERT INTO bikes (name, description, basePrice, imageUrl, category, specifications)
VALUES (
  'RIFT ULTIMATE',
  'The ultimate performance road bike featuring T1000 aerospace carbon throughout, Di2 electronic gears with Shimano Ultegra setup. Complete with pedals, seat, and water bottle with carrier. Custom built just for you.',
  4500,
  '/bikes/rift-ultimate.jpg',
  'Road',
  '{"frame":"T1000 Aerospace Carbon","gears":"Shimano Ultegra Di2 Electronic","wheels":"Carbon Wheelset","brakes":"Hydraulic Disc","weight":"Ultra-lightweight","included":"Pedals, Seat, Water Bottle with Carrier"}'
);

-- Add RIFT GRAVEL EXTREME
INSERT INTO bikes (name, description, basePrice, imageUrl, category, specifications)
VALUES (
  'RIFT GRAVEL EXTREME',
  'Extreme gravel performance with T1000 aerospace carbon, Di2 electronic gears with Shimano Ultegra. Built for adventure on any terrain. Complete with pedals, seat, and water bottle with carrier. Custom built just for you.',
  4200,
  '/bikes/rift-gravel-extreme.jpg',
  'Gravel',
  '{"frame":"T1000 Aerospace Carbon","gears":"Shimano Ultegra Di2 Electronic","wheels":"Gravel Wheelset","brakes":"Hydraulic Disc","tires":"All-terrain","included":"Pedals, Seat, Water Bottle with Carrier"}'
);

-- Add RIFT GRAVEL V3 (3rd bike from GRAVEL zip)
INSERT INTO bikes (name, description, basePrice, imageUrl, category, specifications)
VALUES (
  'RIFT GRAVEL V3',
  'Gravel V3 wireless with T1000 aerospace carbon and Shimano 105 groupset. Built for mixed terrain and adventure. Complete with pedals, seat, and water bottle with carrier. Every bike is custom built just for you.',
  4100,
  '/bikes/rift-gravel-v3.jpg',
  'Gravel',
  '{"model":"Gravel V3 wireless (25yr 105 big)","frame":"T1000 Aerospace Carbon","gears":"Shimano 105","wheels":"Gravel Wheelset","brakes":"Hydraulic Disc","tires":"All-terrain","included":"Pedals, Seat, Water Bottle with Carrier"}'
);
```

---

## ✅ What's Already Done:

1. ✅ Red logo is now used for flashing animations
2. ✅ Bike images are in the right place
3. ✅ Script is ready to run
4. ✅ All other changes from before are complete

---

## 🚀 Next Steps:

1. **Push these new changes to GitHub** (I'll do this next)
2. **Wait for Netlify to deploy**
3. **Run the add-bikes script** OR add them manually
4. **Check your website** - you should see 3 new bikes!

---

**Note:** The bikes won't show up until you add them to the database using one of the methods above! (If the database is empty, the site uses initialBikes and all 3 new bikes are already included there with the same labelling and display.)
