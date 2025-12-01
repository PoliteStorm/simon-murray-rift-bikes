import React from 'react';

export default function Logo() {
  return (
    <div className="flex items-center space-x-3">
      {/* Volcanic rift - sharp, angular, dynamic */}
      <div className="relative w-12 h-12">
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
      {/* Sharp, dynamic racing-style text */}
      <span 
        className="text-2xl font-black text-white uppercase" 
        style={{
          fontFamily: 'system-ui, -apple-system, "Segoe UI", sans-serif',
          letterSpacing: '0.2em',
          fontWeight: 900,
          textShadow: '0 0 12px rgba(251, 191, 36, 0.4), 0 2px 4px rgba(0, 0, 0, 0.6)',
          lineHeight: '1.1',
        }}
      >
        RIFT
      </span>
    </div>
  );
}
