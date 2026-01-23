# Netlify Database Fix - Bikes Not Showing

## Problem
Bikes were not displaying on Netlify because:
- SQLite database file (`rift.db`) is not in repository (in `.gitignore`)
- Netlify's serverless environment has read-only filesystem
- Database is empty on Netlify, so no bikes returned

## Solution Implemented

### 1. Exported Bikes Data
- Created `lib/bikes-data.ts` with exported bikes from local database
- Contains: RIFT Rapid and RIFT Climb
- This file is committed to GitHub

### 2. API Fallback
- Updated `app/api/bikes/route.ts`
- Tries to fetch from database first
- If database is empty or unavailable, returns bikes from `bikes-data.ts`
- Ensures bikes always display, even without database

### 3. Files Added to Repository
- ✅ `lib/bikes-data.ts` - Bike data (committed)
- ✅ `scripts/export-bikes.ts` - Script to export bikes
- ✅ Updated API route with fallback

## How It Works

1. **On Netlify:**
   - Database is empty/unavailable
   - API detects empty database
   - Returns bikes from `bikes-data.ts`
   - Bikes display correctly

2. **Locally:**
   - Database works normally
   - API returns bikes from database
   - If database fails, falls back to `bikes-data.ts`

## Updating Bikes

To update bikes data:

1. **Add bikes to local database** (using admin panel or scripts)
2. **Export bikes:**
   ```bash
   npx tsx scripts/export-bikes.ts
   ```
3. **Commit and push:**
   ```bash
   git add lib/bikes-data.ts
   git commit -m "Update bikes data"
   git push
   ```

## Current Bikes in Fallback

- **RIFT Rapid** - £2,499 - Performance
- **RIFT Climb** - £4,499 - E-Mountain

## Notes

- Database still works locally
- Fallback ensures site works on Netlify
- Can add more bikes by exporting from local database
- All files are now in GitHub repository
