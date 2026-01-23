# Payment System Setup Instructions

## Overview
The website uses Stripe for payment processing. The payment system is already integrated in the codebase.

## Required Steps

### 1. Create Stripe Account
1. Go to https://stripe.com
2. Click "Start now" or "Sign in"
3. Create an account or sign in
4. Complete business verification if required

### 2. Get API Keys
1. Log into Stripe Dashboard: https://dashboard.stripe.com
2. Go to Developers → API keys
3. Copy your Publishable key (starts with `pk_`)
4. Copy your Secret key (starts with `sk_`)

### 3. Set Environment Variables
Create a `.env.local` file in the project root with:

```
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_xxxxxxxxxxxxx
STRIPE_SECRET_KEY=sk_test_xxxxxxxxxxxxx
```

**Important:**
- Use test keys (starting with `pk_test_` and `sk_test_`) for development
- Use live keys (starting with `pk_live_` and `sk_live_`) for production
- Never commit `.env.local` to git

### 4. Test the Payment System
1. Start the development server: `npm run dev`
2. Navigate to a bike product page
3. Add to cart and proceed to checkout
4. Use Stripe test card: `4242 4242 4242 4242`
5. Use any future expiry date (e.g., 12/25)
6. Use any 3-digit CVC (e.g., 123)
7. Use any postal code (e.g., 12345)

### 5. Activate Live Mode (Production)
1. In Stripe Dashboard, toggle from "Test mode" to "Live mode"
2. Copy the live API keys
3. Update `.env.local` with live keys
4. Redeploy your application

### 6. Configure Webhooks (Optional but Recommended)
1. In Stripe Dashboard, go to Developers → Webhooks
2. Click "Add endpoint"
3. Enter your production URL: `https://yourdomain.com/api/webhooks/stripe`
4. Select events to listen to:
   - `payment_intent.succeeded`
   - `payment_intent.payment_failed`
5. Copy the webhook signing secret
6. Add to `.env.local`: `STRIPE_WEBHOOK_SECRET=whsec_xxxxxxxxxxxxx`

## Current Implementation
- Payment component: `components/StripeCheckout.tsx`
- API route: `app/api/create-payment-intent/route.ts`
- Currency: GBP (British Pounds)
- Payment methods: All automatic payment methods enabled

## Troubleshooting
- If payment form doesn't load: Check that `NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY` is set correctly
- If payment fails: Check server logs and Stripe Dashboard → Payments for error details
- If keys are invalid: Verify keys are copied correctly and match the mode (test/live)
