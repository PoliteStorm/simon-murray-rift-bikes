# DNS Setup Instructions for 123reg.com

## Overview
This guide explains how to configure DNS records for riftbike.com to point to your hosting provider.

## Prerequisites
- Access to 123reg.com DNS management panel
- Your hosting provider's IP address or CNAME (if using GitHub Pages, Vercel, Netlify, etc.)

## Access DNS Management
1. Log into 123reg.com account
2. Go to: https://dcc.123-reg.co.uk/control/dnsmanagement?domainName=riftbike.com&plid=587240
3. Or navigate: Control Panel → Domain Management → DNS Management → Select riftbike.com

## DNS Configuration Options

### Option 1: Using Vercel (Recommended for Next.js)
If hosting on Vercel:

1. **In Vercel Dashboard:**
   - Go to your project → Settings → Domains
   - Add `riftbike.com` and `www.riftbike.com`
   - Vercel will provide DNS records

2. **In 123reg DNS Management:**
   - Add A Record:
     - Type: A
     - Name: @ (or leave blank for root domain)
     - Value: 76.76.21.21 (Vercel's IP - verify in Vercel dashboard)
     - TTL: 3600
   
   - Add CNAME Record:
     - Type: CNAME
     - Name: www
     - Value: cname.vercel-dns.com (verify in Vercel dashboard)
     - TTL: 3600

### Option 2: Using Netlify
If hosting on Netlify:

1. **In Netlify Dashboard:**
   - Go to Site settings → Domain management
   - Add custom domain: `riftbike.com`
   - Netlify will provide DNS records

2. **In 123reg DNS Management:**
   - Delete existing A records for @
   - Add A Record:
     - Type: A
     - Name: @
     - Value: 75.2.60.5 (verify in Netlify dashboard)
     - TTL: 3600
   
   - Add CNAME Record:
     - Type: CNAME
     - Name: www
     - Value: your-site-name.netlify.app
     - TTL: 3600

### Option 3: Using GitHub Pages
If hosting on GitHub Pages:

1. **In GitHub Repository:**
   - Go to Settings → Pages
   - Under Custom domain, enter: `riftbike.com`
   - GitHub will provide DNS records

2. **In 123reg DNS Management:**
   - Add A Records (add all 4):
     - Type: A
     - Name: @
     - Value: 185.199.108.153
     - TTL: 3600
   
     - Type: A
     - Name: @
     - Value: 185.199.109.153
     - TTL: 3600
   
     - Type: A
     - Name: @
     - Value: 185.199.110.153
     - TTL: 3600
   
     - Type: A
     - Name: @
     - Value: 185.199.111.153
     - TTL: 3600
   
   - Add CNAME Record:
     - Type: CNAME
     - Name: www
     - Value: your-username.github.io
     - TTL: 3600

### Option 4: Using Custom Server/VPS
If hosting on your own server:

1. **Get your server's IP address**
2. **In 123reg DNS Management:**
   - Add A Record:
     - Type: A
     - Name: @
     - Value: YOUR_SERVER_IP_ADDRESS
     - TTL: 3600
   
   - Add A Record (for www):
     - Type: A
     - Name: www
     - Value: YOUR_SERVER_IP_ADDRESS
     - TTL: 3600

## Step-by-Step: Adding DNS Records in 123reg

1. Log into 123reg.com
2. Navigate to DNS Management for riftbike.com
3. Click "Add Record" or "Manage DNS"
4. Select record type (A, CNAME, etc.)
5. Enter:
   - **Name/Host**: @ for root domain, www for www subdomain
   - **Value/Target**: IP address or CNAME target
   - **TTL**: 3600 (1 hour) is standard
6. Click "Save" or "Add Record"
7. Wait 5-60 minutes for DNS propagation

## Verify DNS Configuration

After adding records, verify with:

```bash
# Check A record
nslookup riftbike.com

# Check CNAME record
nslookup www.riftbike.com

# Or use online tools:
# - https://dnschecker.org
# - https://www.whatsmydns.net
```

## Common Issues

**DNS not updating:**
- Wait up to 48 hours for full propagation
- Clear DNS cache: `ipconfig /flushdns` (Windows) or `sudo dscacheutil -flushcache` (Mac)
- Check TTL value - lower TTL = faster updates

**Website not loading:**
- Verify DNS records are correct
- Check hosting provider is configured correctly
- Ensure SSL certificate is set up (if using HTTPS)

**Subdomain not working:**
- Verify CNAME record is added correctly
- Check www subdomain points to correct target

## SSL Certificate Setup

After DNS is configured:
1. Most hosting providers (Vercel, Netlify) automatically provision SSL certificates
2. For custom servers, use Let's Encrypt or your hosting provider's SSL service
3. Ensure HTTPS is enabled and HTTP redirects to HTTPS

## Notes
- DNS changes can take 5 minutes to 48 hours to propagate globally
- Always verify records match your hosting provider's requirements
- Keep a backup of your DNS configuration
- TTL (Time To Live) controls how long DNS records are cached
