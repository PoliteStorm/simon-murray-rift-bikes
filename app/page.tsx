'use client';

import Link from 'next/link';
import PartnerLogos from '@/components/PartnerLogos';
import { useEffect, useRef } from 'react';

export default function Home() {
  const videoRef = useRef<HTMLVideoElement>(null);

  useEffect(() => {
    if (videoRef.current) {
      videoRef.current.play().catch(() => {
        // Autoplay was prevented, user interaction required
      });
    }
  }, []);

  return (
    <div className="flex-1 bg-rift-dark relative overflow-hidden">
      {/* Background Video */}
      <div className="absolute inset-0 z-0">
        <video
          ref={videoRef}
          autoPlay
          loop
          muted
          playsInline
          className="w-full h-full object-cover opacity-30"
        >
          <source src="/videos/homepage-video.mov" type="video/quicktime" />
          <source src="/videos/homepage-video.mov" type="video/mp4" />
        </video>
        <div className="absolute inset-0 bg-gradient-to-b from-rift-dark/80 via-rift-dark/60 to-rift-dark/80"></div>
      </div>

      {/* Hero Section */}
      <section className="relative z-10 bg-gradient-to-b from-rift-dark/40 via-transparent to-rift-dark/40 py-32 flex-1 flex items-center min-h-full">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
          <div className="text-center">
            <div className="flex items-center justify-center mb-12">
              <img
                src="/logo.jpg"
                alt="RIFT Logo"
                className="max-w-md w-full h-auto object-contain"
                style={{
                  maxWidth: '500px',
                  width: '100%',
                  height: 'auto',
                }}
              />
            </div>
            <p className="text-xl md:text-2xl text-white mb-12 drop-shadow-lg">
              Premium Road Cycling. Custom Built.
            </p>
            <div className="flex justify-center space-x-4">
              <Link href="/bikes" className="rift-button shadow-2xl">
                Shop Bikes
              </Link>
            </div>
          </div>
        </div>
      </section>

      {/* Partner Logos Section */}
      <section className="relative z-10 py-16 bg-rift-dark/80">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <PartnerLogos variant="compact" />
        </div>
      </section>
    </div>
  );
}

