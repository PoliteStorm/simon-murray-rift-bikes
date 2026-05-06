interface LogoProps {
  size?: 'small' | 'large';
}

export default function Logo({ size = 'small' }: LogoProps) {
  const isLarge = size === 'large';

  return (
    <span
      className={`text-rift-gold font-extrabold uppercase leading-none select-none ${
        isLarge ? 'text-4xl tracking-[0.32em]' : 'text-2xl tracking-[0.32em]'
      }`}
      style={{ textShadow: '0 0 12px rgba(251,191,36,0.25)' }}
      aria-label="RIFT"
    >
      RIFT
    </span>
  );
}
