'use client';

import { useEffect, useState } from 'react';

interface FlashingLogoProps {
  position?: 'top-left' | 'top-right' | 'bottom-left' | 'bottom-right' | 'center';
  size?: 'small' | 'medium' | 'large';
}

export default function FlashingLogo({ position = 'top-right', size = 'medium' }: FlashingLogoProps) {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    // Flash the logo every 5 seconds for 2 seconds
    const interval = setInterval(() => {
      setIsVisible(true);
      setTimeout(() => {
        setIsVisible(false);
      }, 2000);
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  const positionClasses = {
    'top-left': 'top-4 left-4',
    'top-right': 'top-4 right-4',
    'bottom-left': 'bottom-4 left-4',
    'bottom-right': 'bottom-4 right-4',
    'center': 'top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2'
  };

  const sizeClasses = {
    'small': 'w-16 h-16',
    'medium': 'w-24 h-24',
    'large': 'w-32 h-32'
  };

  return (
    <div
      className={`fixed ${positionClasses[position]} ${sizeClasses[size]} pointer-events-none z-50 transition-all duration-500 ${
        isVisible ? 'opacity-100 scale-100' : 'opacity-0 scale-0'
      }`}
    >
      <div className="relative w-full h-full animate-pulse-glow">
        <img
          src="/red-logo.jpg"
          alt="RIFT Logo"
          className="w-full h-full object-contain drop-shadow-2xl"
          style={{
            filter: 'drop-shadow(0 0 20px rgba(239, 68, 68, 0.8)) drop-shadow(0 0 40px rgba(239, 68, 68, 0.6))'
          }}
        />
      </div>
    </div>
  );
}
