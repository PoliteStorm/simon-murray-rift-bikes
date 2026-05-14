'use client';

import { useState, useEffect } from 'react';
import { useParams } from 'next/navigation';
import Link from 'next/link';
import PartnerLogos from '@/components/PartnerLogos';

interface Bike {
  id: number;
  name: string;
  description: string;
  basePrice: number;
  imageUrl?: string;
  videoUrl?: string;
  category?: string;
  specifications?: string;
}

export default function BikeDetailPage() {
  const params = useParams();
  const bikeId = params.id;
  const [bike, setBike] = useState<Bike | null>(null);
  const [loading, setLoading] = useState(true);
  const [specs, setSpecs] = useState<any>(null);
  const [holographicPaint, setHolographicPaint] = useState(false);
  const [totalPrice, setTotalPrice] = useState(0);

  useEffect(() => {
    if (bikeId) {
      fetchBike(Number(bikeId));
    }
  }, [bikeId]);

  const fetchBike = async (id: number) => {
    try {
      const response = await fetch(`/api/bikes/${id}`);
      if (!response.ok) {
        throw new Error(`Failed to fetch bike: ${response.status}`);
      }
      const data = await response.json();

      if (data.error) {
        throw new Error(data.error);
      }

      if (!data || !data.name || data.basePrice === undefined) {
        throw new Error('Invalid bike data received');
      }

      setBike(data);
      setTotalPrice(data.basePrice);
      if (data.specifications) {
        try {
          setSpecs(JSON.parse(data.specifications));
        } catch (parseError) {
          console.error('Error parsing specifications:', parseError);
          setSpecs(null);
        }
      }
    } catch (error) {
      console.error('Error fetching bike:', error);
      setBike(null);
    } finally {
      setLoading(false);
    }
  };

  const handleHolographicChange = (checked: boolean) => {
    setHolographicPaint(checked);
    if (bike) {
      setTotalPrice(checked ? bike.basePrice + 250 : bike.basePrice);
    }
  };

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
          <Link href="/bikes" className="rift-button">Back to Bikes</Link>
        </div>
      </div>
    );
  }

  return (
    <div className="flex-1 py-12 bg-rift-dark">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <Link href="/bikes" className="text-rift-gold hover:text-yellow-400 mb-6 inline-block">
          ← Back to Bikes
        </Link>

        <div className="grid md:grid-cols-2 gap-8 mb-8">
          {/* Image/Video Gallery */}
          <div className="space-y-4">
            <div className="rift-card overflow-hidden">
              <div className="aspect-square bg-gradient-to-br from-rift-royal to-emerald-950 flex items-center justify-center relative">
                {bike.videoUrl ? (
                  <video
                    key={bike.id}
                    className="w-full h-full object-cover"
                    controls
                    autoPlay
                    loop
                    muted
                    playsInline
                    style={{ maxHeight: '100%', maxWidth: '100%' }}
                  >
                    <source src={bike.videoUrl} type="video/mp4" />
                  </video>
                ) : bike.imageUrl ? (
                  <img src={bike.imageUrl} alt={bike.name} className="w-full h-full object-contain" />
                ) : (
                  <div className="text-center p-8">
                    <div className="w-32 h-32 border-2 border-rift-gold/30 rounded-full mx-auto mb-4 flex items-center justify-center">
                      <svg className="w-16 h-16 text-rift-gold/50" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                      </svg>
                    </div>
                    <p className="text-rift-gold/70 text-sm">Image Coming Soon</p>
                  </div>
                )}
              </div>
            </div>
          </div>

          {/* Bike Info */}
          <div className="rift-card p-8">
            <div className="flex items-center justify-between mb-2">
              <h1 className="text-3xl font-bold text-white tracking-tight">{bike.name}</h1>
              {bike.category && (
                <span className="text-sm bg-rift-gold/20 text-rift-gold px-3 py-1 rounded-full border border-rift-gold/30">
                  {bike.category}
                </span>
              )}
            </div>
            <p className="text-rift-gold/90 text-xs tracking-[0.18em] uppercase font-medium mb-5">
              Hand built just for you<span className="opacity-70">…</span>
            </p>
            <p className="text-white/80 mb-6">{bike.description}</p>
            <div className="mb-6">
              <div className="text-4xl font-bold text-rift-gold mb-2">
                £{totalPrice.toLocaleString()}
              </div>
              <div className="text-white/60 text-sm">
                Base Price: £{bike.basePrice.toLocaleString()}
                {holographicPaint && <span className="text-rift-gold"> + £250 (Holographic Paint)</span>}
              </div>
              <div className="text-white/80 text-sm mt-2 mb-4">✓ Available to Order</div>
            </div>

            {/* Paint Options */}
            <div className="mb-6">
              <h3 className="text-lg font-bold text-white mb-3">Paint Options</h3>
              <div className="space-y-2">
                <label className="flex items-center gap-3 p-3 rounded-lg cursor-pointer transition-all bg-rift-royal/30 border border-rift-emerald/30 hover:border-rift-gold/50">
                  <input
                    type="radio"
                    name="paint"
                    className="w-5 h-5 text-rift-gold bg-rift-royal border-rift-emerald rounded-full focus:ring-rift-gold"
                    defaultChecked
                    onChange={() => handleHolographicChange(false)}
                  />
                  <div className="flex-1">
                    <div className="text-white font-semibold text-sm">Standard Paint</div>
                    <div className="text-white/60 text-xs">Included — Immediate availability</div>
                  </div>
                  <div className="text-rift-gold font-bold text-sm">£0</div>
                </label>
                <label className="flex items-center gap-3 p-3 rounded-lg cursor-pointer transition-all bg-rift-royal/30 border border-rift-emerald/30 hover:border-rift-gold/50">
                  <input
                    type="radio"
                    name="paint"
                    className="w-5 h-5 text-rift-gold bg-rift-royal border-rift-emerald rounded-full focus:ring-rift-gold"
                    onChange={() => handleHolographicChange(true)}
                  />
                  <div className="flex-1">
                    <div className="text-white font-semibold text-sm">Holographic Paint</div>
                    <div className="text-white/60 text-xs">Premium colour-shifting finish — additional wait time required</div>
                  </div>
                  <div className="text-rift-gold font-bold text-sm">+£250</div>
                </label>
              </div>
              <div className="mt-3 bg-rift-royal/20 border border-rift-gold/30 rounded-lg p-3">
                <p className="text-white/80 text-xs">
                  <strong className="text-rift-gold">Note:</strong> Custom paint jobs require additional wait time. Timeline will be confirmed during order processing.
                </p>
              </div>
            </div>

            <div className="space-y-3 mb-6">
              <Link href={`/checkout?bikeId=${bike.id}`} className="block w-full rift-button text-center">
                Order Now
              </Link>
              <Link href="/contact" className="block w-full rift-button-secondary text-center">
                Talk to Simon First
              </Link>
            </div>
            <div className="text-white/60 text-sm space-y-1">
              <p>Standard paint bikes ship immediately.</p>
              <p>Holographic paint option available — additional wait time applies.</p>
            </div>
          </div>
        </div>

        {/* Specifications */}
        {specs && (
          <div className="bg-rift-card border border-rift-emerald rounded-lg p-8">
            <h2 className="text-2xl font-bold text-white mb-6">Specifications</h2>
            <div className="grid md:grid-cols-2 gap-6">
              {Object.entries(specs)
                .filter(([key]) => !['specFile', 'model', 'images', 'undefined', 'specSheetUrl'].includes(key))
                .map(([key, value]) => {
                  const displayKey = key
                    .replace(/([A-Z])/g, ' $1')
                    .replace(/^./, (str) => str.toUpperCase())
                    .trim();
                  return (
                    <div key={key} className="border-b border-rift-emerald/30 pb-3 flex items-start gap-2">
                      <span className="text-rift-gold mt-0.5">✓</span>
                      <div>
                        <div className="text-rift-gold font-semibold text-sm mb-1">{displayKey}</div>
                        <div className="text-white/80 text-sm">{String(value)}</div>
                      </div>
                    </div>
                  );
                })}
            </div>
          </div>
        )}

        {/* Partner Logos */}
        <div className="mt-8">
          <PartnerLogos variant="compact" />
        </div>
      </div>
    </div>
  );
}
