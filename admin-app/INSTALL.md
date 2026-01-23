# RIFT Admin - Installation Guide

## Quick Start

### Step 1: Install Dependencies

Navigate to the admin-app directory and install:

```bash
cd admin-app
npm install
```

### Step 2: Build the Application

Build for your operating system:

**Windows:**
```bash
npm run build:win
```

**macOS:**
```bash
npm run build:mac
```

**Linux:**
```bash
npm run build:linux
```

### Step 3: Install the Application

The built installer will be in the `dist` folder:

- **Windows**: Run `RIFT Admin Setup.exe`
- **macOS**: Open `RIFT Admin.dmg` and drag to Applications
- **Linux**: Make `RIFT Admin.AppImage` executable and run it

## Usage

1. **Start the main website** (if not already running):
   ```bash
   # In the main RIFT project directory
   npm run dev
   ```

2. **Launch RIFT Admin** from your applications menu

3. The admin app will automatically connect to the website's API

## Features

- ✅ View all bikes
- ✅ Add new bikes
- ✅ Edit existing bikes
- ✅ Delete bikes
- ✅ Real-time updates (refreshes every 5 seconds)

## Requirements

- Node.js 18+ installed
- The main RIFT website running on `localhost:3000`
- Access to the website's database file (`rift.db`)

## Troubleshooting

**App won't start:**
- Make sure Node.js is installed: `node --version`
- Reinstall dependencies: `npm install`

**Cannot connect to website:**
- Ensure the website is running: `npm run dev` in the main project
- Check that `http://localhost:3000` is accessible in your browser

**Database errors:**
- The app connects via the website's API, not directly to the database
- Make sure the website can access `rift.db`
