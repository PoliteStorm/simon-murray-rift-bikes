export default function CartPage() {
  return (
    <div className="flex-1 py-12 bg-rift-dark">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-4xl font-bold text-white mb-8">Shopping Cart</h1>
        <div className="bg-rift-card border border-rift-emerald rounded-lg p-8 text-center">
          <p className="text-white/80 text-lg mb-4">Your cart is empty.</p>
          <a href="/bikes" className="rift-button inline-block">
            Shop Bikes
          </a>
        </div>
      </div>
    </div>
  );
}

