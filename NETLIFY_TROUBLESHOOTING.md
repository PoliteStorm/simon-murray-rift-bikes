# Netlify Deployment Troubleshooting Guide

## Build Errors Fixed

### Issue 1: Stripe API Version Error
**Error:** `Type '"2024-11-20.acacia"' is not assignable to type '"2023-10-16"'`

**Fix Applied:**
- Updated `app/api/create-payment-intent/route.ts`
- Changed API version from `'2024-11-20.acacia'` to `'2023-10-16'`
- This matches the Stripe package version compatibility

### Issue 2: PaymentElement Options Error
**Error:** `'appearance' does not exist in type 'StripePaymentElementOptions'`

**Fix Applied:**
- Updated `components/StripeCheckout.tsx`
- Removed `appearance` option from PaymentElement
- Kept only `layout: 'tabs'` option

## Current Build Status

✅ **Build Successful**
- All TypeScript errors resolved
- Next.js build completes successfully
- All pages compile correctly

## Testing Build Locally

Before pushing to GitHub, test the build locally:

```bash
npm run build
```

If build succeeds, it will work on Netlify.

## Common Build Issues & Solutions

### TypeScript Errors
1. Check error message in Netlify build logs
2. Fix TypeScript type errors locally
3. Test with `npm run build`
4. Commit and push

### Missing Dependencies
1. Ensure all dependencies are in `package.json`
2. Run `npm install` locally to verify
3. Check `package-lock.json` is committed

### Environment Variables
- Stripe keys not needed (using bank transfer)
- No environment variables required for basic deployment
- Add any needed vars in Netlify dashboard: Site settings → Environment variables

### Next.js Build Issues
- Check `next.config.js` for errors
- Verify `netlify.toml` configuration
- Ensure Node version matches (currently 18)

## Making Changes

### Workflow:
1. Make changes locally
2. Test with `npm run dev` (development)
3. Test build with `npm run build` (production)
4. Commit changes: `git add -A && git commit -m "Description"`
5. Push to GitHub: `git push`
6. Netlify automatically deploys from GitHub

### Quick Commands:
```bash
# Test build locally
npm run build

# Commit and push
git add -A
git commit -m "Your change description"
git push

# Check deployment status
# Go to Netlify dashboard
```

## Netlify Configuration

Current `netlify.toml`:
```toml
[build]
  command = "npm run build"
  publish = ".next"

[[plugins]]
  package = "@netlify/plugin-nextjs"

[build.environment]
  NODE_VERSION = "18"
  NPM_FLAGS = "--legacy-peer-deps"
```

## Deployment Checklist

Before deploying:
- [ ] Local build succeeds (`npm run build`)
- [ ] No TypeScript errors
- [ ] All dependencies in `package.json`
- [ ] `netlify.toml` configured correctly
- [ ] Code committed and pushed to GitHub

## Getting Help

1. Check Netlify build logs in dashboard
2. Compare with local build output
3. Review error messages carefully
4. Test fixes locally before pushing

## Notes

- Stripe code is kept but not actively used (bank transfer is primary)
- All API routes are functional
- Database uses SQLite (file-based, no external DB needed)
- No external services required for basic deployment
