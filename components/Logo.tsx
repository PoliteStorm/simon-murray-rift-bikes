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
        className={isLarge ? "h-16 w-auto object-contain" : "h-10 w-auto max-h-10 object-contain"}
        style={isLarge ? {
          maxHeight: '64px',
          height: 'auto',
          width: 'auto',
        } : {
          maxHeight: '40px',
          height: 'auto',
          width: 'auto',
        }}
      />
    </div>
  );
}
