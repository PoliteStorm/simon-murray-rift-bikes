'use client';

import { useState } from 'react';

const logos = [
  // Original logos
  { name: 'Horizontal', file: 'rift-logo-horizontal.svg', description: 'Best for: Website headers, email signatures', category: 'original' },
  { name: 'Vertical', file: 'rift-logo-vertical.svg', description: 'Best for: Mobile apps, social media profiles', category: 'original' },
  { name: 'Icon Only', file: 'rift-logo-icon-only.svg', description: 'Best for: Favicons, app icons, small placements', category: 'original' },
  { name: 'Minimal', file: 'rift-logo-minimal.svg', description: 'Best for: Subtle branding, watermarks', category: 'original' },
  { name: 'Badge', file: 'rift-logo-badge.svg', description: 'Best for: Certificates, achievements, premium branding', category: 'original' },
  { name: 'Stacked', file: 'rift-logo-stacked.svg', description: 'Best for: Business cards, marketing materials', category: 'original' },
  { name: 'Wide Banner', file: 'rift-logo-wide-banner.svg', description: 'Best for: Website headers, banners, wide posters', category: 'original' },
  { name: 'Circle Badge', file: 'rift-logo-circle-badge.svg', description: 'Best for: Profile pictures, round formats', category: 'original' },
  { name: 'Text Only', file: 'rift-logo-text-only.svg', description: 'Best for: Text-based branding', category: 'original' },
  { name: 'Compact', file: 'rift-logo-compact.svg', description: 'Best for: Mobile headers, compact spaces', category: 'original' },
  { name: 'Watermark', file: 'rift-logo-watermark.svg', description: 'Best for: Video overlays, image watermarks', category: 'original' },
  // Generated logos
  { name: 'Horizontal Primary', file: 'rift-logo-01-horizontal-primary.svg', description: 'Icon left, text right - Main logo', category: 'generated' },
  { name: 'Vertical Stacked', file: 'rift-logo-02-vertical-stacked.svg', description: 'Icon above text', category: 'generated' },
  { name: 'Horizontal Tagline', file: 'rift-logo-03-horizontal-tagline.svg', description: 'Includes custom bike shop tagline', category: 'generated' },
  { name: 'Icon Only Square', file: 'rift-logo-04-icon-only-square.svg', description: 'Perfect for social media avatars', category: 'generated' },
  { name: 'Text Only', file: 'rift-logo-05-text-only.svg', description: 'No icon, typography focus', category: 'generated' },
  { name: 'Circle Badge', file: 'rift-logo-06-circle-badge.svg', description: 'Circular design with border', category: 'generated' },
  { name: 'Compact Square', file: 'rift-logo-07-compact-square.svg', description: 'Small space optimized', category: 'generated' },
  { name: 'Wide Banner', file: 'rift-logo-08-wide-banner.svg', description: 'Website header format', category: 'generated' },
  { name: 'Minimal Transparent', file: 'rift-logo-09-minimal-transparent.svg', description: 'Clean background', category: 'generated' },
  { name: 'Watermark', file: 'rift-logo-10-watermark.svg', description: 'Semi-transparent for overlays', category: 'generated' },
  { name: 'Inverted Colors', file: 'rift-logo-11-inverted-colors.svg', description: 'Gold background variation', category: 'generated' },
  { name: 'Vertical Tagline', file: 'rift-logo-12-vertical-tagline.svg', description: 'Tall format with subtitle', category: 'generated' },
  { name: 'Square Badge', file: 'rift-logo-13-square-badge.svg', description: 'Bordered with EST. date', category: 'generated' },
  { name: 'Horizontal Reversed', file: 'rift-logo-14-horizontal-reversed.svg', description: 'Text left, icon right', category: 'generated' },
  { name: 'Icon Bordered', file: 'rift-logo-15-icon-bordered.svg', description: 'Decorative frame', category: 'generated' },
  { name: 'Text Outlined', file: 'rift-logo-16-text-outlined.svg', description: 'Outline effect typography', category: 'generated' },
  { name: 'Angled Dynamic', file: 'rift-logo-17-angled-dynamic.svg', description: 'Energetic slanted design', category: 'generated' },
  { name: 'Monochrome Gold', file: 'rift-logo-18-monochrome-gold.svg', description: 'Single color version', category: 'generated' },
  { name: 'Stacked Centered', file: 'rift-logo-19-stacked-centered.svg', description: 'Accent lines top/bottom', category: 'generated' },
  { name: 'Minimal Icon + Text', file: 'rift-logo-20-minimal-icon-text.svg', description: 'Ultra compact version', category: 'generated' },
];

export default function LogosPage() {
  const [selectedLogo, setSelectedLogo] = useState<string | null>(null);
  const [backgroundType, setBackgroundType] = useState<'transparent' | 'dark' | 'light' | 'image'>('transparent');
  const [filterCategory, setFilterCategory] = useState<'all' | 'original' | 'generated'>('all');
  
  const filteredLogos = filterCategory === 'all' 
    ? logos 
    : logos.filter(logo => logo.category === filterCategory);

  return (
    <div className="flex-1 bg-rift-dark py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-4xl font-bold text-white mb-4">RIFT Marketing Logos</h1>
        <p className="text-white/70 mb-8">
          Collection of logo variations for marketing materials, posters, and video overlays.
        </p>

        {/* Category Filter */}
        <div className="mb-8 flex gap-4 flex-wrap">
          <button
            onClick={() => setFilterCategory('all')}
            className={`px-4 py-2 rounded-lg border transition-all ${
              filterCategory === 'all'
                ? 'bg-rift-gold text-rift-dark border-rift-gold'
                : 'bg-rift-card text-white border-rift-emerald'
            }`}
          >
            All Logos ({logos.length})
          </button>
          <button
            onClick={() => setFilterCategory('original')}
            className={`px-4 py-2 rounded-lg border transition-all ${
              filterCategory === 'original'
                ? 'bg-rift-gold text-rift-dark border-rift-gold'
                : 'bg-rift-card text-white border-rift-emerald'
            }`}
          >
            Original ({logos.filter(l => l.category === 'original').length})
          </button>
          <button
            onClick={() => setFilterCategory('generated')}
            className={`px-4 py-2 rounded-lg border transition-all ${
              filterCategory === 'generated'
                ? 'bg-rift-gold text-rift-dark border-rift-gold'
                : 'bg-rift-card text-white border-rift-emerald'
            }`}
          >
            Generated ({logos.filter(l => l.category === 'generated').length})
          </button>
        </div>

        {/* Background Preview Options */}
        <div className="mb-8 flex gap-4 flex-wrap">
          <button
            onClick={() => setBackgroundType('transparent')}
            className={`px-4 py-2 rounded-lg border transition-all ${
              backgroundType === 'transparent'
                ? 'bg-rift-gold text-rift-dark border-rift-gold'
                : 'bg-rift-card text-white border-rift-emerald'
            }`}
          >
            Transparent
          </button>
          <button
            onClick={() => setBackgroundType('dark')}
            className={`px-4 py-2 rounded-lg border transition-all ${
              backgroundType === 'dark'
                ? 'bg-rift-gold text-rift-dark border-rift-gold'
                : 'bg-rift-card text-white border-rift-emerald'
            }`}
          >
            Dark Background
          </button>
          <button
            onClick={() => setBackgroundType('light')}
            className={`px-4 py-2 rounded-lg border transition-all ${
              backgroundType === 'light'
                ? 'bg-rift-gold text-rift-dark border-rift-gold'
                : 'bg-rift-card text-white border-rift-emerald'
            }`}
          >
            Light Background
          </button>
          <button
            onClick={() => setBackgroundType('image')}
            className={`px-4 py-2 rounded-lg border transition-all ${
              backgroundType === 'image'
                ? 'bg-rift-gold text-rift-dark border-rift-gold'
                : 'bg-rift-card text-white border-rift-emerald'
            }`}
          >
            Image Overlay
          </button>
        </div>

        {/* Logo Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8 mb-12">
          {filteredLogos.map((logo) => (
            <div
              key={logo.file}
              className="rift-card p-6 cursor-pointer hover:border-rift-gold transition-all"
              onClick={() => setSelectedLogo(logo.file)}
            >
              <div
                className={`mb-4 flex items-center justify-center rounded-lg p-6 transition-all ${
                  backgroundType === 'dark'
                    ? 'bg-rift-dark'
                    : backgroundType === 'light'
                    ? 'bg-white'
                    : backgroundType === 'image'
                    ? 'bg-gradient-to-br from-rift-royal to-emerald-950'
                    : 'bg-transparent'
                }`}
              >
                <img
                  src={`/logos/marketing/${logo.file}`}
                  alt={logo.name}
                  className="max-w-full h-auto"
                />
              </div>
              <div className="flex items-center justify-between mb-2">
                <h3 className="text-xl font-bold text-white">{logo.name}</h3>
                {logo.category === 'generated' && (
                  <span className="text-xs bg-rift-gold/20 text-rift-gold px-2 py-1 rounded-full border border-rift-gold/30">
                    NEW
                  </span>
                )}
              </div>
              <p className="text-white/60 text-sm">{logo.description}</p>
              <a
                href={`/logos/marketing/${logo.file}`}
                download
                className="text-rift-gold hover:text-yellow-400 text-sm mt-2 inline-block"
                onClick={(e) => e.stopPropagation()}
              >
                Download SVG →
              </a>
            </div>
          ))}
        </div>

        {/* Selected Logo Preview */}
        {selectedLogo && (
          <div className="fixed inset-0 bg-black/80 z-50 flex items-center justify-center p-8" onClick={() => setSelectedLogo(null)}>
            <div className="rift-card p-8 max-w-4xl w-full" onClick={(e) => e.stopPropagation()}>
              <div className="flex justify-between items-center mb-6">
                <h2 className="text-2xl font-bold text-white">
                  {logos.find((l) => l.file === selectedLogo)?.name}
                </h2>
                <button
                  onClick={() => setSelectedLogo(null)}
                  className="text-white/60 hover:text-white text-2xl"
                >
                  ×
                </button>
              </div>
              <div
                className={`mb-6 flex items-center justify-center rounded-lg p-12 transition-all ${
                  backgroundType === 'dark'
                    ? 'bg-rift-dark'
                    : backgroundType === 'light'
                    ? 'bg-white'
                    : backgroundType === 'image'
                    ? 'bg-gradient-to-br from-rift-royal to-emerald-950'
                    : 'bg-transparent'
                }`}
              >
                <img
                  src={`/logos/marketing/${selectedLogo}`}
                  alt="Logo preview"
                  className="max-w-full h-auto"
                />
              </div>
              <div className="flex gap-4">
                <a
                  href={`/logos/marketing/${selectedLogo}`}
                  download
                  className="rift-button"
                >
                  Download SVG
                </a>
                <button
                  onClick={() => {
                    navigator.clipboard.writeText(`${window.location.origin}/logos/marketing/${selectedLogo}`);
                    alert('Logo URL copied to clipboard!');
                  }}
                  className="rift-button-secondary"
                >
                  Copy URL
                </button>
              </div>
            </div>
          </div>
        )}

        {/* Usage Instructions */}
        <div className="rift-card p-8 mt-12">
          <h2 className="text-2xl font-bold text-white mb-4">Usage Tips</h2>
          <ul className="space-y-2 text-white/70">
            <li>• All logos have transparent backgrounds - perfect for overlaying</li>
            <li>• SVG format scales perfectly to any size without quality loss</li>
            <li>• Use the watermark version for subtle video/image branding</li>
            <li>• Icon-only and compact versions work great for corner placements</li>
            <li>• Convert to PNG/JPG if needed for specific applications</li>
            <li>• All logos are located in: <code className="text-rift-gold">/public/logos/marketing/</code></li>
          </ul>
        </div>
      </div>
    </div>
  );
}
