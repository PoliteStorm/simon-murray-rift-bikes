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
      <div className="w-full">
        <div className="grid grid-cols-3 md:grid-cols-4 lg:grid-cols-7 gap-4 md:gap-6 items-center justify-items-center">
          {partnerLogos.map((logo, index) => (
            <div 
              key={index}
              className="w-full flex items-center justify-center h-16 md:h-20 lg:h-24"
            >
              <img 
                src={logo.imagePath} 
                alt={logo.name}
                className="max-h-full max-w-full w-auto h-auto object-contain"
                style={{ backgroundColor: 'transparent' }}
              />
            </div>
          ))}
        </div>
      </div>
    );
  }

  if (variant === 'compact') {
    return (
      <div className="flex flex-wrap items-center justify-center gap-4 md:gap-6 lg:gap-8 py-4">
        {partnerLogos.map((logo, index) => (
          <div 
            key={index}
            className="h-12 md:h-16 lg:h-20 flex items-center justify-center"
            style={{ width: 'auto' }}
          >
            <img 
              src={logo.imagePath} 
              alt={logo.name}
              className="max-h-full max-w-full w-auto h-auto object-contain"
              style={{ backgroundColor: 'transparent' }}
            />
          </div>
        ))}
      </div>
    );
  }

  // Default variant - grouped by category
  return (
    <div className="w-full">
      <div className="grid grid-cols-3 md:grid-cols-4 lg:grid-cols-7 gap-4 md:gap-6 items-center justify-items-center">
        {partnerLogos.map((logo, index) => (
          <div 
            key={index}
            className="w-full flex items-center justify-center h-16 md:h-20 lg:h-24"
          >
            <img 
              src={logo.imagePath} 
              alt={logo.name}
              className="max-h-full max-w-full w-auto h-auto object-contain"
              style={{ backgroundColor: 'transparent' }}
            />
          </div>
        ))}
      </div>
    </div>
  );
}
