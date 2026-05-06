import Link from 'next/link';

const PHONE = '01985-844563';
const WHATSAPP_DISPLAY = '07817 174 391';
const WHATSAPP_INTL = '447817174391';
const EMAIL = 'riftbike@outlook.com';

export const metadata = {
  title: 'Contact RIFT — Talk to Simon',
  description:
    'Get in touch with Simon at RIFT — WhatsApp, phone or email. Hand built bikes, hand answered enquiries.',
};

export default function ContactPage() {
  return (
    <div className="flex-1 py-16 bg-rift-dark relative overflow-hidden">
      {/* Subtle accent glow */}
      <div className="pointer-events-none absolute inset-0 bg-[radial-gradient(circle_at_top,rgba(251,191,36,0.08),transparent_60%)]"></div>

      <div className="relative max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Header */}
        <div className="text-center mb-12">
          <p className="font-serif italic text-rift-gold text-lg md:text-xl tracking-wide mb-3">
            Hand built just for you<span className="opacity-70">…</span>
          </p>
          <h1 className="text-4xl md:text-5xl font-bold text-white tracking-tight">All Contact Info</h1>
          <div className="mx-auto w-24 h-px bg-gradient-to-r from-transparent via-rift-gold to-transparent mt-5"></div>
          <p className="text-white/70 mt-5 max-w-2xl mx-auto">
            Every bike is custom built — questions are part of the process. The fastest reply is on WhatsApp.
          </p>
        </div>

        {/* Primary contact cards */}
        <div className="grid md:grid-cols-3 gap-5">
          {/* WhatsApp */}
          <a
            href={`https://wa.me/${WHATSAPP_INTL}?text=${encodeURIComponent(
              "Hi Simon, I'd like to ask about a RIFT bike."
            )}`}
            target="_blank"
            rel="noopener noreferrer"
            className="group rift-card p-6 hover:border-rift-gold transition-all duration-300 transform hover:-translate-y-1 hover:shadow-2xl"
          >
            <div className="flex items-center gap-3 mb-4">
              <div className="w-11 h-11 rounded-full bg-[#25D366]/15 border border-[#25D366]/40 flex items-center justify-center">
                {/* WhatsApp glyph */}
                <svg viewBox="0 0 32 32" className="w-6 h-6 text-[#25D366]" fill="currentColor" aria-hidden="true">
                  <path d="M19.11 17.21c-.27-.14-1.62-.8-1.87-.89-.25-.09-.43-.14-.61.14-.18.27-.7.89-.86 1.07-.16.18-.32.2-.59.07-.27-.14-1.15-.42-2.19-1.35-.81-.72-1.36-1.61-1.52-1.88-.16-.27-.02-.42.12-.55.12-.12.27-.32.41-.48.14-.16.18-.27.27-.45.09-.18.05-.34-.02-.48-.07-.14-.61-1.47-.83-2.01-.22-.53-.45-.46-.61-.47l-.52-.01c-.18 0-.48.07-.73.34s-.96.94-.96 2.29.99 2.66 1.13 2.84c.14.18 1.95 2.98 4.73 4.18.66.28 1.18.45 1.58.58.66.21 1.27.18 1.74.11.53-.08 1.62-.66 1.85-1.3.23-.64.23-1.18.16-1.3-.07-.13-.25-.2-.52-.34zM16.02 5.33C10.16 5.33 5.4 10.09 5.4 15.95c0 2.06.6 3.97 1.62 5.59L5.33 26.67l5.27-1.66a10.59 10.59 0 0 0 5.41 1.49h.01c5.86 0 10.62-4.76 10.62-10.62 0-2.84-1.1-5.51-3.11-7.51a10.55 10.55 0 0 0-7.51-3.04zm0 19.4h-.01a8.79 8.79 0 0 1-4.49-1.23l-.32-.19-3.13.99 1-3.05-.21-.32a8.78 8.78 0 0 1-1.34-4.65c0-4.86 3.96-8.81 8.82-8.81 2.36 0 4.57.92 6.24 2.59a8.74 8.74 0 0 1 2.58 6.24c0 4.86-3.96 8.83-8.83 8.83z" />
                </svg>
              </div>
              <div>
                <div className="text-xs uppercase tracking-[0.18em] text-rift-gold/80">Fastest</div>
                <div className="text-white font-bold">WhatsApp</div>
              </div>
            </div>
            <div className="text-white/80 text-sm mb-4">
              Open a chat with Simon directly — usually replied within the hour.
            </div>
            <div className="flex items-center justify-between">
              <span className="text-white/90 font-mono text-sm">{WHATSAPP_DISPLAY}</span>
              <span className="text-rift-gold text-sm font-semibold group-hover:translate-x-0.5 transition-transform">
                Chat now →
              </span>
            </div>
          </a>

          {/* Phone */}
          <a
            href={`tel:${PHONE.replace(/[^+\d]/g, '')}`}
            className="group rift-card p-6 hover:border-rift-gold transition-all duration-300 transform hover:-translate-y-1 hover:shadow-2xl"
          >
            <div className="flex items-center gap-3 mb-4">
              <div className="w-11 h-11 rounded-full bg-rift-gold/15 border border-rift-gold/40 flex items-center justify-center">
                <svg className="w-6 h-6 text-rift-gold" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.6}
                    d="M3 5.5C3 4.12 4.12 3 5.5 3h1.7c.6 0 1.13.4 1.31.97l1 3.1a1.4 1.4 0 0 1-.4 1.46L7.7 9.95a13 13 0 0 0 6.35 6.35l1.42-1.42a1.4 1.4 0 0 1 1.46-.4l3.1 1c.57.18.97.71.97 1.31v1.7c0 1.38-1.12 2.5-2.5 2.5C10.94 21 3 13.06 3 5.5z" />
                </svg>
              </div>
              <div>
                <div className="text-xs uppercase tracking-[0.18em] text-rift-gold/80">Call</div>
                <div className="text-white font-bold">Phone</div>
              </div>
            </div>
            <div className="text-white/80 text-sm mb-4">
              Prefer a chat? Ring the workshop and Simon will pick up if he's not under a frame.
            </div>
            <div className="flex items-center justify-between">
              <span className="text-white/90 font-mono text-sm">{PHONE}</span>
              <span className="text-rift-gold text-sm font-semibold group-hover:translate-x-0.5 transition-transform">
                Call →
              </span>
            </div>
          </a>

          {/* Email */}
          <a
            href={`mailto:${EMAIL}`}
            className="group rift-card p-6 hover:border-rift-gold transition-all duration-300 transform hover:-translate-y-1 hover:shadow-2xl"
          >
            <div className="flex items-center gap-3 mb-4">
              <div className="w-11 h-11 rounded-full bg-rift-emerald/30 border border-rift-emerald/60 flex items-center justify-center">
                <svg className="w-6 h-6 text-emerald-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.6}
                    d="M3 7.5A2.5 2.5 0 0 1 5.5 5h13A2.5 2.5 0 0 1 21 7.5v9A2.5 2.5 0 0 1 18.5 19h-13A2.5 2.5 0 0 1 3 16.5v-9z" />
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.6} d="M3.5 7.5l8.5 6 8.5-6" />
                </svg>
              </div>
              <div>
                <div className="text-xs uppercase tracking-[0.18em] text-rift-gold/80">Write</div>
                <div className="text-white font-bold">Email</div>
              </div>
            </div>
            <div className="text-white/80 text-sm mb-4">
              For longer enquiries, spec discussions, or a paper trail of your build.
            </div>
            <div className="flex items-center justify-between">
              <span className="text-white/90 font-mono text-sm break-all">{EMAIL}</span>
              <span className="text-rift-gold text-sm font-semibold group-hover:translate-x-0.5 transition-transform whitespace-nowrap">
                Email →
              </span>
            </div>
          </a>
        </div>

        {/* Workshop / Viewings */}
        <div className="mt-10 grid md:grid-cols-2 gap-5">
          <div className="rift-card p-6">
            <h2 className="text-rift-gold uppercase tracking-[0.18em] text-xs font-semibold mb-2">Viewings & Test Rides</h2>
            <p className="text-white/85">
              Always welcomed and encouraged — drop a line on WhatsApp and Simon will sort a time.
            </p>
          </div>
          <div className="rift-card p-6">
            <h2 className="text-rift-gold uppercase tracking-[0.18em] text-xs font-semibold mb-2">Delivery</h2>
            <p className="text-white/85">
              Free within 50 miles of BA11&nbsp;5ER. Nationwide and worldwide delivery available at unbeatable prices.
            </p>
          </div>
        </div>

        <div className="mt-10 text-center">
          <Link href="/bikes" className="rift-button">View the Range</Link>
        </div>
      </div>
    </div>
  );
}
