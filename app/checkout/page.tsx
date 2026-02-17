'use client';

import { useSearchParams, useRouter } from 'next/navigation';
import { Suspense, useEffect, useState } from 'react';
import BankTransferCheckoutForm from '@/components/BankTransferCheckoutForm';

function CheckoutContent() {
  const searchParams = useSearchParams();
  const router = useRouter();
  const bikeId = searchParams.get('bikeId');
  const [bike, setBike] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!bikeId) {
      router.push('/bikes');
      return;
    }

    fetch(`/api/bikes/${bikeId}`)
      .then(res => res.json())
      .then(data => {
        setBike(data);
        setLoading(false);
      })
      .catch(() => {
        router.push('/bikes');
      });
  }, [bikeId, router]);

  if (loading) {
    return (
      <div className="flex-1 flex items-center justify-center bg-rift-dark">
        <p className="text-rift-gold text-xl">Loading...</p>
      </div>
    );
  }

  if (!bike) {
    return (
      <div className="flex-1 flex items-center justify-center bg-rift-dark">
        <div className="text-center">
          <p className="text-white/60 text-lg mb-4">Bike not found.</p>
          <button onClick={() => router.push('/bikes')} className="rift-button">
            Back to Bikes
          </button>
        </div>
      </div>
    );
  }

  const deposit = 500; // £500 fixed deposit

  return (
    <div className="flex-1 py-12 bg-rift-dark">
      <div className="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-4xl font-bold text-white mb-8">Checkout</h1>
        <BankTransferCheckoutForm
          bikeId={bike.id}
          bikeName={bike.name}
          basePrice={bike.basePrice}
          deposit={deposit}
        />
      </div>
    </div>
  );
}

export default function CheckoutPage() {
  return (
    <Suspense fallback={
      <div className="flex-1 flex items-center justify-center bg-rift-dark">
        <p className="text-rift-gold text-xl">Loading...</p>
      </div>
    }>
      <CheckoutContent />
    </Suspense>
  );
}
