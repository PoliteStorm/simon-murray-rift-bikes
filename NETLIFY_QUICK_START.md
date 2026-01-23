# Quick Start: 123reg DNS + Netlify

## Part 1: DNS Setup on 123reg (Do This First)

1. **Go to 123reg DNS:**
   https://dcc.123-reg.co.uk/control/dnsmanagement?domainName=riftbike.com&plid=587240

2. **Add A Record:**
   - Type: **A**
   - Name: **@** (or leave blank)
   - Value: **75.2.60.5**
   - TTL: **3600**
   - Click **Save**

3. **Add CNAME Record** (you'll update this after Netlify deployment):
   - Type: **CNAME**
   - Name: **www**
   - Value: **placeholder.netlify.app** (temporary - update after Step 2)
   - TTL: **3600**
   - Click **Save**

✅ DNS setup complete!

---

## Part 2: Deploy to Netlify

### Step 1: Push Code to GitHub
```bash
# If not already done:
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/rift-bikes.git
git push -u origin main
```

### Step 2: Create Netlify Account
1. Go to https://netlify.com
2. Sign up with GitHub

### Step 3: Deploy Site
1. Click **"Add new site"** → **"Import an existing project"**
2. Choose **GitHub**
3. Select your **rift-bikes** repository
4. Netlify will auto-detect Next.js (using `netlify.toml` file)
5. Click **"Deploy site"**

### Step 4: Get Your Netlify URL
- After deployment, your site URL is: `https://random-name-123.netlify.app`
- **Copy this URL**

### Step 5: Update DNS CNAME
1. Go back to 123reg DNS
2. Edit the CNAME record for `www`
3. Change value to your Netlify URL (e.g., `random-name-123.netlify.app`)
4. Save

### Step 6: Add Custom Domain in Netlify
1. In Netlify: **Site settings** → **Domain management**
2. Click **"Add custom domain"**
3. Enter: `riftbike.com`
4. Click **"Add domain alias"**
5. Enter: `www.riftbike.com`
6. Netlify will automatically set up SSL (wait 1-5 minutes)

---

## Part 3: Verify

1. **Check DNS:** https://dnschecker.org
   - Enter `riftbike.com`
   - Should show A record: `75.2.60.5`

2. **Test Site:**
   - Visit `https://riftbike.com` (wait 1-2 hours for DNS)
   - Visit `https://www.riftbike.com`

✅ Done! Your site is live!

---

## Troubleshooting

**Site not loading?**
- Wait 1-2 hours for DNS propagation
- Check Netlify deployment status
- Verify DNS records in 123reg

**SSL not working?**
- Wait 5-10 minutes after adding domain
- Check Netlify SSL/TLS settings

**Build failed?**
- Check Netlify build logs
- Verify `package.json` has `"build": "next build"`

---

## Need More Details?

See `NETLIFY_DNS_SETUP.md` for complete instructions.
