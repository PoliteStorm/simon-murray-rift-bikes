'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useState } from 'react';

const navLinks = [
  { href: '/bikes', label: 'Bikes' },
  { href: '/about', label: 'About' },
  { href: '/contact', label: 'Contact' },
];

export default function Navbar() {
  const pathname = usePathname();
  const [mobileOpen, setMobileOpen] = useState(false);

  return (
    <>
      <nav className="bg-rift-dark border-b border-rift-gold">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-20">
            <div className="flex items-center">
              <Link
                href="/"
                className="text-rift-gold/90 hover:text-rift-gold text-xs sm:text-sm tracking-[0.18em] uppercase font-medium transition-colors"
              >
                Hand built just for you<span className="opacity-70">…</span>
              </Link>
            </div>

            {/* Desktop nav */}
            <div className="hidden md:flex items-center space-x-8">
              {navLinks.map((link) => {
                const active = pathname === link.href || (link.href !== '/' && pathname.startsWith(link.href));
                return (
                  <Link
                    key={link.href}
                    href={link.href}
                    className={`relative text-sm uppercase tracking-[0.18em] font-semibold transition-colors ${
                      active ? 'text-rift-gold' : 'text-white hover:text-rift-gold'
                    }`}
                  >
                    {link.label}
                    {active && (
                      <span className="absolute -bottom-2 left-0 right-0 h-px bg-rift-gold"></span>
                    )}
                  </Link>
                );
              })}
              <Link
                href="/cart"
                aria-label="Cart"
                className="text-white hover:text-rift-gold transition-colors"
              >
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                </svg>
              </Link>
            </div>

            {/* Mobile toggle */}
            <button
              onClick={() => setMobileOpen((v) => !v)}
              aria-label="Toggle menu"
              className="md:hidden text-white hover:text-rift-gold transition-colors p-2"
            >
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                {mobileOpen ? (
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                ) : (
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 7h16M4 12h16M4 17h16" />
                )}
              </svg>
            </button>
          </div>

          {/* Mobile menu */}
          {mobileOpen && (
            <div className="md:hidden border-t border-rift-gold/20 py-3 animate-fadeIn">
              <div className="flex flex-col space-y-1">
                {navLinks.map((link) => (
                  <Link
                    key={link.href}
                    href={link.href}
                    onClick={() => setMobileOpen(false)}
                    className="px-3 py-2 rounded-md text-white hover:text-rift-gold hover:bg-rift-card/40 uppercase tracking-[0.18em] text-sm font-semibold"
                  >
                    {link.label}
                  </Link>
                ))}
                <Link
                  href="/cart"
                  onClick={() => setMobileOpen(false)}
                  className="px-3 py-2 rounded-md text-white hover:text-rift-gold hover:bg-rift-card/40 uppercase tracking-[0.18em] text-sm font-semibold flex items-center gap-2"
                >
                  <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
                  </svg>
                  Cart
                </Link>
              </div>
            </div>
          )}
        </div>
      </nav>
      <div className="bg-rift-gold text-rift-dark py-2 text-center font-semibold text-sm">
        🚚 Free delivery within 50 miles of BA11
      </div>
    </>
  );
}
