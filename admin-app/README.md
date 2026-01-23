# RIFT Admin Desktop Application

A standalone desktop application for managing RIFT bikes. This app runs separately from the website and connects to the same database.

## Installation

### Option 1: Install from Built Package (Recommended)

1. Download the installer for your operating system:
   - **Windows**: `dist/RIFT Admin Setup.exe`
   - **macOS**: `dist/RIFT Admin.dmg`
   - **Linux**: `dist/RIFT Admin.AppImage`

2. Run the installer and follow the setup wizard

3. Launch "RIFT Admin" from your applications

### Option 2: Build from Source

1. Navigate to the admin-app directory:
```bash
cd admin-app
```

2. Install dependencies:
```bash
npm install
```

3. Build the application:
```bash
# For Windows
npm run build:win

# For macOS
npm run build:mac

# For Linux
npm run build:linux
```

4. The built application will be in the `dist` folder

## Usage

1. **Start the website** (if not already running):
   ```bash
   cd /path/to/rift
   npm run dev
   ```

2. **Launch RIFT Admin** application

3. The admin app will connect to the website's API at `http://localhost:3000`

## Features

- **View all bikes**: See all bikes in the database
- **Add new bikes**: Create new bike entries
- **Edit bikes**: Update bike information
- **Delete bikes**: Remove bikes from the database
- **Real-time updates**: Automatically refreshes every 5 seconds

## Requirements

- The main RIFT website must be running on `localhost:3000`
- The website's database (`rift.db`) must be accessible

## Troubleshooting

**Cannot connect to API:**
- Make sure the website is running: `npm run dev` in the main project
- Check that the website is accessible at `http://localhost:3000`

**Database errors:**
- Ensure the `rift.db` file exists in the main project root
- Check file permissions

## Development

To run in development mode:

```bash
npm start
```

This will open the Electron app with DevTools enabled.
