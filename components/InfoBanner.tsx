'use client';

import { useState } from 'react';

interface InfoSection {
  title: string;
  content: string;
}

const infoSections: InfoSection[] = [
  {
    title: "RIFTBIKES",
    content: "Every bike features top quality carbon throughout the whole bike and often T1000 aerospace carbon is used along with Di2 electronic gears, and where possible Ultegra gear set up. All bikes are complete with pedals and seat and water bottle with carrier. Every bike is custom built just for you."
  },
  {
    title: "PAYMENT AND ORDERING",
    content: "Sample bikes can be viewed and then ordered depending on your specific colour and specifications. Deposit of £500 to be placed upon order."
  },
  {
    title: "COLOUR OPTIONS",
    content: "Ask about our unique colour options including stunning holographic colour choices."
  },
  {
    title: "DELIVERY",
    content: "Free delivery within 50 miles of our BA11 5ER postcode. Nationwide and Worldwide delivery can be made at unbeatable prices."
  },
  {
    title: "ALL CONTACT INFO",
    content: "All our contact info in one location. Simon - WhatsApp: 07817174391, Email: riftbike@outlook.com, Phone: 01985-844563"
  },
  {
    title: "VIEWINGS",
    content: "All viewings and test rides always welcomed and encouraged. Please get in touch."
  }
];

export default function InfoBanner() {
  const [expandedSection, setExpandedSection] = useState<string | null>(null);

  const toggleSection = (title: string) => {
    setExpandedSection(expandedSection === title ? null : title);
  };

  return (
    <div className="bg-rift-royal/80 border-b border-rift-gold/30 backdrop-blur-sm">
      <div className="max-w-7xl mx-auto">
        {/* Scrolling tabs */}
        <div className="flex overflow-x-auto scrollbar-hide">
          {infoSections.map((section) => (
            <button
              key={section.title}
              onClick={() => toggleSection(section.title)}
              className={`flex-shrink-0 px-6 py-3 text-sm font-semibold transition-all whitespace-nowrap border-b-2 ${
                expandedSection === section.title
                  ? 'text-rift-gold border-rift-gold bg-rift-dark/30'
                  : 'text-white/80 border-transparent hover:text-rift-gold hover:bg-rift-dark/20'
              }`}
            >
              {section.title}
            </button>
          ))}
        </div>
        
        {/* Expanded content */}
        {expandedSection && (
          <div className="bg-rift-dark/40 border-t border-rift-gold/20 p-6 animate-fadeIn">
            <div className="max-w-4xl">
              <h3 className="text-rift-gold font-bold text-lg mb-3">{expandedSection}</h3>
              <p className="text-white/80 text-sm leading-relaxed">
                {infoSections.find(s => s.title === expandedSection)?.content}
              </p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
