'use client';

import { useEffect, useState, useRef } from 'react';
import Link from 'next/link';
import FlashingLogo from '@/components/FlashingLogo';

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

export default function BikesPage() {
  const [bikes, setBikes] = useState<Bike[]>([]);
  const [loading, setLoading] = useState(true);
  const [visibleVideo, setVisibleVideo] = useState<number | null>(null);
  const videoRefs = useRef<{ [key: number]: HTMLVideoElement | null }>({});

  useEffect(() => {
    fetchBikes();
  }, []);

  useEffect(() => {
    // Intersection Observer for YouTube-like autoplay
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          const videoId = parseInt(entry.target.getAttribute('data-video-id') || '0');
          const video = videoRefs.current[videoId];
          
          if (entry.isIntersecting && entry.intersectionRatio > 0.5) {
            // Video is in view - play it
            setVisibleVideo(videoId);
            if (video) {
              video.play().catch(() => {
                // Autoplay was prevented
              });
            }
          } else {
            // Video is out of view - pause it
            if (visibleVideo === videoId) {
              setVisibleVideo(null);
            }
            if (video) {
              video.pause();
            }
          }
        });
      },
      {
        threshold: [0, 0.5, 1],
        rootMargin: '0px',
      }
    );

    // Observe all video elements
    Object.keys(videoRefs.current).forEach((key) => {
      const video = videoRefs.current[parseInt(key)];
      if (video) {
        observer.observe(video);
      }
    });

    return () => {
      observer.disconnect();
    };
  }, [bikes, visibleVideo]);

  const fetchBikes = async () => {
    try {
      const response = await fetch('/api/bikes');
      const data = await response.json();
      // Ensure data is always an array
      if (Array.isArray(data)) {
        setBikes(data);
      } else {
        console.error('Invalid bikes data:', data);
        setBikes([]);
      }
    } catch (error) {
      console.error('Error fetching bikes:', error);
      setBikes([]);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="flex-1 flex items-center justify-center">
        <p className="text-rift-gold text-xl">Loading bikes...</p>
      </div>
    );
  }

  return (
    <div className="flex-1 py-12 bg-rift-dark relative">
      <FlashingLogo position="bottom-right" size="small" />
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-4xl font-bold text-white mb-4">Shop Bikes</h1>
        <p className="text-white/80 mb-12">Explore our collection of premium road bikes.</p>
        
        {bikes.length === 0 ? (
          <div className="text-center py-12">
            <p className="text-white/60 text-lg mb-4">No bikes available yet.</p>
            <p className="text-white/40">Videos and images will be added once bikes are built.</p>
          </div>
        ) : (
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {bikes.map((bike) => (
              <Link key={bike.id} href={`/bikes/${bike.id}`} className="rift-card overflow-hidden hover:border-rift-gold transition-all duration-300 transform hover:scale-[1.02] block group">
                <div className="aspect-video bg-gradient-to-br from-rift-royal to-emerald-950 flex items-center justify-center overflow-hidden">
                  {bike.videoUrl ? (
                    <video
                      ref={(el) => {
                        if (el) {
                          videoRefs.current[bike.id] = el;
                          // Try to autoplay when video is loaded
                          el.addEventListener('loadeddata', () => {
                            if (visibleVideo === bike.id) {
                              el.play().catch(() => {
                                // Autoplay prevented
                              });
                            }
                          });
                        }
                      }}
                      data-video-id={bike.id}
                      className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                      controls
                      loop
                      muted
                      playsInline
                      preload="auto"
                    >
                      <source src={bike.videoUrl} type="video/mp4" />
                    </video>
                  ) : bike.imageUrl ? (
                    <img src={bike.imageUrl} alt={bike.name} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300" />
                  ) : (
                    <div className="text-center p-8">
                      <div className="w-24 h-24 border-2 border-rift-gold/30 rounded-full mx-auto mb-4 flex items-center justify-center">
                        <svg className="w-12 h-12 text-rift-gold/50" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                        </svg>
                      </div>
                      <p className="text-rift-gold/70 text-sm">Image Coming Soon</p>
                    </div>
                  )}
                </div>
                <div className="p-6">
                  <div className="flex items-center justify-between mb-3">
                    <h2 className="text-xl font-bold text-white group-hover:text-rift-gold transition-colors">{bike.name}</h2>
                    {bike.category && (
                      <span className="text-xs bg-rift-gold/20 text-rift-gold px-3 py-1 rounded-full border border-rift-gold/30">
                        {bike.category}
                      </span>
                    )}
                  </div>
                  <p className="text-white/70 mb-4 text-sm leading-relaxed">{bike.description}</p>
                  <div className="flex justify-between items-center pt-4 border-t border-rift-emerald/30">
                    <span className="text-2xl font-bold text-rift-gold">
                      £{bike.basePrice ? bike.basePrice.toLocaleString() : 'N/A'}
                    </span>
                    <span className="text-sm text-white/60 flex items-center gap-1">
                      <svg className="w-4 h-4 text-rift-gold" fill="currentColor" viewBox="0 0 20 20">
                        <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                      </svg>
                      Available to Order
                    </span>
                  </div>
                </div>
              </Link>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

