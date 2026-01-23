# Bank Transfer Payment System

## Overview
The website now uses bank transfer payments instead of Stripe. Orders are confirmed and Simon Murray will contact customers to arrange payment and discuss specifications.

## Changes Made

### 1. About Page Updated
- Added warranty section with detailed explanation
- Added payment method section explaining bank transfer and deposit system
- Added charity donation information

### 2. New Bank Transfer Checkout
- Created `components/BankTransferCheckout.tsx`
- Collects customer information (name, email, phone, address)
- Calculates 10% deposit automatically
- Creates order in database
- Redirects to success page

### 3. Checkout Page
- Created `app/checkout/page.tsx`
- Uses bike ID from URL parameter
- Displays BankTransferCheckout component

### 4. Bike Detail Page
- Changed "Add to Cart" button to "Order Now"
- Links directly to checkout page with bike ID

### 5. Order Success Page
- Updated messaging for bank transfer
- Explains that Simon Murray will contact customer
- Lists next steps (bank transfer details, specifications, delivery timeline)

### 6. Orders API
- Updated to accept `paymentMethod` field
- Logs order details for Simon Murray to review
- Console output shows all order information

## Order Flow

1. Customer clicks "Order Now" on bike detail page
2. Redirected to `/checkout?bikeId=X`
3. Fills in contact information
4. Submits order (deposit calculated as 10% of total)
5. Order created in database with status "pending"
6. Order details logged to console
7. Customer sees success page
8. **Simon Murray contacts customer** to:
   - Provide bank transfer details
   - Discuss custom specifications
   - Confirm delivery timeline

## Simon Murray Contact Process

When an order is placed, the following information is logged to the console:

```
=== NEW ORDER - CONTACT SIMON MURRAY ===
Order ID: [order_id]
Customer: [customer_name]
Email: [customer_email]
Phone: [customer_phone]
Bike ID: [bike_id]
Deposit Required: £[deposit_amount]
Total Price: £[total_price]
==========================================
```

**Action Required:** Simon Murray should:
1. Check order logs/console
2. Contact customer via email or phone
3. Provide bank transfer details
4. Discuss bike specifications
5. Confirm delivery timeline

## Database

Orders are stored with:
- `bikeId` - The bike being ordered
- `customization` - JSON of selected options
- `customerInfo` - JSON with name, email, phone, address
- `deposit` - Deposit amount (10% of total)
- `totalPrice` - Full bike price
- `status` - "pending" initially
- `paymentMethod` - "bank_transfer"

## Testing

1. Navigate to a bike detail page
2. Click "Order Now"
3. Fill in contact form
4. Submit order
5. Check console for order log
6. Verify success page displays correctly

## Future Enhancements

- Email notifications to Simon Murray when order is placed
- Email confirmation to customer
- Admin dashboard to view orders
- Order status tracking
- Bank transfer details page

## Notes

- Stripe payment system is still in codebase but not used
- Can be re-enabled by updating checkout flow
- All orders currently use bank transfer method
- Deposit is automatically calculated as 10% of total price
