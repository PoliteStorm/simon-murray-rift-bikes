'use client';

import Link from 'next/link';

export default function InfoBanner() {
  return (
    <div className="bg-gradient-to-r from-rift-royal via-rift-card to-rift-royal border-b border-rift-gold/30">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2 flex flex-wrap items-center justify-center gap-x-6 gap-y-1 text-xs md:text-sm">
        <span className="font-serif italic text-rift-gold tracking-wide">Hand built just for you<span className="opacity-70">…</span></span>
        <span className="hidden md:inline-block w-px h-3 bg-rift-gold/40"></span>
        <span className="text-white/80">T1000 carbon · Shimano Ultegra Di2</span>
        <span className="hidden md:inline-block w-px h-3 bg-rift-gold/40"></span>
        <Link href="/contact" className="text-white/80 hover:text-rift-gold transition-colors">
          Contact Simon
        </Link>
      </div>
    </div>
  );
}
