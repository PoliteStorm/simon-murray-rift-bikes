'use client';

import Link from 'next/link';
import Logo from '@/components/Logo';
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
              <div className="flex items-center space-x-6">
                <div className="relative w-20 h-20 md:w-24 md:h-24">
                  <svg 
                    viewBox="0 0 48 48" 
                    className="w-full h-full"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    {/* Main rift lines - sharp, angular */}
                    <path
                      d="M4 14 L44 14"
                      stroke="#fbbf24"
                      strokeWidth="2.5"
                      strokeLinecap="square"
                      strokeLinejoin="miter"
                    />
                    <path
                      d="M6 24 L42 24"
                      stroke="#fbbf24"
                      strokeWidth="2.5"
                      strokeLinecap="square"
                      strokeLinejoin="miter"
                    />
                    <path
                      d="M8 34 L40 34"
                      stroke="#fbbf24"
                      strokeWidth="2.5"
                      strokeLinecap="square"
                      strokeLinejoin="miter"
                    />
                    {/* Sharp volcanic cracks - angular, dynamic */}
                    <path
                      d="M12 8 L14 14 M36 8 L34 14"
                      stroke="#fbbf24"
                      strokeWidth="2"
                      strokeLinecap="square"
                    />
                    <path
                      d="M18 18 L20 24 M30 18 L28 24"
                      stroke="#fbbf24"
                      strokeWidth="2"
                      strokeLinecap="square"
                    />
                    <path
                      d="M24 28 L26 34 M24 28 L22 34"
                      stroke="#fbbf24"
                      strokeWidth="2"
                      strokeLinecap="square"
                    />
                    {/* Additional sharp detail lines */}
                    <path
                      d="M16 10 L18 14 M32 10 L30 14"
                      stroke="#fbbf24"
                      strokeWidth="1.5"
                      strokeLinecap="square"
                      opacity="0.7"
                    />
                  </svg>
                </div>
                <h1 className="text-6xl md:text-8xl font-black text-white uppercase"
                    style={{
                      letterSpacing: '0.25em',
                      textShadow: '0 0 20px rgba(251, 191, 36, 0.5), 0 4px 8px rgba(0, 0, 0, 0.7)',
                      fontWeight: 900,
                      lineHeight: '1.1',
                    }}>
                  RIFT
                </h1>
              </div>
            </div>
            <p className="text-xl md:text-2xl text-white mb-12 drop-shadow-lg">
              Premium Road Cycling. Custom Built.
            </p>
            <div className="flex justify-center space-x-4">
              <Link href="/bikes" className="rift-button shadow-2xl">
                Shop Bikes
              </Link>
              <Link href="/order" className="rift-button-secondary shadow-2xl">
                Custom Build
              </Link>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

