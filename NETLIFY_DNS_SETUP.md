# Complete Setup Guide: 123reg DNS + Netlify Hosting

## Step 1: Set Up DNS on 123reg

### Access DNS Management
1. Log into your 123reg account: https://www.123-reg.co.uk/
2. Go to **Control Panel** → **Domain Management**
3. Click on **DNS Management** for `riftbike.com`
4. Or go directly to: https://dcc.123-reg.co.uk/control/dnsmanagement?domainName=riftbike.com&plid=587240

### Remove Existing DNS Records (if any)
1. Delete any existing A records for `@` (root domain)
2. Delete any existing CNAME records for `www`
3. Keep any MX records (for email) if you use email with this domain

### Add DNS Records for Netlify

**Record 1: A Record for Root Domain**
- **Type:** A
- **Name/Host:** @ (or leave blank)
- **Value/Target:** 75.2.60.5
- **TTL:** 3600 (or Auto)
- Click **Add Record** or **Save**

**Record 2: CNAME Record for www**
- **Type:** CNAME
- **Name/Host:** www
- **Value/Target:** your-site-name.netlify.app
  - *Note: You'll get this from Netlify after deploying (see Step 2)*
- **TTL:** 3600 (or Auto)
- Click **Add Record** or **Save**

**Important:** You can add the A record now, but wait to add the CNAME until after Step 2 when you have your Netlify site URL.

### Verify DNS Records
After adding records, verify they're correct:
- A record: `@` → `75.2.60.5`
- CNAME record: `www` → `your-site-name.netlify.app`

### DNS Propagation
- DNS changes can take 5 minutes to 48 hours to propagate globally
- Usually takes 1-2 hours
- Check propagation status at: https://dnschecker.org

---

## Step 2: Set Up Netlify Hosting

### 2.1 Create Netlify Account
1. Go to https://netlify.com
2. Click **Sign up**
3. Choose **Continue with GitHub** (recommended)
4. Authorize Netlify to access your GitHub account

### 2.2 Push Code to GitHub (if not already done)
1. Open terminal in your project directory
2. Initialize git (if not already):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```
3. Create GitHub repository:
   - Go to https://github.com/new
   - Repository name: `rift-bikes`
   - Description: "RIFT Custom Bike Shop"
   - Choose **Private** or **Public**
   - Do NOT initialize with README
   - Click **Create repository**
4. Push code:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/rift-bikes.git
   git branch -M main
   git push -u origin main
   ```

### 2.3 Deploy to Netlify
1. In Netlify dashboard, click **Add new site** → **Import an existing project**
2. Choose **GitHub**
3. Select your `rift-bikes` repository
4. Click **Deploy site**

### 2.4 Configure Build Settings
Netlify should auto-detect Next.js using the `netlify.toml` file included in your project.

The configuration file (`netlify.toml`) is already set up with:
- Build command: `npm run build`
- Publish directory: `.next`
- Next.js plugin: `@netlify/plugin-nextjs`
- Node version: 18

Netlify will automatically use these settings. If you need to verify:
- Go to **Site settings** → **Build & deploy** → **Build settings**
- Should show: Build command: `npm run build`
- Publish directory: `.next`

### 2.5 Add Environment Variables
1. Go to **Site settings** → **Environment variables**
2. Add the following (if needed):
   ```
   NODE_VERSION=18
   ```
   - Note: Stripe keys not needed since we're using bank transfer
   - Add any other environment variables your app needs

### 2.6 Get Your Netlify Site URL
1. After deployment, go to **Site settings** → **General**
2. Your site URL will be: `https://random-name-123.netlify.app`
3. Copy this URL

### 2.7 Update DNS CNAME Record
1. Go back to 123reg DNS Management
2. Edit the CNAME record for `www`
3. Update **Value/Target** to your Netlify site URL (e.g., `random-name-123.netlify.app`)
4. Save

---

## Step 3: Add Custom Domain to Netlify

### 3.1 Add Domain
1. In Netlify, go to **Site settings** → **Domain management**
2. Click **Add custom domain**
3. Enter: `riftbike.com`
4. Click **Verify**

### 3.2 Add www Subdomain
1. Click **Add domain alias**
2. Enter: `www.riftbike.com`
3. Click **Verify**

### 3.3 Netlify DNS Configuration
Netlify will show you DNS records to add. Since you're using 123reg DNS, you should already have:
- A record: `@` → `75.2.60.5` ✓
- CNAME: `www` → `your-site.netlify.app` ✓

### 3.4 SSL Certificate
1. Netlify automatically provisions SSL certificates
2. Go to **Site settings** → **SSL/TLS**
3. Wait for certificate to be issued (usually 1-5 minutes)
4. Status should show: **Certificate issued**

---

## Step 4: Verify Everything Works

### 4.1 Check DNS Propagation
1. Go to https://dnschecker.org
2. Enter `riftbike.com`
3. Check A record points to `75.2.60.5`
4. Check CNAME for `www` points to your Netlify site

### 4.2 Test Your Site
1. Visit `https://riftbike.com` (wait for DNS propagation)
2. Visit `https://www.riftbike.com`
3. Both should load your site
4. Check SSL certificate (should show as secure)

### 4.3 Test HTTPS
- Both `http://riftbike.com` and `https://riftbike.com` should work
- Netlify automatically redirects HTTP to HTTPS

---

## Troubleshooting

### DNS Not Updating
- Wait up to 48 hours for full propagation
- Clear DNS cache: `ipconfig /flushdns` (Windows) or `sudo dscacheutil -flushcache` (Mac)
- Check TTL value - lower TTL = faster updates

### Site Not Loading
- Verify DNS records are correct in 123reg
- Check Netlify deployment status (should be "Published")
- Verify custom domain is added in Netlify
- Check SSL certificate status in Netlify

### SSL Certificate Issues
- Wait 5-10 minutes after adding domain
- Ensure DNS is properly configured
- Check Netlify SSL/TLS settings

### Build Errors
- Check Netlify build logs
- Verify `package.json` has correct build script
- Ensure all dependencies are in `package.json`
- Check Node.js version (Netlify uses Node 18 by default)

---

## Quick Reference

### 123reg DNS Records Needed:
```
Type: A
Name: @
Value: 75.2.60.5
TTL: 3600

Type: CNAME
Name: www
Value: your-site-name.netlify.app
TTL: 3600
```

### Netlify Settings:
- Build command: `npm run build`
- Publish directory: `.next`
- Node version: 18 (default)

### Important URLs:
- 123reg DNS: https://dcc.123-reg.co.uk/control/dnsmanagement?domainName=riftbike.com&plid=587240
- Netlify Dashboard: https://app.netlify.com
- DNS Checker: https://dnschecker.org

---

## Next Steps After Setup

1. ✅ Test all pages on your site
2. ✅ Test order form (bank transfer checkout)
3. ✅ Verify console logs for orders (Simon Murray notifications)
4. ✅ Set up email notifications (optional - for order confirmations)
5. ✅ Monitor Netlify analytics (optional)

---

## Summary

1. **123reg DNS:** Add A record (`@` → `75.2.60.5`) and CNAME (`www` → Netlify URL)
2. **Netlify:** Deploy from GitHub, add custom domain
3. **SSL:** Automatic via Netlify
4. **Wait:** DNS propagation (1-48 hours)
5. **Test:** Visit `https://riftbike.com`

Your site will be live at `https://riftbike.com` and `https://www.riftbike.com`!
