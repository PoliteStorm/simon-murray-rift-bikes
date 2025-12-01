'use client';

import { useState, useEffect, Suspense } from 'react';
import { useSearchParams } from 'next/navigation';
import dynamic from 'next/dynamic';

const StripeCheckout = dynamic(() => import('@/components/StripeCheckout'), { ssr: false });

interface Bike {
  id: number;
  name: string;
  description: string;
  basePrice: number;
  imageUrl?: string;
  videoUrl?: string;
  category?: string;
}

interface Customization {
  holographicPaint: boolean;
  upgradedGears: boolean;
}

function OrderPageContent() {
  const searchParams = useSearchParams();
  const initialBikeId = searchParams.get('bikeId');
  
  const [allBikes, setAllBikes] = useState<Bike[]>([]);
  const [selectedBike, setSelectedBike] = useState<Bike | null>(null);
  const [customization, setCustomization] = useState<Customization>({
    holographicPaint: false,
    upgradedGears: false,
  });
  const [showPayment, setShowPayment] = useState(false);
  const [orderId, setOrderId] = useState<number | null>(null);
  const [loading, setLoading] = useState(true);
  const [submitted, setSubmitted] = useState(false);

  useEffect(() => {
    fetchBikes();
  }, []);

  useEffect(() => {
    if (initialBikeId && allBikes.length > 0) {
      const bike = allBikes.find(b => b.id === parseInt(initialBikeId));
      if (bike) {
        setSelectedBike(bike);
      } else if (allBikes.length > 0) {
        setSelectedBike(allBikes[0]);
      }
    } else if (allBikes.length > 0 && !selectedBike) {
      setSelectedBike(allBikes[0]);
    }
  }, [initialBikeId, allBikes]);

  const fetchBikes = async () => {
    try {
      const response = await fetch('/api/bikes');
      const data = await response.json();
      setAllBikes(data);
      if (data.length > 0 && !selectedBike) {
        const bike = initialBikeId ? data.find((b: Bike) => b.id === parseInt(initialBikeId)) : data[0];
        setSelectedBike(bike || data[0]);
      }
    } catch (error) {
      console.error('Error fetching bikes:', error);
    } finally {
      setLoading(false);
    }
  };

  const calculateTotal = () => {
    if (!selectedBike) return 0;
    let total = selectedBike.basePrice;
    if (customization.holographicPaint) total += 500;
    if (customization.upgradedGears) total += 300;
    return total;
  };

  const handleBuyNow = async () => {
    if (!selectedBike) return;
    
    try {
      const response = await fetch('/api/orders', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          bikeId: selectedBike.id,
          customization,
          customerInfo: {},
          deposit: 500,
          totalPrice: calculateTotal(),
        }),
      });
      
      if (response.ok) {
        const data = await response.json();
        setOrderId(data.id);
        setShowPayment(true);
      }
    } catch (error) {
      console.error('Error creating order:', error);
      alert('Error creating order. Please try again.');
    }
  };

  const handlePaymentSuccess = () => {
    setSubmitted(true);
    setShowPayment(false);
  };

  const handlePaymentCancel = () => {
    setShowPayment(false);
  };

  const handleDownloadVideo = () => {
    if (selectedBike?.videoUrl) {
      const link = document.createElement('a');
      link.href = selectedBike.videoUrl;
      link.download = `${selectedBike.name.replace(/\s+/g, '-')}-video.mp4`;
      link.click();
    }
  };

  if (loading) {
    return (
      <div className="flex-1 flex items-center justify-center bg-rift-dark">
        <p className="text-rift-gold text-xl">Loading...</p>
      </div>
    );
  }

  if (submitted) {
    return (
      <div className="flex-1 flex items-center justify-center bg-rift-dark">
        <div className="text-center p-12 border border-rift-gold rounded-2xl bg-gradient-to-br from-rift-card to-rift-royal max-w-lg backdrop-blur-sm shadow-2xl">
          <div className="w-16 h-16 bg-rift-gold rounded-full flex items-center justify-center mx-auto mb-6">
            <svg className="w-8 h-8 text-rift-dark" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 13l4 4L19 7" />
            </svg>
          </div>
          <h2 className="text-3xl font-bold text-rift-gold mb-4">Order Placed Successfully</h2>
          <p className="text-white/90 mb-4 text-lg">
            Your order has been received. A £500 deposit is required to secure your custom bike.
          </p>
          <p className="text-white/70 text-sm mb-8">
            We'll contact you shortly to arrange payment and discuss your specifications.
          </p>
          <a href="/bikes" className="rift-button inline-block">
            View More Bikes
          </a>
        </div>
      </div>
    );
  }

  if (!selectedBike) {
    return (
      <div className="flex-1 flex items-center justify-center bg-rift-dark">
        <div className="text-center">
          <p className="text-white/60 text-lg mb-4">No bikes available.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="flex-1 bg-rift-dark py-8">
      <div className="max-w-[1800px] mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-12 gap-6 h-[calc(100vh-8rem)]">
          {/* Left Sidebar - All Bikes */}
          <div className="col-span-12 lg:col-span-3 flex flex-col">
            <h2 className="text-2xl font-bold text-white mb-4">All Bikes</h2>
            <div className="flex-1 overflow-hidden">
              <div className="h-full overflow-y-auto scrollbar-modern">
                <div className="space-y-3 pr-2">
                  {allBikes.map((bike) => (
                    <div
                      key={bike.id}
                      onClick={() => setSelectedBike(bike)}
                      className={`p-4 rounded-lg border cursor-pointer transition-all ${
                        selectedBike.id === bike.id
                          ? 'bg-rift-card border-rift-gold border-2'
                          : 'bg-rift-card/50 border-rift-emerald/50 hover:border-rift-gold/50'
                      }`}
                    >
                      <div className="flex justify-between items-start mb-2">
                        <h3 className="text-white font-semibold">{bike.name}</h3>
                      </div>
                      <div className="flex justify-between items-center">
                        <span className="text-rift-gold font-bold">£{bike.basePrice.toLocaleString()}</span>
                        <span className="text-sm text-white/60 flex items-center gap-1">
                          <svg className="w-4 h-4 text-rift-gold" fill="currentColor" viewBox="0 0 20 20">
                            <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                          </svg>
                          In Stock
                        </span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>

          {/* Center - Video Player */}
          <div className="col-span-12 lg:col-span-5 flex flex-col">
            <div className="aspect-video bg-black rounded-lg overflow-hidden mb-4 flex items-center justify-center">
              {selectedBike.videoUrl ? (
                <video
                  key={selectedBike.id}
                  className="w-full h-full object-cover"
                  controls
                  autoPlay
                  loop
                  muted
                  playsInline
                  preload="auto"
                  src={selectedBike.videoUrl}
                  onCanPlay={(e) => {
                    const video = e.currentTarget;
                    video.play().catch(() => {
                      // Autoplay prevented
                    });
                  }}
                  onLoadedMetadata={(e) => {
                    const video = e.currentTarget;
                    video.play().catch(() => {
                      // Autoplay prevented
                    });
                  }}
                >
                  Your browser does not support the video tag.
                </video>
              ) : (
                <div className="w-full h-full flex items-center justify-center bg-gradient-to-br from-rift-royal to-emerald-950">
                  <div className="text-center">
                    <div className="w-24 h-24 border-2 border-rift-gold/30 rounded-full mx-auto mb-4 flex items-center justify-center">
                      <svg className="w-12 h-12 text-rift-gold/50" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" />
                      </svg>
                    </div>
                    <p className="text-rift-gold/70 text-sm">Video Coming Soon</p>
                  </div>
                </div>
              )}
            </div>

            {/* Download 4K Brochure Section */}
            <div className="bg-rift-card border border-rift-emerald rounded-lg p-6">
              <h3 className="text-lg font-bold text-white mb-3">Download 4K Brochure</h3>
              <p className="text-white/70 text-sm mb-4">
                Save the full 4K video to your device for offline viewing.
              </p>
              <div className="flex gap-3">
                <button
                  onClick={() => {
                    if (selectedBike.videoUrl) {
                      window.open(selectedBike.videoUrl, '_blank');
                    }
                  }}
                  className="flex-1 rift-button flex items-center justify-center gap-2"
                  disabled={!selectedBike.videoUrl}
                >
                  <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M14.752 11.168l-3.197-2.132A1 1 0 0010 9.87v4.263a1 1 0 001.555.832l3.197-2.132a1 1 0 000-1.664z" />
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                  Open Video
                </button>
                <button
                  onClick={handleDownloadVideo}
                  className="flex-1 rift-button-secondary flex items-center justify-center gap-2"
                  disabled={!selectedBike.videoUrl}
                >
                  <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                  </svg>
                  Download (Desktop)
                </button>
              </div>
              <p className="text-white/50 text-xs mt-3">
                On mobile: Tap "Open Video" then use your browser's share/save option to download.
              </p>
            </div>
          </div>

          {/* Right Sidebar - Product Details */}
          <div className="col-span-12 lg:col-span-4 flex flex-col">
            <div className="bg-rift-card border border-rift-emerald rounded-lg p-6 flex-1 overflow-y-auto scrollbar-modern">
              {/* Price */}
              <div className="text-4xl font-bold text-rift-gold mb-4">
                £{selectedBike.basePrice.toLocaleString()}
              </div>

              {/* Stock Status */}
              <div className="bg-rift-royal border border-rift-emerald rounded-lg p-3 mb-6">
                <div className="flex items-center gap-2 text-white">
                  <svg className="w-5 h-5 text-rift-gold" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                  </svg>
                  <span>In Stock - Test Ride Available</span>
                </div>
              </div>

              {/* Available Upgrades */}
              <div className="mb-6">
                <h3 className="text-lg font-bold text-white mb-4">Available Upgrades</h3>
                <div className="space-y-3">
                  <label className="flex items-start gap-3 p-3 bg-rift-royal/30 border border-rift-emerald/30 rounded-lg cursor-pointer hover:border-rift-gold/50 transition-all">
                    <input
                      type="checkbox"
                      checked={customization.holographicPaint}
                      onChange={(e) => setCustomization({ ...customization, holographicPaint: e.target.checked })}
                      className="mt-1 w-5 h-5 text-rift-gold bg-rift-royal border-rift-emerald rounded focus:ring-rift-gold"
                    />
                    <div className="flex-1">
                      <div className="text-white font-semibold">Holographic Paint</div>
                      <div className="text-white/60 text-sm">Premium color-shifting finish</div>
                    </div>
                    <div className="text-rift-gold font-bold">+£500</div>
                  </label>

                  <label className="flex items-start gap-3 p-3 bg-rift-royal/30 border border-rift-emerald/30 rounded-lg cursor-pointer hover:border-rift-gold/50 transition-all">
                    <input
                      type="checkbox"
                      checked={customization.upgradedGears}
                      onChange={(e) => setCustomization({ ...customization, upgradedGears: e.target.checked })}
                      className="mt-1 w-5 h-5 text-rift-gold bg-rift-royal border-rift-emerald rounded focus:ring-rift-gold"
                    />
                    <div className="flex-1">
                      <div className="text-white font-semibold">Upgraded Gears</div>
                      <div className="text-white/60 text-sm">Professional-grade components</div>
                    </div>
                    <div className="text-rift-gold font-bold">+£300</div>
                  </label>
                </div>
              </div>

              {/* Payment Section */}
              {showPayment ? (
                <div className="space-y-4">
                  <div className="bg-rift-gold/20 border border-rift-gold/50 rounded-lg p-4">
                    <p className="text-white text-sm mb-2">Order placed! Complete your £500 deposit:</p>
                  </div>
                  <StripeCheckout
                    amount={500}
                    orderId={orderId || undefined}
                    customerEmail=""
                    onSuccess={handlePaymentSuccess}
                    onCancel={handlePaymentCancel}
                  />
                </div>
              ) : (
                <>
                  {/* Action Buttons */}
                  <div className="space-y-3 mb-4">
                    <button
                      onClick={handleBuyNow}
                      className="w-full rift-button text-lg py-4"
                    >
                      Buy Now
                    </button>
                    <a
                      href={`/order/customize?bikeId=${selectedBike.id}`}
                      className="block w-full rift-button-secondary text-lg py-4 text-center"
                    >
                      Full Customization
                    </a>
                  </div>

                  {/* Shipping Info */}
                  <div className="text-white/60 text-sm space-y-1 pt-4 border-t border-rift-emerald/30">
                    <p>Standard spec bikes ship immediately.</p>
                    <p>Custom builds in 30-40 days.</p>
                  </div>
                </>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default function OrderPage() {
  return (
    <Suspense fallback={
      <div className="flex-1 flex items-center justify-center bg-rift-dark">
        <p className="text-rift-gold text-xl">Loading...</p>
      </div>
    }>
      <OrderPageContent />
    </Suspense>
  );
}
