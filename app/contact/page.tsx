import PartnerLogos from '@/components/PartnerLogos';

export const metadata = {
  title: 'Contact RIFT | Get in Touch',
  description: 'Contact Simon Murray at RIFT — WhatsApp, email, phone and social media.',
};

export default function ContactPage() {
  return (
    <div className="flex-1 py-12 bg-rift-dark">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-4xl font-bold text-white mb-4">Contact Us</h1>
        <p className="text-white/80 text-lg mb-8">
          All viewings and test rides are always welcomed and encouraged. Get in touch with Simon and we&apos;ll
          help you build the perfect RIFT.
        </p>

        <div className="rift-card p-8 space-y-8">
          {/* Primary contact */}
          <div>
            <h2 className="text-2xl font-bold text-rift-gold mb-1">Simon Murray</h2>
            <p className="text-white/60 mb-6">RIFT Bikes</p>

            <div className="grid gap-4 sm:grid-cols-2">
              {/* WhatsApp */}
              <a
                href="https://wa.me/447817174391"
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center gap-3 bg-rift-royal/40 hover:bg-rift-royal/70 border border-rift-emerald rounded-xl p-4 transition-colors"
              >
                <svg className="w-7 h-7 text-rift-gold flex-shrink-0" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M.057 24l1.687-6.163a11.867 11.867 0 01-1.587-5.945C.16 5.335 5.495 0 12.05 0a11.82 11.82 0 018.413 3.488 11.82 11.82 0 013.48 8.414c-.003 6.557-5.338 11.892-11.893 11.892a11.9 11.9 0 01-5.688-1.448L.057 24zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884a9.86 9.86 0 001.519 5.26l-.999 3.648 3.97-1.207zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z" />
                </svg>
                <div>
                  <p className="text-white font-semibold">WhatsApp</p>
                  <p className="text-white/70 text-sm">07817 174391</p>
                </div>
              </a>

              {/* Phone */}
              <a
                href="tel:01985844563"
                className="flex items-center gap-3 bg-rift-royal/40 hover:bg-rift-royal/70 border border-rift-emerald rounded-xl p-4 transition-colors"
              >
                <svg className="w-7 h-7 text-rift-gold flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                </svg>
                <div>
                  <p className="text-white font-semibold">Phone</p>
                  <p className="text-white/70 text-sm">01985 844563</p>
                </div>
              </a>

              {/* Email */}
              <a
                href="mailto:riftbike@outlook.com"
                className="flex items-center gap-3 bg-rift-royal/40 hover:bg-rift-royal/70 border border-rift-emerald rounded-xl p-4 transition-colors sm:col-span-2"
              >
                <svg className="w-7 h-7 text-rift-gold flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
                <div>
                  <p className="text-white font-semibold">Email</p>
                  <p className="text-white/70 text-sm">riftbike@outlook.com</p>
                </div>
              </a>
            </div>
          </div>

          {/* Social media */}
          <div className="border-t border-rift-emerald pt-6">
            <h2 className="text-2xl font-bold text-rift-gold mb-4">Follow Us</h2>
            <div className="flex flex-wrap gap-4">
              <a
                href="https://www.facebook.com/riftbikesocial"
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center gap-3 bg-rift-royal/40 hover:bg-rift-royal/70 border border-rift-emerald rounded-xl px-5 py-4 transition-colors"
              >
                <svg className="w-7 h-7 text-rift-gold flex-shrink-0" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z" />
                </svg>
                <div>
                  <p className="text-white font-semibold">Facebook</p>
                  <p className="text-white/70 text-sm">@riftbikesocial</p>
                </div>
              </a>

              <a
                href="https://www.instagram.com/riftbikesocial"
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center gap-3 bg-rift-royal/40 hover:bg-rift-royal/70 border border-rift-emerald rounded-xl px-5 py-4 transition-colors"
              >
                <svg className="w-7 h-7 text-rift-gold flex-shrink-0" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z" />
                </svg>
                <div>
                  <p className="text-white font-semibold">Instagram</p>
                  <p className="text-white/70 text-sm">@riftbikesocial</p>
                </div>
              </a>
            </div>
          </div>

          {/* Location / delivery */}
          <div className="border-t border-rift-emerald pt-6">
            <h2 className="text-2xl font-bold text-rift-gold mb-4">Viewings &amp; Delivery</h2>
            <p className="text-white/80">
              Based at postcode <strong className="text-rift-gold">BA11 5ER</strong>. Free delivery within 50 miles —
              nationwide and worldwide delivery available at unbeatable prices. Get in touch to arrange a viewing or
              test ride.
            </p>
          </div>
        </div>

        {/* Partner Logos */}
        <div className="mt-12">
          <PartnerLogos variant="grid" showCategories={false} />
        </div>
      </div>
    </div>
  );
}
