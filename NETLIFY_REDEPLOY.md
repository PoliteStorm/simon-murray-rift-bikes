# How to Redeploy on Netlify

## Quick Method: Trigger New Deployment

### Option 1: Clear Cache and Redeploy (Recommended)
1. Go to your Netlify dashboard: https://app.netlify.com
2. Select your site
3. Go to **Deploys** tab
4. Click **"Trigger deploy"** button (top right)
5. Select **"Clear cache and deploy site"**
6. Wait 2-5 minutes for deployment to complete

### Option 2: Push to GitHub (Automatic)
If you've already pushed changes to GitHub:
1. Netlify automatically detects new commits
2. Go to **Deploys** tab
3. You should see a new deployment in progress
4. Wait for it to complete

### Option 3: Manual Redeploy
1. Go to **Deploys** tab
2. Find the latest successful deployment
3. Click the **"..."** menu (three dots)
4. Select **"Redeploy deploy"**
5. Wait for completion

## Verify Deployment

1. Check **Deploys** tab - should show "Published"
2. Visit your site: `https://riftbike.com`
3. Hard refresh: `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)
4. Check browser console for errors

## If Site Still Shows Old Version

1. **Clear browser cache:**
   - Chrome: Settings → Privacy → Clear browsing data
   - Or use Incognito/Private window

2. **Check Netlify deployment status:**
   - Go to Deploys tab
   - Ensure latest deployment is "Published"
   - Check build logs for errors

3. **CDN cache:**
   - Netlify CDN may cache for a few minutes
   - Wait 5-10 minutes and refresh

## Troubleshooting

### Deployment Failed?
- Check build logs in Netlify dashboard
- Look for error messages
- Fix errors locally, commit, and push

### Still Seeing Old Code?
- Verify latest commit is pushed to GitHub
- Check Netlify is connected to correct branch (usually `main`)
- Clear Netlify cache and redeploy

### Need to Rollback?
1. Go to **Deploys** tab
2. Find previous successful deployment
3. Click **"..."** menu
4. Select **"Publish deploy"**

## Quick Commands

If you need to push new changes:
```bash
git add -A
git commit -m "Your changes"
git push
```

Netlify will automatically deploy the new version.
