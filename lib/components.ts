// Component database with prices (UK market, approximate as of 2024)
export interface Component {
  id: string;
  name: string;
  brand: string;
  category: 'groupset' | 'brakes' | 'wheels' | 'frame' | 'other';
  price: number;
  logoPath: string;
  description?: string;
}

export const components: Component[] = [
  // Shimano Groupsets
  {
    id: 'dura-ace-r9200',
    name: 'Dura Ace R9200',
    brand: 'Shimano',
    category: 'groupset',
    price: 2800, // Approximate UK price
    logoPath: '/logos/partners/shimano.svg',
    description: 'Top-tier professional groupset with Di2 electronic shifting'
  },
  {
    id: 'ultegra-r8100',
    name: 'Ultegra R8100',
    brand: 'Shimano',
    category: 'groupset',
    price: 2200,
    logoPath: '/logos/partners/shimano.svg',
    description: 'Professional groupset with Di2 electronic shifting'
  },
  {
    id: '105-r7100',
    name: '105 R7100',
    brand: 'Shimano',
    category: 'groupset',
    price: 1200,
    logoPath: '/logos/partners/shimano.svg',
    description: 'Performance groupset with Di2 electronic shifting'
  },
  {
    id: 'dura-ace-mechanical',
    name: 'Dura Ace Mechanical',
    brand: 'Shimano',
    category: 'groupset',
    price: 2000,
    logoPath: '/logos/partners/shimano.svg',
    description: 'Top-tier mechanical groupset'
  },
  {
    id: 'ultegra-mechanical',
    name: 'Ultegra Mechanical',
    brand: 'Shimano',
    category: 'groupset',
    price: 1500,
    logoPath: '/logos/partners/shimano.svg',
    description: 'Professional mechanical groupset'
  },
  {
    id: '105-mechanical',
    name: '105 Mechanical',
    brand: 'Shimano',
    category: 'groupset',
    price: 800,
    logoPath: '/logos/partners/shimano.svg',
    description: 'Performance mechanical groupset'
  },
  {
    id: 'deore-m6100',
    name: 'Deore M6100',
    brand: 'Shimano',
    category: 'groupset',
    price: 600,
    logoPath: '/logos/partners/shimano.svg',
    description: 'Mountain bike groupset 12-speed'
  },
  // Other Components
  {
    id: 'maxxis-pursuer',
    name: 'Maxxis Pursuer',
    brand: 'Maxxis',
    category: 'other',
    price: 80,
    logoPath: '/logos/partners/maxxis.svg',
    description: 'High-performance road tire 700x28C'
  },
  {
    id: 'rockshox-recon',
    name: 'RockShox Recon',
    brand: 'RockShox',
    category: 'other',
    price: 450,
    logoPath: '/logos/partners/rockshox.svg',
    description: 'Air suspension fork 150mm travel'
  },
  {
    id: 'jagwire-cables',
    name: 'JAGWIRE Cables',
    brand: 'JAGWIRE',
    category: 'other',
    price: 50,
    logoPath: '/logos/partners/jagwire.svg',
    description: 'Premium cable and housing set'
  },
  {
    id: 'bafang-m820',
    name: 'Bafang M820',
    brand: 'Bafang',
    category: 'other',
    price: 1200,
    logoPath: '/logos/partners/bafang.svg',
    description: 'Mid-drive motor system 36V/48V 250W'
  },
  {
    id: 'tektro-m535',
    name: 'Tektro M535',
    brand: 'Tektro',
    category: 'brakes',
    price: 180,
    logoPath: '/logos/partners/tektro.svg',
    description: '4-piston hydraulic disc brakes 203mm'
  },
];

export function getComponentsByCategory(category: Component['category']): Component[] {
  return components.filter(c => c.category === category);
}

export function getComponentById(id: string): Component | undefined {
  return components.find(c => c.id === id);
}
