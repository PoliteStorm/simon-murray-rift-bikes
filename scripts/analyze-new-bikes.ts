import * as fs from 'fs';
import * as path from 'path';
import { openDatabase } from '../lib/db';

// Note: We'll need to manually read Excel or convert to CSV
// For now, let's organize the files and create a structure

const newBikesPath = path.join(process.cwd(), 'new_bikes_extract');
const publicBikesPath = path.join(process.cwd(), 'public/bikes');

interface BikeInfo {
  name: string;
  model: string;
  images: string[];
  specFile: string;
  description: string;
  basePrice: number;
  category: string;
}

async function analyzeNewBikes() {
  const files = fs.readdirSync(newBikesPath);
  
  console.log('Files found:', files);
  
  // Organize files by bike
  const bikes: { [key: string]: BikeInfo } = {};
  
  for (const file of files) {
    const filePath = path.join(newBikesPath, file);
    const ext = path.extname(file).toLowerCase();
    
    if (ext === '.xlsx') {
      // Extract bike name from filename
      if (file.includes('CYCLONE')) {
        if (!bikes['CYCLONE-3rd']) {
          bikes['CYCLONE-3rd'] = {
            name: 'RIFT Cyclone 3rd',
            model: 'CYCLONE-3rd',
            images: [],
            specFile: filePath,
            description: 'High-performance road bike with aerodynamic design.',
            basePrice: 2499,
            category: 'Performance'
          };
        }
        bikes['CYCLONE-3rd'].specFile = filePath;
      } else if (file.includes('EM19')) {
        if (!bikes['EM19']) {
          bikes['EM19'] = {
            name: 'RIFT EM19',
            model: 'EM19',
            images: [],
            specFile: filePath,
            description: 'Full-suspension electric mountain bike with advanced features.',
            basePrice: 4499,
            category: 'E-Mountain'
          };
        }
        bikes['EM19'].specFile = filePath;
      }
    } else if (['.jpg', '.jpeg', '.png'].includes(ext)) {
      // Try to identify which bike the image belongs to
      // We'll need to check the image or organize them
      // For now, add to both and we'll manually sort
      const imagePath = filePath;
      
      // Copy to public folder structure
      // We'll organize these manually or by analyzing the images
      console.log(`Found image: ${file}`);
    }
  }
  
  console.log('\n📋 Bikes identified:');
  for (const [key, bike] of Object.entries(bikes)) {
    console.log(`\n${bike.name}:`);
    console.log(`  Model: ${bike.model}`);
    console.log(`  Spec File: ${bike.specFile}`);
    console.log(`  Category: ${bike.category}`);
    console.log(`  Price: £${bike.basePrice}`);
  }
  
  return bikes;
}

analyzeNewBikes().catch(console.error);
