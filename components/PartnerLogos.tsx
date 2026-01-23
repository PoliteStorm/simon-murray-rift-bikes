'use client';

import React from 'react';

interface PartnerLogo {
  name: string;
  imagePath: string;
  category?: string;
  format?: 'svg' | 'png';
}

// Real branded components only - using newest, highest quality logo files
const partnerLogos: PartnerLogo[] = [
  {
    name: 'Shimano',
    category: 'Components',
    imagePath: '/logos/partners/shimano.png',
    format: 'png'
  },
  {
    name: 'SRAM',
    category: 'Components',
    imagePath: '/logos/partners/sram.png',
    format: 'png'
  },
  {
    name: 'Campagnolo',
    category: 'Components',
    imagePath: '/logos/partners/campagnolo.png',
    format: 'png'
  },
  {
    name: 'Maxxis',
    category: 'Tires',
    imagePath: '/logos/partners/maxxis.png',
    format: 'png'
  },
  {
    name: 'JAGWIRE',
    category: 'Cables',
    imagePath: '/logos/partners/jagwire.svg',
    format: 'svg'
  },
  {
    name: 'Bafang',
    category: 'Motor Systems',
    imagePath: '/logos/partners/bafang.png',
    format: 'png'
  },
  {
    name: 'Tektro',
    category: 'Brakes',
    imagePath: '/logos/partners/tektro.svg',
    format: 'svg'
  },
];

export default function PartnerLogos({ 
  variant = 'default',
  showCategories = false 
}: { 
  variant?: 'default' | 'compact' | 'grid';
  showCategories?: boolean;
}) {
  const groupedLogos = partnerLogos.reduce((acc, logo) => {
    const category = logo.category || 'Other';
    if (!acc[category]) {
      acc[category] = [];
    }
    acc[category].push(logo);
    return acc;
  }, {} as Record<string, PartnerLogo[]>);

  if (variant === 'grid') {
    return (
      <div className="bg-rift-card border border-rift-emerald rounded-lg p-8">
        <h3 className="text-2xl font-bold text-white mb-6 text-center">Premium Components & Features</h3>
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6">
          {partnerLogos.map((logo, index) => (
            <div 
              key={index}
              className="flex flex-col items-center justify-center p-4 bg-rift-dark/50 rounded-lg border border-rift-emerald/30 hover:border-rift-gold transition-all hover:bg-rift-dark/70"
            >
              <div className="w-full h-32 md:h-40 lg:h-48 flex items-center justify-center mb-2 relative bg-transparent partner-logo">
                <img 
                  src={logo.imagePath} 
                  alt={logo.name}
                  className="h-32 md:h-40 lg:h-48 w-auto object-contain partner-logo"
                  style={{ maxWidth: '600px', backgroundColor: 'transparent', imageRendering: 'auto' }}
                />
              </div>
              {showCategories && logo.category && (
                <span className="text-xs text-rift-gold/70 mt-1">{logo.category}</span>
              )}
            </div>
          ))}
        </div>
      </div>
    );
  }

  if (variant === 'compact') {
    return (
      <div className="flex flex-wrap items-center justify-center gap-6 md:gap-8 py-6">
        {partnerLogos.map((logo, index) => (
          <div 
            key={index}
            className="h-20 md:h-24 lg:h-28 opacity-80 hover:opacity-100 transition-opacity relative partner-logo flex items-center justify-center"
            style={{ width: 'auto', minWidth: '120px' }}
          >
            <img 
              src={logo.imagePath} 
              alt={logo.name}
              className="h-20 md:h-24 lg:h-28 w-auto object-contain partner-logo"
              style={{ maxWidth: '200px', backgroundColor: 'transparent', imageRendering: 'auto' }}
            />
          </div>
        ))}
      </div>
    );
  }

  // Default variant - grouped by category
  return (
    <div className="bg-rift-card border border-rift-emerald rounded-lg p-8">
      <h3 className="text-2xl font-bold text-white mb-8 text-center">
        Premium Components & Quality Assurance
      </h3>
      
      {Object.entries(groupedLogos).map(([category, logos]) => (
        <div key={category} className="mb-8 last:mb-0">
          {showCategories && (
            <h4 className="text-lg font-semibold text-rift-gold mb-4">{category}</h4>
          )}
          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4">
            {logos.map((logo, index) => (
              <div 
                key={index}
                className="flex flex-col items-center justify-center p-4 bg-rift-dark/50 rounded-lg border border-rift-emerald/30 hover:border-rift-gold transition-all hover:bg-rift-dark/70 group"
              >
                <div className="w-full h-32 md:h-40 lg:h-48 flex items-center justify-center mb-2 relative bg-transparent partner-logo">
                  <img 
                    src={logo.imagePath} 
                    alt={logo.name}
                    className="h-32 md:h-40 lg:h-48 w-auto object-contain partner-logo"
                    style={{ maxWidth: '600px', backgroundColor: 'transparent', imageRendering: 'auto' }}
                  />
                </div>
                <span className="text-xs text-white/60 group-hover:text-rift-gold transition-colors">
                  {logo.name}
                </span>
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}
