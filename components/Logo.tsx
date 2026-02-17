import React from 'react';

interface LogoProps {
  size?: 'small' | 'large';
}

export default function Logo({ size = 'small' }: LogoProps) {
  const isLarge = size === 'large';
  
  return (
    <div className="flex items-center">
      <img
        src="/logo.jpg"
        alt="RIFT Logo"
        className={isLarge ? "h-20 w-auto object-contain" : "h-14 w-auto max-h-14 object-contain"}
        style={isLarge ? {
          maxHeight: '80px',
          height: 'auto',
          width: 'auto',
        } : {
          maxHeight: '56px',
          height: 'auto',
          width: 'auto',
        }}
      />
    </div>
  );
}
