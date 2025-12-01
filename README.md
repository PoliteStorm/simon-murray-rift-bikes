# RIFT - Custom Bike Shop E-commerce

A modern, custom bike shop e-commerce website built with Next.js, featuring Stripe payment integration and a complete ordering system.

## Features

- **View Bikes**: Browse available custom bikes with images/videos
- **Test Drive Booking**: Book test drives for bikes
- **Customization**: Customize bikes with colors, gear specs, and optional upgrades
- **Stripe Payment Integration**: Secure £500 deposit payments via Stripe
- **Order System**: Place orders with full customization options
- **Admin Panel**: Add, edit, and remove bikes and components
- **Warranty Information**: Lifetime frame warranty, 1 year on other components

## Design

- **Color Scheme**: Dark royal green and gold borders throughout
- **Logo**: Volcanic rift design representing biking technology
- **Modern & Fresh**: Clean, minimalist design with gradients and animations

## Getting Started

1. Install dependencies:
```bash
npm install
```

2. Set up environment variables:
Create a `.env.local` file with your Stripe keys:
```
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=pk_test_your_key_here
STRIPE_SECRET_KEY=sk_test_your_key_here
```

Get your Stripe keys from: https://dashboard.stripe.com/apikeys

3. Run the development server:
```bash
npm run dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser

## Database

The application uses SQLite for data storage. The database file (`rift.db`) will be created automatically on first run.

## Pages

- `/` - Home page with video background
- `/bikes` - View all available bikes
- `/bikes/[id]` - Detailed bike view with specifications
- `/test-drive` - Book a test drive
- `/order` - Customize and order a bike (with Stripe payment)
- `/order/success` - Payment success page
- `/admin` - Admin panel for managing bikes

## Stripe Integration

The site uses Stripe for processing the £500 deposit payments. The payment form is styled to match the site's royal green and gold aesthetic.

## Tech Stack

- Next.js 14
- React 18
- TypeScript
- Tailwind CSS
- SQLite
- Stripe (Payment processing)
