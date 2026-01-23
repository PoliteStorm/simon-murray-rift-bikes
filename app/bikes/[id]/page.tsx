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
      
      // Check if response is an error object
      if (data.error) {
        throw new Error(data.error);
      }
      
      // Ensure required fields exist
      if (!data || !data.name || data.basePrice === undefined) {
        throw new Error('Invalid bike data received');
      }
      
      setBike(data);
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

  const isRiftRapid = bike.name === 'RIFT Rapid' || bike.name === 'Rift Rapid';
  const isRiftClimb = bike.name === 'RIFT Climb';

  return (
    <div className="flex-1 py-12 bg-rift-dark">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <Link href="/bikes" className="text-rift-gold hover:text-yellow-400 mb-6 inline-block">
          ← Back to Bikes
        </Link>
        
        <div className="grid md:grid-cols-2 gap-8 mb-8">
          {/* Image/Video Gallery */}
          <div className="space-y-4">
            {/* Main Image/Video */}
            <div className="rift-card overflow-hidden">
              <div className="aspect-square bg-gradient-to-br from-rift-royal to-emerald-950 flex items-center justify-center relative">
                {/* For RIFT Climb: Always show video if available, no images */}
                {isRiftClimb && bike.videoUrl ? (
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
                ) : bike.videoUrl && !isRiftClimb ? (
                  /* For other bikes: Show video if available */
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
                ) : bike.imageUrl && !isRiftClimb ? (
                  /* For other bikes: Show image if no video */
                  <>
                    <img src={bike.imageUrl} alt={bike.name} className="w-full h-full object-contain" />
                    {isRiftRapid && (
                      <div className="absolute top-4 right-4 w-16 h-16 bg-white z-10"></div>
                    )}
                  </>
                ) : (
                  /* Placeholder if no media */
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
            
            {/* Image Gallery Thumbnails */}
            {specs && specs.images && Array.isArray(specs.images) && specs.images.length > 1 && !isRiftRapid && !isRiftClimb && (
              <div className="grid grid-cols-3 gap-2">
                {specs.images.slice(0, 6).map((img: string, idx: number) => (
                  <div key={idx} className="rift-card overflow-hidden aspect-square cursor-pointer hover:border-rift-gold transition-all">
                    <img src={img} alt={`${bike.name} ${idx + 1}`} className="w-full h-full object-cover" />
                  </div>
                ))}
              </div>
            )}
            {/* For Rift Rapid, only show first image with white overlay */}
            {isRiftRapid && specs && specs.images && Array.isArray(specs.images) && specs.images.length > 0 && (
              <div className="grid grid-cols-3 gap-2">
                <div className="rift-card overflow-hidden aspect-square cursor-pointer hover:border-rift-gold transition-all relative">
                  <img src={specs.images[0]} alt={`${bike.name} 1`} className="w-full h-full object-cover" />
                  <div className="absolute top-2 right-2 w-12 h-12 bg-white z-10"></div>
                </div>
              </div>
            )}
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
              <div className="text-4xl font-bold text-rift-gold mb-2">
                £{bike.basePrice ? bike.basePrice.toLocaleString() : 'N/A'}
              </div>
              <div className="text-white/80 text-sm mb-4">✓ In Stock - Test Ride Available</div>
            </div>
            
            {/* Paint Options */}
            <div className="mb-6">
              <h3 className="text-lg font-bold text-white mb-3">Paint Options</h3>
              <div className="space-y-2">
                <label className="flex items-center gap-3 p-3 rounded-lg cursor-pointer transition-all bg-rift-royal/30 border border-rift-emerald/30 hover:border-rift-gold/50">
                  <input
                    type="checkbox"
                    className="w-5 h-5 text-rift-gold bg-rift-royal border-rift-emerald rounded focus:ring-rift-gold"
                    defaultChecked
                  />
                  <div className="flex-1">
                    <div className="text-white font-semibold text-sm">Standard Paint</div>
                    <div className="text-white/60 text-xs">Included - Immediate availability</div>
                  </div>
                  <div className="text-rift-gold font-bold text-sm">£0</div>
                </label>
                <label className="flex items-center gap-3 p-3 rounded-lg cursor-pointer transition-all bg-rift-royal/30 border border-rift-emerald/30 hover:border-rift-gold/50">
                  <input
                    type="checkbox"
                    className="w-5 h-5 text-rift-gold bg-rift-royal border-rift-emerald rounded focus:ring-rift-gold"
                  />
                  <div className="flex-1">
                    <div className="text-white font-semibold text-sm">Holographic Paint</div>
                    <div className="text-white/60 text-xs">Premium color-shifting finish - Additional wait time required</div>
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
            </div>
            <div className="text-white/60 text-sm space-y-1">
              <p>Standard paint bikes ship immediately.</p>
              <p>Holographic paint option available - additional wait time applies.</p>
            </div>
          </div>
        </div>

        {/* Specifications */}
        {specs && (
          <div className="bg-rift-card border border-rift-emerald rounded-lg p-8">
            <h2 className="text-2xl font-bold text-white mb-6">Specifications</h2>
            <div className="grid md:grid-cols-2 gap-6">
              {Object.entries(specs)
                .filter(([key]) => key !== 'specFile' && key !== 'model' && key !== 'images' && key !== 'undefined')
                .map(([key, value]) => {
                  const displayKey = key
                    .replace(/([A-Z])/g, ' $1')
                    .replace(/^./, str => str.toUpperCase())
                    .trim();
                  return (
                    <div key={key} className="border-b border-rift-emerald/30 pb-3">
                      <div className="text-rift-gold font-semibold text-sm mb-1">
                        {displayKey}
                      </div>
                      <div className="text-white/80 text-sm">{String(value)}</div>
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

