# Hosting on 123reg - Guide

## Can You Host Next.js on 123reg?

**Short answer:** It depends on your hosting plan. Basic shared hosting typically does NOT support Next.js.

## 123reg Hosting Options

### Option 1: Shared Hosting (NOT Recommended)
- **Limitation:** Does not support Node.js/Next.js
- **What it supports:** Static HTML, PHP, WordPress
- **Cost:** £2-5/month
- **Verdict:** Cannot host your Next.js website

### Option 2: VPS (Virtual Private Server) - Possible
- **Requirement:** Full server access with Node.js installed
- **What you need:**
  - SSH access
  - Ability to install Node.js
  - Ability to run `npm install` and `npm run build`
  - Process manager (PM2) to keep server running
  - Reverse proxy (Nginx) configuration
- **Cost:** £10-30/month
- **Verdict:** Possible but requires technical setup

### Option 3: Dedicated Server - Possible
- **Requirement:** Full server control
- **Cost:** £50+/month
- **Verdict:** Overkill for most websites

## Why Next.js is Different

Your website requires:
- Node.js runtime (for server-side rendering)
- API routes (`/api/create-payment-intent`)
- Database (SQLite)
- Build process (`npm run build`)
- Server process running continuously

These features are NOT available on basic shared hosting.

## Recommended Alternatives

### 1. Vercel (Best for Next.js)
- **Cost:** Free tier available, then £16/month
- **Why:** Built by Next.js creators, zero configuration
- **Features:**
  - Automatic deployments from GitHub
  - Free SSL certificates
  - Global CDN
  - Serverless functions included
- **Setup:** Connect GitHub repository, automatic deployment

### 2. Netlify
- **Cost:** Free tier available, then £15/month
- **Why:** Easy deployment, good Next.js support
- **Features:** Similar to Vercel
- **Setup:** Connect GitHub, automatic deployment

### 3. Railway
- **Cost:** £5-20/month
- **Why:** Good for Node.js applications
- **Features:** Simple deployment, database included
- **Setup:** Connect GitHub or deploy via CLI

### 4. DigitalOcean App Platform
- **Cost:** £5-25/month
- **Why:** Reliable, good performance
- **Features:** Automatic scaling, managed databases
- **Setup:** Connect GitHub repository

## How to Check 123reg Support

1. **Contact 123reg Support:**
   - Ask: "Do you support Node.js applications?"
   - Ask: "Can I run Next.js on your hosting?"
   - Ask: "Do you have VPS plans with Node.js?"

2. **Check Their Documentation:**
   - Look for "Node.js" or "Application Hosting" in their hosting plans
   - Check if they mention "SSH access" or "Full server control"

3. **If They Say Yes:**
   - Verify you can install Node.js
   - Verify you can run `npm` commands
   - Verify you can keep a process running 24/7
   - Ask about reverse proxy setup (Nginx/Apache)

## If Using 123reg VPS

If you proceed with 123reg VPS, you'll need to:

1. **Install Node.js:**
   ```bash
   # SSH into your server
   curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
   sudo apt-get install -y nodejs
   ```

2. **Install PM2 (Process Manager):**
   ```bash
   npm install -g pm2
   ```

3. **Deploy Your Site:**
   ```bash
   git clone your-repo
   cd RIFT
   npm install
   npm run build
   pm2 start npm --name "rift-bikes" -- start
   pm2 save
   pm2 startup
   ```

4. **Configure Nginx (Reverse Proxy):**
   ```nginx
   server {
       listen 80;
       server_name riftbike.com www.riftbike.com;
       
       location / {
           proxy_pass http://localhost:3000;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection 'upgrade';
           proxy_set_header Host $host;
           proxy_cache_bypass $http_upgrade;
       }
   }
   ```

5. **Set Up SSL (Let's Encrypt):**
   ```bash
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx -d riftbike.com -d www.riftbike.com
   ```

## Recommendation

**For your Next.js e-commerce site, I recommend:**

1. **Vercel** - Easiest, best Next.js support, free tier available
2. **Netlify** - Good alternative, similar to Vercel
3. **123reg VPS** - Only if you need UK-based hosting and have technical expertise

**Why not 123reg shared hosting:**
- Cannot run Node.js
- Cannot run your API routes
- Cannot use your database
- Will not work with your Next.js application

## Next Steps

1. **If choosing Vercel/Netlify:**
   - Follow instructions in `GITHUB_HOSTING.md`
   - Connect your GitHub repository
   - Deploy automatically

2. **If choosing 123reg VPS:**
   - Contact 123reg to confirm Node.js support
   - Follow the setup steps above
   - Configure DNS as per `DNS_SETUP.md`

3. **If staying with 123reg:**
   - Use 123reg only for domain management
   - Host website on Vercel/Netlify
   - Point DNS from 123reg to your hosting provider

## Cost Comparison

- **123reg Shared Hosting:** £2-5/month (won't work)
- **123reg VPS:** £10-30/month (requires setup)
- **Vercel:** Free tier, then £16/month (easiest)
- **Netlify:** Free tier, then £15/month (easy)
- **Railway:** £5-20/month (good balance)

## Summary

**Can you host on 123reg?**
- Shared hosting: ❌ No
- VPS: ✅ Yes, but requires technical setup
- Recommended: Use Vercel or Netlify instead

Your Next.js website needs Node.js runtime, which basic shared hosting does not provide. Vercel or Netlify are better options for Next.js applications.
