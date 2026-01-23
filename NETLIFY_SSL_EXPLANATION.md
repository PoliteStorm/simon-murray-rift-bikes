# Netlify SSL/TLS Certificate - What It All Means

## Overview
Your DNS verification was successful! Netlify can now set up a free SSL certificate so your site uses HTTPS (secure connection).

## Main Options

### 1. "Provision certificate" (RECOMMENDED - Choose This)
**What it does:**
- Netlify automatically gets a free SSL certificate from Let's Encrypt
- Installs it on their CDN (Content Delivery Network)
- Your site will use HTTPS (secure, encrypted connection)
- Certificate renews automatically (never expires)

**When to use:**
- ✅ **Always choose this** - It's free and automatic
- Works for most websites
- No technical setup needed

**Action:** Click **"Provision certificate"**

---

### 2. "Provide your own certificate"
**What it does:**
- You upload your own SSL certificate
- You manage certificate renewal yourself
- More complex setup

**When to use:**
- Only if you have a specific certificate requirement
- Enterprise/compliance needs
- **Not recommended for most sites**

**Action:** Don't choose this unless you have a specific reason

---

## Automatic Deploy Subdomains (Paid Feature)

**What it means:**
This is a **paid feature** - you don't need it for basic hosting.

**What it does:**
- Creates automatic URLs for preview deployments
- Example: `deploy-preview-123--your-site.netlify.app`
- Useful for testing before going live

**Do you need it?**
- ❌ **No** - Not required for your site
- Your site works fine without it
- Free tier is sufficient

**Action:** Ignore this section - it's optional

---

## What Happens After You Click "Provision certificate"

1. **Netlify requests certificate** from Let's Encrypt (takes 1-5 minutes)
2. **Certificate is installed** on Netlify's servers
3. **Your site becomes secure:**
   - `https://riftbike.com` ✅ (secure)
   - `http://riftbike.com` → automatically redirects to HTTPS
4. **Certificate auto-renews** - you never need to worry about it

---

## Step-by-Step: What To Do Now

1. **Click "Provision certificate"** button
2. **Wait 1-5 minutes** for certificate to be issued
3. **Check status:**
   - Go to: Site settings → SSL/TLS
   - Should show: "Certificate issued" ✅
4. **Test your site:**
   - Visit `https://riftbike.com`
   - Browser should show a padlock icon 🔒
   - No security warnings

---

## Important Notes

### Your Site Will Work With:
- ✅ `https://riftbike.com` (secure)
- ✅ `https://www.riftbike.com` (secure)
- ✅ `http://riftbike.com` (redirects to HTTPS)
- ✅ `http://www.riftbike.com` (redirects to HTTPS)

### Certificate Details:
- **Provider:** Let's Encrypt (free, trusted)
- **Type:** Automatic renewal
- **Validity:** 90 days (auto-renews)
- **Coverage:** Both `riftbike.com` and `www.riftbike.com`

---

## Troubleshooting

### Certificate Not Issuing?
- Wait 5-10 minutes (can take time)
- Check DNS is still correct
- Verify domain is added in Netlify

### Security Warning in Browser?
- Wait for certificate to fully propagate (up to 1 hour)
- Clear browser cache
- Try incognito/private window

### Certificate Expired?
- Should auto-renew, but if it doesn't:
- Go to SSL/TLS settings
- Click "Renew certificate"

---

## Summary

**What to do:**
1. ✅ Click **"Provision certificate"**
2. ✅ Wait 1-5 minutes
3. ✅ Done! Your site is secure

**What to ignore:**
- ❌ "Provide your own certificate" (not needed)
- ❌ "Automatic deploy subdomains" (paid feature, not needed)

**Result:**
- Your site will have HTTPS
- Free SSL certificate
- Automatic renewal
- No action needed after setup

---

## Quick Answer

**Just click "Provision certificate"** - that's all you need to do! Everything else is automatic.
