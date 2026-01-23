# GitHub Hosting Instructions

## Overview
This guide explains how to host your Next.js website on GitHub using Vercel (recommended) or GitHub Pages.

## Option 1: Vercel (Recommended for Next.js)

### Why Vercel
- Built by Next.js creators
- Automatic deployments from GitHub
- Free SSL certificates
- Serverless functions support
- Environment variables management
- Custom domain support

### Setup Steps

1. **Push Code to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Create Vercel Account**
   - Go to https://vercel.com
   - Click "Sign Up"
   - Choose "Continue with GitHub"
   - Authorize Vercel to access your GitHub account

3. **Import Project**
   - In Vercel Dashboard, click "Add New Project"
   - Select your GitHub repository (rift-bikes)
   - Click "Import"

4. **Configure Project**
   - Framework Preset: Next.js (auto-detected)
   - Root Directory: ./ (default)
   - Build Command: `npm run build` (default)
   - Output Directory: `.next` (default)
   - Install Command: `npm install` (default)

5. **Add Environment Variables**
   - In Project Settings → Environment Variables
   - Add:
     - `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY` = your Stripe publishable key
     - `STRIPE_SECRET_KEY` = your Stripe secret key
   - Click "Save"

6. **Deploy**
   - Click "Deploy"
   - Wait for build to complete (2-5 minutes)
   - Your site will be live at: `https://your-project-name.vercel.app`

7. **Add Custom Domain**
   - In Project Settings → Domains
   - Add `riftbike.com` and `www.riftbike.com`
   - Follow DNS setup instructions in DNS_SETUP.md
   - Vercel automatically provisions SSL certificates

### Automatic Deployments
- Every push to `main` branch = production deployment
- Every pull request = preview deployment
- No manual deployment needed

## Option 2: GitHub Pages (Static Export Only)

### Limitations
- Next.js must be configured for static export
- No server-side features (API routes, server components)
- Requires build modifications

### Setup Steps

1. **Modify next.config.js**
   ```javascript
   /** @type {import('next').NextConfig} */
   const nextConfig = {
     output: 'export',
     images: {
       unoptimized: true,
     },
   }
   
   module.exports = nextConfig
   ```

2. **Update package.json**
   Add to scripts:
   ```json
   "export": "next build"
   ```

3. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Configure for GitHub Pages"
   git push origin main
   ```

4. **Enable GitHub Pages**
   - Go to repository Settings → Pages
   - Source: Deploy from a branch
   - Branch: `main` → `/out` folder
   - Click "Save"

5. **Configure GitHub Actions (Optional)**
   Create `.github/workflows/deploy.yml`:
   ```yaml
   name: Deploy to GitHub Pages
   
   on:
     push:
       branches: [ main ]
   
   jobs:
     build-and-deploy:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         - uses: actions/setup-node@v3
           with:
             node-version: '18'
         - run: npm install
         - run: npm run export
         - uses: peaceiris/actions-gh-pages@v3
           with:
             github_token: ${{ secrets.GITHUB_TOKEN }}
             publish_dir: ./out
   ```

6. **Site URL**
   - Your site will be at: `https://your-username.github.io/rift-bikes`
   - Or configure custom domain in repository Settings → Pages

## Option 3: Netlify

### Setup Steps

1. **Push Code to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Create Netlify Account**
   - Go to https://netlify.com
   - Click "Sign up"
   - Choose "Continue with GitHub"

3. **Import Project**
   - Click "Add new site" → "Import an existing project"
   - Select GitHub → Choose your repository
   - Click "Deploy site"

4. **Configure Build Settings**
   - Build command: `npm run build`
   - Publish directory: `.next`
   - Click "Deploy site"

5. **Add Environment Variables**
   - Site settings → Environment variables
   - Add Stripe keys
   - Redeploy site

6. **Add Custom Domain**
   - Site settings → Domain management
   - Add custom domain: `riftbike.com`
   - Follow DNS setup in DNS_SETUP.md

## Environment Variables Setup

### For Vercel/Netlify
Add in hosting provider's dashboard:
- `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY`
- `STRIPE_SECRET_KEY`

### For GitHub Pages
GitHub Pages doesn't support server-side environment variables. Use client-side only or switch to Vercel/Netlify.

## Post-Deployment Checklist

1. ✅ Verify site loads at production URL
2. ✅ Test payment system with Stripe test keys
3. ✅ Verify all pages load correctly
4. ✅ Check mobile responsiveness
5. ✅ Test checkout flow
6. ✅ Configure custom domain (if applicable)
7. ✅ Set up SSL certificate (automatic on Vercel/Netlify)
8. ✅ Switch to Stripe live keys when ready
9. ✅ Set up monitoring/analytics (optional)

## Continuous Deployment

### Vercel/Netlify
- Automatic: Every push to main branch
- Preview: Every pull request

### GitHub Pages
- Automatic: If using GitHub Actions workflow
- Manual: Push to `gh-pages` branch

## Troubleshooting

**Build fails:**
- Check build logs in hosting provider dashboard
- Verify all dependencies are in package.json
- Ensure Node.js version is compatible (18+)

**Environment variables not working:**
- Verify variable names match exactly (case-sensitive)
- Redeploy after adding variables
- Check variable is set for correct environment (production/preview)

**Site not updating:**
- Clear browser cache
- Check deployment status in dashboard
- Verify latest code is pushed to GitHub

**Custom domain not working:**
- Verify DNS records are correct (see DNS_SETUP.md)
- Wait for DNS propagation (up to 48 hours)
- Check SSL certificate status in hosting dashboard

## Recommended: Vercel
For Next.js applications, Vercel is the recommended hosting solution because:
- Zero configuration needed
- Optimized for Next.js
- Automatic HTTPS
- Global CDN
- Serverless functions included
- Free tier is generous
