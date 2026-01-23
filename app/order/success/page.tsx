'use client';

import { useSearchParams } from 'next/navigation';
import Link from 'next/link';
import { Suspense } from 'react';

function SuccessContent() {
  const searchParams = useSearchParams();
  const orderId = searchParams.get('orderId');

  return (
    <div className="flex-1 flex items-center justify-center bg-rift-dark">
      <div className="text-center p-12 border border-rift-gold rounded-2xl bg-gradient-to-br from-rift-card to-rift-royal max-w-lg backdrop-blur-sm shadow-2xl">
        <div className="w-20 h-20 bg-rift-gold rounded-full flex items-center justify-center mx-auto mb-6">
          <svg className="w-10 h-10 text-rift-dark" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 13l4 4L19 7" />
          </svg>
        </div>
        <h2 className="text-3xl font-bold text-rift-gold mb-4">Order Confirmed!</h2>
        <p className="text-white/90 mb-4 text-lg">
          Your order has been received successfully.
        </p>
        {orderId && (
          <p className="text-white/70 text-sm mb-6">
            Order ID: #{orderId}
          </p>
        )}
        <div className="bg-rift-royal/30 border border-rift-emerald/50 rounded-xl p-4 mb-6">
          <p className="text-white/90 text-sm mb-2">
            <strong className="text-rift-gold">Next Steps:</strong>
          </p>
          <p className="text-white/70 text-sm">
            Simon Murray will contact you shortly via email or phone to:
          </p>
          <ul className="text-white/70 text-sm mt-2 ml-4 space-y-1">
            <li>• Provide bank transfer details for your deposit</li>
            <li>• Discuss your custom bike specifications</li>
            <li>• Confirm delivery timeline</li>
          </ul>
        </div>
        <p className="text-white/60 text-xs mb-8">
          Please keep your order ID for reference. You will receive an email confirmation shortly.
        </p>
        <div className="flex gap-4 justify-center">
          <Link href="/bikes" className="rift-button">
            View More Bikes
          </Link>
          <Link href="/" className="rift-button-secondary">
            Return Home
          </Link>
        </div>
      </div>
    </div>
  );
}

export default function SuccessPage() {
  return (
    <Suspense fallback={
      <div className="flex-1 flex items-center justify-center bg-rift-dark">
        <p className="text-rift-gold text-xl">Loading...</p>
      </div>
    }>
      <SuccessContent />
    </Suspense>
  );
}
