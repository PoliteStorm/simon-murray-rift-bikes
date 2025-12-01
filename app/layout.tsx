import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'
import Navbar from '@/components/Navbar'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'RIFT - Custom Bikes | Edge of Biking Technology',
  description: 'Handmade custom bikes with lifetime frame warranty',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en" className="h-full">
      <body className={`${inter.className} h-full flex flex-col`}>
        <Navbar />
        <main className="flex-1">
          {children}
        </main>
        <footer className="bg-rift-dark border-t border-rift-gold py-8 mt-auto">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <p className="text-white/60">
              © 2025 RIFT. Lifetime warranty on frame. 1 year warranty on all other components.
            </p>
          </div>
        </footer>
      </body>
    </html>
  )
}

