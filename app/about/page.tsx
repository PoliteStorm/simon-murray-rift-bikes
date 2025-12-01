export default function AboutPage() {
  return (
    <div className="flex-1 py-12 bg-rift-dark">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-4xl font-bold text-white mb-8">About RIFT</h1>
        <div className="bg-rift-card border border-rift-emerald rounded-lg p-8 space-y-6">
          <p className="text-white/80 text-lg">
            RIFT represents the edge of biking technology, where premium craftsmanship meets cutting-edge design.
          </p>
          <p className="text-white/80">
            Every bike is handmade to your exact specifications, ensuring the perfect fit and performance for your riding style.
          </p>
            <div className="border-t border-rift-emerald pt-6">
            <h2 className="text-2xl font-bold text-rift-gold mb-4">Our Commitment</h2>
            <ul className="text-white/80 space-y-2">
              <li>✓ Lifetime warranty on frame</li>
              <li>✓ 1 year warranty on all other components</li>
              <li>✓ Top spec as standard - no compromises</li>
              <li>✓ Fully customizable to your requirements</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}

