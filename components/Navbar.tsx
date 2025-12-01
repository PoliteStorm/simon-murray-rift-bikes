import Link from 'next/link';
import Logo from './Logo';

export default function Navbar() {
  return (
    <nav className="bg-rift-dark border-b border-rift-gold">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <Link href="/" className="flex items-center">
            <Logo />
          </Link>
          <div className="flex items-center space-x-6">
            <Link href="/bikes" className="text-white hover:text-rift-gold transition-colors">
              Shop
            </Link>
            <Link href="/order" className="text-white hover:text-rift-gold transition-colors">
              Custom Build
            </Link>
            <Link href="/about" className="text-white hover:text-rift-gold transition-colors">
              About
            </Link>
            <Link href="/cart" className="text-white hover:text-rift-gold transition-colors">
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
              </svg>
            </Link>
            <Link href="/admin" className="text-white hover:text-rift-gold transition-colors">
              Admin
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
}

