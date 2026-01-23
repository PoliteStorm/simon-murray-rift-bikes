import PartnerLogos from '@/components/PartnerLogos';

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
            <h2 className="text-2xl font-bold text-rift-gold mb-4">Warranty</h2>
            <div className="text-white/80 space-y-3">
              <p>
                We stand behind the quality of every RIFT bike with comprehensive warranty coverage:
              </p>
              <ul className="space-y-2 ml-4">
                <li>✓ <strong>Lifetime warranty on frame</strong> - Your RIFT frame is guaranteed for life against manufacturing defects</li>
                <li>✓ <strong>1 year warranty on all other components</strong> - All components are covered for one year from purchase date</li>
                <li>✓ <strong>Top spec as standard</strong> - No compromises, only premium components</li>
                <li>✓ <strong>Fully customizable</strong> - Every bike is built to your exact requirements</li>
              </ul>
              <p className="text-sm text-white/60 mt-4">
                Warranty covers manufacturing defects and material failures under normal use. Damage from accidents, misuse, or modifications may void warranty coverage.
              </p>
            </div>
          </div>

          <div className="border-t border-rift-emerald pt-6">
            <h2 className="text-2xl font-bold text-rift-gold mb-4">Payment & Ordering</h2>
            <div className="text-white/80 space-y-3">
              <p>
                We operate on a deposit system to secure your custom build:
              </p>
              <ul className="space-y-2 ml-4">
                <li>✓ <strong>Deposit required</strong> - A deposit is required to confirm your order and begin the build process</li>
                <li>✓ <strong>Bank transfer payment</strong> - We accept payments via bank transfer</li>
                <li>✓ <strong>Order confirmation</strong> - Once your order is confirmed, you will be contacted directly at <strong>si@riftbike.com</strong> or <strong>07817174391</strong> to arrange payment details and discuss your custom specifications</li>
                <li>✓ <strong>Balance payment</strong> - Remaining balance is due upon completion, before delivery</li>
              </ul>
              <p className="text-sm text-white/60 mt-4">
                After placing your order, you will receive confirmation and payment instructions. You will be contacted at <strong>si@riftbike.com</strong> or <strong>07817174391</strong> to finalize your bike specifications and delivery timeline.
              </p>
            </div>
          </div>

          <div className="border-t border-rift-emerald pt-6">
            <h2 className="text-2xl font-bold text-rift-gold mb-4">Giving Back</h2>
            <div className="text-white/80 space-y-3">
              <p>
                At RIFT, we believe in supporting our local community. A percentage of our profits is donated to local charities, helping to make a positive impact in the areas where we operate.
              </p>
              <p className="text-sm text-white/60">
                By choosing RIFT, you're not just investing in a premium bike - you're also contributing to charitable causes that support our local community.
              </p>
            </div>
          </div>
        </div>

        {/* Partner Logos */}
        <div className="mt-12">
          <PartnerLogos variant="grid" showCategories={true} />
        </div>
      </div>
    </div>
  );
}

