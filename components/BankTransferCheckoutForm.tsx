'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';

interface BankTransferCheckoutFormProps {
  bikeId: number;
  bikeName: string;
  basePrice: number;
  deposit: number;
}

export default function BankTransferCheckoutForm({
  bikeId,
  bikeName,
  basePrice,
  deposit
}: BankTransferCheckoutFormProps) {
  const router = useRouter();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [customerInfo, setCustomerInfo] = useState({
    name: '',
    email: '',
    phone: '',
    address: '',
    city: '',
    postcode: '',
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      // Create order
      const response = await fetch('/api/orders', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          bikeId,
          customization: {},
          customerInfo,
          deposit,
          totalPrice: basePrice,
          paymentMethod: 'bank_transfer'
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to create order');
      }

      const data = await response.json();
      
      // Redirect to success page
      router.push(`/order/success?orderId=${data.id}`);
    } catch (err: any) {
      setError(err.message || 'Failed to place order. Please try again.');
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      <div className="bg-rift-royal/30 border border-rift-emerald/50 rounded-xl p-6">
        <h3 className="text-xl font-bold text-white mb-4">Order Information</h3>
        <div className="space-y-2 text-white/80">
          <div className="flex justify-between">
            <span>Bike:</span>
            <span className="text-white font-semibold">{bikeName}</span>
          </div>
          <div className="flex justify-between">
            <span>Total Price:</span>
            <span className="text-rift-gold font-bold">£{basePrice.toLocaleString()}</span>
          </div>
          <div className="flex justify-between">
            <span>Deposit Required:</span>
            <span className="text-rift-gold font-bold">£{deposit.toLocaleString()}</span>
          </div>
        </div>
      </div>

      <div className="bg-rift-royal/30 border border-rift-emerald/50 rounded-xl p-6">
        <h3 className="text-xl font-bold text-white mb-4">Contact Information</h3>
        <p className="text-white/70 text-sm mb-4">
          Please provide your details. You will be contacted at <strong className="text-rift-gold">riftbike@outlook.com</strong>, <strong className="text-rift-gold">WhatsApp: 07817174391</strong>, or <strong className="text-rift-gold">Phone: 01985-844563</strong> to arrange payment via bank transfer and discuss your custom bike specifications.
        </p>
        
        <div className="space-y-4">
          <div>
            <label className="block text-white/80 text-sm mb-2">Full Name *</label>
            <input
              type="text"
              required
              value={customerInfo.name}
              onChange={(e) => setCustomerInfo({ ...customerInfo, name: e.target.value })}
              className="rift-input w-full"
              placeholder="John Doe"
            />
          </div>
          
          <div>
            <label className="block text-white/80 text-sm mb-2">Email Address *</label>
            <input
              type="email"
              required
              value={customerInfo.email}
              onChange={(e) => setCustomerInfo({ ...customerInfo, email: e.target.value })}
              className="rift-input w-full"
              placeholder="john@example.com"
            />
          </div>
          
          <div>
            <label className="block text-white/80 text-sm mb-2">Phone Number *</label>
            <input
              type="tel"
              required
              value={customerInfo.phone}
              onChange={(e) => setCustomerInfo({ ...customerInfo, phone: e.target.value })}
              className="rift-input w-full"
              placeholder="+44 123 456 7890"
            />
          </div>
          
          <div>
            <label className="block text-white/80 text-sm mb-2">Address</label>
            <input
              type="text"
              value={customerInfo.address}
              onChange={(e) => setCustomerInfo({ ...customerInfo, address: e.target.value })}
              className="rift-input w-full"
              placeholder="Street address"
            />
          </div>
          
          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-white/80 text-sm mb-2">City</label>
              <input
                type="text"
                value={customerInfo.city}
                onChange={(e) => setCustomerInfo({ ...customerInfo, city: e.target.value })}
                className="rift-input w-full"
                placeholder="City"
              />
            </div>
            
            <div>
              <label className="block text-white/80 text-sm mb-2">Postcode</label>
              <input
                type="text"
                value={customerInfo.postcode}
                onChange={(e) => setCustomerInfo({ ...customerInfo, postcode: e.target.value })}
                className="rift-input w-full"
                placeholder="Postcode"
              />
            </div>
          </div>
        </div>
      </div>

      <div className="bg-rift-royal/30 border border-rift-emerald/50 rounded-xl p-4">
        <p className="text-white/70 text-sm">
          <strong className="text-rift-gold">Next Steps:</strong> After submitting your order, you will be contacted via email or phone to:
        </p>
        <ul className="text-white/70 text-sm mt-2 ml-4 space-y-1">
          <li>• Provide bank transfer details for the deposit</li>
          <li>• Discuss your custom bike specifications</li>
          <li>• Confirm delivery timeline</li>
        </ul>
        <p className="text-white/60 text-xs mt-3">
          Contact: <strong>riftbike@outlook.com</strong> | <strong>WhatsApp: 07817174391</strong> | <strong>Phone: 01985-844563</strong>
        </p>
      </div>

      {error && (
        <div className="bg-red-900/30 border border-red-500/50 rounded-xl p-4 text-red-200 text-sm">
          {error}
        </div>
      )}

      <div className="flex gap-4">
        <button
          type="button"
          onClick={() => router.back()}
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
          {loading ? 'Placing Order...' : `Place Order (Deposit: £${deposit.toLocaleString()})`}
        </button>
      </div>
    </form>
  );
}
