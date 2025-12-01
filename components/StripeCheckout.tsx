'use client';

import { loadStripe } from '@stripe/stripe-js';
import { Elements, PaymentElement, useStripe, useElements } from '@stripe/react-stripe-js';
import { useState, useEffect } from 'react';

const stripePromise = loadStripe(process.env.NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY || '');

interface StripeCheckoutProps {
  amount: number;
  orderId?: number;
  customerEmail?: string;
  onSuccess: () => void;
  onCancel: () => void;
}

function CheckoutForm({ amount, orderId, customerEmail, onSuccess, onCancel }: StripeCheckoutProps) {
  const stripe = useStripe();
  const elements = useElements();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!stripe || !elements) {
      return;
    }

    setLoading(true);
    setError(null);

    const { error: submitError } = await elements.submit();
    if (submitError) {
      setError(submitError.message || 'An error occurred');
      setLoading(false);
      return;
    }

    const { error: confirmError } = await stripe.confirmPayment({
      elements,
      confirmParams: {
        return_url: `${window.location.origin}/order/success?orderId=${orderId}`,
      },
      redirect: 'if_required',
    });

    if (confirmError) {
      setError(confirmError.message || 'Payment failed');
      setLoading(false);
    } else {
      onSuccess();
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      <div className="bg-rift-royal/30 border border-rift-emerald/50 rounded-xl p-6">
        <PaymentElement 
          options={{
            layout: 'tabs',
            appearance: {
              theme: 'night',
              variables: {
                colorPrimary: '#fbbf24',
                colorBackground: '#0f3d32',
                colorText: '#ffffff',
                colorDanger: '#ef4444',
                fontFamily: 'system-ui, sans-serif',
                borderRadius: '12px',
              },
            },
          }}
        />
      </div>

      {error && (
        <div className="bg-red-900/30 border border-red-500/50 rounded-xl p-4 text-red-200 text-sm">
          {error}
        </div>
      )}

      <div className="flex gap-4">
        <button
          type="button"
          onClick={onCancel}
          className="flex-1 rift-button-secondary"
          disabled={loading}
        >
          Cancel
        </button>
        <button
          type="submit"
          disabled={!stripe || loading}
          className="flex-1 rift-button"
        >
          {loading ? 'Processing...' : `Pay £${amount.toLocaleString()}`}
        </button>
      </div>
    </form>
  );
}

export default function StripeCheckout({ amount, orderId, customerEmail, onSuccess, onCancel }: StripeCheckoutProps) {
  const [clientSecret, setClientSecret] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/create-payment-intent', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ amount, orderId, customerEmail }),
    })
      .then((res) => res.json())
      .then((data) => {
        setClientSecret(data.clientSecret);
        setLoading(false);
      })
      .catch((error) => {
        console.error('Error creating payment intent:', error);
        setLoading(false);
      });
  }, [amount, orderId, customerEmail]);

  if (loading) {
    return (
      <div className="flex items-center justify-center p-12">
        <div className="animate-pulse text-rift-gold">Loading payment form...</div>
      </div>
    );
  }

  if (!clientSecret) {
    return (
      <div className="bg-red-900/30 border border-red-500/50 rounded-xl p-4 text-red-200">
        Failed to initialize payment. Please try again.
      </div>
    );
  }

  const options = {
    clientSecret,
    appearance: {
      theme: 'night' as const,
      variables: {
        colorPrimary: '#fbbf24',
        colorBackground: '#0f3d32',
        colorText: '#ffffff',
      },
    },
  };

  return (
    <Elements stripe={stripePromise} options={options}>
      <CheckoutForm 
        amount={amount} 
        orderId={orderId} 
        customerEmail={customerEmail}
        onSuccess={onSuccess}
        onCancel={onCancel}
      />
    </Elements>
  );
}

