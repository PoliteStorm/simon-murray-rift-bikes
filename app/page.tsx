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
            <div className="flex items-center justify-center mb-10">
              <span
                className="text-rift-gold font-extrabold uppercase leading-none select-none text-7xl md:text-9xl tracking-[0.28em]"
                style={{ textShadow: '0 0 24px rgba(251,191,36,0.35), 0 4px 12px rgba(0,0,0,0.6)' }}
                aria-label="RIFT"
              >
                RIFT
              </span>
            </div>

            {/* Signature tagline */}
            <p className="text-rift-gold text-xl md:text-3xl mb-4 tracking-[0.18em] uppercase font-medium drop-shadow-[0_2px_12px_rgba(251,191,36,0.35)]">
              Hand built just for you<span className="opacity-70">…</span>
            </p>
            <div className="mx-auto w-24 h-px bg-gradient-to-r from-transparent via-rift-gold to-transparent mb-8"></div>

            <p className="text-lg md:text-xl text-white/90 mb-10 drop-shadow-lg font-semibold max-w-3xl mx-auto">
              Losers look at winners — winners look at winning. Be a winner with RiftBike.
            </p>
            <div className="flex flex-wrap justify-center gap-4">
              <Link href="/bikes" className="rift-button shadow-2xl">
                Shop Bikes
              </Link>
              <Link href="/contact" className="rift-button-secondary shadow-2xl">
                Talk to Simon
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

