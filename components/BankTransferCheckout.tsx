'use client';

import { useState } from 'react';

interface BankTransferCheckoutProps {
  amount: number;
  orderId?: number;
  customerEmail?: string;
  customerName?: string;
  onSuccess: () => void;
  onCancel: () => void;
}

export default function BankTransferCheckout({ 
  amount, 
  orderId, 
  customerEmail,
  customerName,
  onSuccess, 
  onCancel 
}: BankTransferCheckoutProps) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      // Create order with bank transfer payment method
      const response = await fetch('/api/orders', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          bikeId: orderId,
          customization: {},
          customerInfo: {
            name: customerName || '',
            email: customerEmail || '',
            paymentMethod: 'bank_transfer'
          },
          deposit: amount,
          totalPrice: amount,
          status: 'pending_payment'
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to create order');
      }

      const data = await response.json();
      
      // Send notification to Simon Murray
      await fetch('/api/notify-order', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          orderId: data.id,
          customerName: customerName || '',
          customerEmail: customerEmail || '',
          amount: amount,
          message: `New order #${data.id} received. Customer: ${customerName || 'N/A'} (${customerEmail || 'N/A'}). Deposit: £${amount}. Please contact customer to arrange bank transfer.`
        }),
      });

      onSuccess();
    } catch (err: any) {
      setError(err.message || 'Failed to process order. Please try again.');
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      <div className="bg-rift-royal/30 border border-rift-emerald/50 rounded-xl p-6">
        <h3 className="text-xl font-bold text-white mb-4">Bank Transfer Payment</h3>
        <div className="space-y-4 text-white/80">
          <div>
            <p className="text-sm text-white/60 mb-2">Order Total:</p>
            <p className="text-2xl font-bold text-rift-gold">£{amount.toLocaleString()}</p>
          </div>
          <div className="border-t border-rift-emerald/30 pt-4 space-y-3">
            <p className="text-sm">
              <strong className="text-white">How it works:</strong>
            </p>
            <ul className="text-sm space-y-2 ml-4">
              <li>1. Submit your order below</li>
              <li>2. You'll receive order confirmation</li>
              <li>3. You will be contacted within 24-48 hours at <strong>si@riftbike.com</strong> or <strong>07817174391</strong></li>
              <li>4. Bank transfer details will be provided</li>
              <li>5. Once deposit is received, your build begins</li>
            </ul>
          </div>
          <div className="bg-rift-dark/50 border border-rift-gold/30 rounded-lg p-4 mt-4">
            <p className="text-sm text-white/90">
              <strong className="text-rift-gold">Contact:</strong> si@riftbike.com or 07817174391 - We'll be in touch to arrange payment and discuss your custom specifications.
            </p>
          </div>
        </div>
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
          disabled={loading}
          className="flex-1 rift-button"
        >
          {loading ? 'Processing...' : 'Confirm Order'}
        </button>
      </div>
    </form>
  );
}
