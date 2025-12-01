'use client';

import { useState, useEffect } from 'react';
import { useParams } from 'next/navigation';
import Link from 'next/link';

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

  useEffect(() => {
    if (bikeId) {
      fetchBike(Number(bikeId));
    }
  }, [bikeId]);

  const fetchBike = async (id: number) => {
    try {
      const response = await fetch(`/api/bikes/${id}`);
      const data = await response.json();
      setBike(data);
      if (data.specifications) {
        setSpecs(JSON.parse(data.specifications));
      }
    } catch (error) {
      console.error('Error fetching bike:', error);
    } finally {
      setLoading(false);
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
          {/* Image/Video */}
          <div className="rift-card overflow-hidden">
            <div className="aspect-square bg-gradient-to-br from-rift-royal to-emerald-950 flex items-center justify-center">
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

          {/* Bike Info */}
          <div className="rift-card p-8">
            <div className="flex items-center justify-between mb-4">
              <h1 className="text-3xl font-bold text-white">{bike.name}</h1>
              {bike.category && (
                <span className="text-sm bg-rift-gold/20 text-rift-gold px-3 py-1 rounded-full border border-rift-gold/30">
                  {bike.category}
                </span>
              )}
            </div>
            <p className="text-white/80 mb-6">{bike.description}</p>
            <div className="mb-6">
              <div className="text-4xl font-bold text-rift-gold mb-2">£{bike.basePrice.toLocaleString()}</div>
              <div className="text-white/80 text-sm mb-4">✓ In Stock - Test Ride Available</div>
            </div>
            <div className="space-y-3 mb-6">
              <Link 
                href={`/order?bikeId=${bike.id}`}
                className="block w-full rift-button text-center"
              >
                Buy Now
              </Link>
              <Link 
                href={`/order?bikeId=${bike.id}`}
                className="block w-full rift-button-secondary text-center"
              >
                Full Customization
              </Link>
            </div>
            <div className="text-white/60 text-sm space-y-1">
              <p>Standard spec bikes ship immediately.</p>
              <p>Custom builds in 30-40 days.</p>
            </div>
          </div>
        </div>

        {/* Specifications */}
        {specs && (
          <div className="bg-rift-card border border-rift-emerald rounded-lg p-8">
            <h2 className="text-2xl font-bold text-white mb-6">Specifications</h2>
            <div className="grid md:grid-cols-2 gap-6">
              {Object.entries(specs).map(([key, value]) => (
                <div key={key} className="border-b border-rift-emerald pb-2">
                  <div className="text-rift-gold font-semibold text-sm mb-1">
                    {key.replace(/([A-Z])/g, ' $1').replace(/^./, str => str.toUpperCase())}
                  </div>
                  <div className="text-white/80 text-sm">{String(value)}</div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

