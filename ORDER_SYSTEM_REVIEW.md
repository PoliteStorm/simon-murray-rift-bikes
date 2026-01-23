# Order System & Account Integration Review

## Current State

### ✅ Completed
1. **Bike Database**: 2 bikes (CYCLONE-3rd and EM19) with specifications from Excel files
2. **Shop Page**: Lists bikes with videos/images as display
3. **Bike Detail Page**: Shows individual bike with:
   - Main image/video
   - Image gallery (if multiple images)
   - Full specifications
   - Paint options (Standard, Holographic, 3K Gloss Black, 3K Gloss Green)
   - Add to Cart button
4. **Custom Order Page**: Removed (as requested)
5. **Stripe Integration**: Payment system in place

### Current Order System

#### Database Schema
```sql
orders (
  id INTEGER PRIMARY KEY,
  bikeId INTEGER,
  customization TEXT,      -- JSON string
  customerInfo TEXT,        -- JSON string (no user accounts yet)
  deposit REAL,
  totalPrice REAL,
  status TEXT DEFAULT 'pending',
  createdAt DATETIME
)
```

#### Payment Flow
1. User selects bike and paint options
2. Creates order via `/api/orders` POST
3. Stripe PaymentIntent created via `/api/create-payment-intent`
4. Stripe Checkout component handles payment
5. Success redirects to `/bikes?orderId=...`

### What's Missing for Account Integration

#### 1. User Authentication System
**Options:**
- **NextAuth.js** (Recommended)
  - Supports multiple providers (Google, Email, etc.)
  - Session management
  - Easy integration with Next.js
  - Install: `npm install next-auth`

- **Clerk** (Alternative)
  - Full-featured auth solution
  - Built-in UI components
  - User management dashboard
  - More expensive but easier setup

- **Custom Auth**
  - Full control but more work
  - Need to handle sessions, passwords, etc.

#### 2. User Database Table
```sql
users (
  id INTEGER PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  name TEXT,
  passwordHash TEXT,        -- if using email/password
  provider TEXT,            -- 'email', 'google', etc.
  providerId TEXT,          -- external ID
  createdAt DATETIME,
  updatedAt DATETIME
)

user_profiles (
  userId INTEGER PRIMARY KEY,
  phone TEXT,
  address TEXT,
  city TEXT,
  postcode TEXT,
  country TEXT,
  FOREIGN KEY (userId) REFERENCES users(id)
)
```

#### 3. Order System Updates
- Link orders to user accounts
- Add user order history page
- Email notifications
- Order tracking

#### 4. Cart System
Currently missing - need to:
- Add cart table or session storage
- Cart page (`/cart`)
- Add to cart functionality
- Checkout flow

## Recommended Implementation Steps

### Phase 1: User Authentication (NextAuth.js)
1. Install NextAuth.js
2. Configure providers (Email, Google)
3. Create user table
4. Add login/signup pages
5. Protect routes (admin, orders)

### Phase 2: Cart System
1. Create cart table or use session storage
2. Implement add to cart on bike detail page
3. Create cart page with items
4. Update checkout flow

### Phase 3: Order Management
1. Link orders to users
2. Create user dashboard (`/account`)
3. Order history page
4. Order status updates
5. Email notifications

### Phase 4: Enhanced Features
1. Save addresses
2. Order tracking
3. Wishlist
4. Reviews/ratings

## Current Files to Review

- `/app/api/orders/route.ts` - Order creation endpoint
- `/app/api/create-payment-intent/route.ts` - Stripe payment
- `/components/StripeCheckout.tsx` - Payment form
- `/lib/db.ts` - Database schema

## Environment Variables Needed

```env
# Stripe (already configured)
STRIPE_SECRET_KEY=sk_...
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_...

# NextAuth.js (if implementing)
NEXTAUTH_URL=http://localhost:3000
NEXTAUTH_SECRET=your-secret-key

# Email (for notifications)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASS=your-password
```

## Next Steps

1. **Decide on auth provider**: NextAuth.js recommended
2. **Design user flow**: Login, signup, account page
3. **Implement cart system**: Before or after auth
4. **Update order system**: Link to users
5. **Add email notifications**: Order confirmations
