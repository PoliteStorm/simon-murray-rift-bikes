import * as fs from 'fs';
import * as path from 'path';
import * as XLSX from 'xlsx';
import { openDatabase } from '../lib/db';

const newBikesPath = path.join(process.cwd(), 'new_bikes_extract');
const publicBikesPath = path.join(process.cwd(), 'public/bikes');

interface BikeData {
  name: string;
  model: string;
  description: string;
  basePrice: number;
  category: string;
  imageUrl?: string;
  videoUrl?: string;
  specifications: any;
  images: string[];
}

function readExcelSpecs(filePath: string): any {
  try {
    const workbook = XLSX.readFile(filePath);
    const sheetName = workbook.SheetNames[0];
    const worksheet = workbook.Sheets[sheetName];
    const data = XLSX.utils.sheet_to_json(worksheet, { header: 1 });
    
    // Convert to object
    const specs: any = {};
    for (const row of data as any[][]) {
      if (row && row.length >= 2) {
        const key = String(row[0]).trim();
        const value = String(row[1]).trim();
        if (key && value) {
          specs[key] = value;
        }
      }
    }
    
    return specs;
  } catch (error) {
    console.error(`Error reading Excel file ${filePath}:`, error);
    return {};
  }
}

async function processNewBikes() {
  const db = await openDatabase();
  const files = fs.readdirSync(newBikesPath);
  
  console.log('📦 Processing new bikes from zip file...\n');
  
  // Find Excel files and images
  const excelFiles: { [key: string]: string } = {};
  const imageFiles: string[] = [];
  
  for (const file of files) {
    const filePath = path.join(newBikesPath, file);
    const ext = path.extname(file).toLowerCase();
    
    if (ext === '.xlsx') {
      if (file.includes('CYCLONE')) {
        excelFiles['CYCLONE-3rd'] = filePath;
      } else if (file.includes('EM19')) {
        excelFiles['EM19'] = filePath;
      }
    } else if (['.jpg', '.jpeg', '.png'].includes(ext)) {
      imageFiles.push(filePath);
    }
  }
  
  console.log('Found Excel files:', Object.keys(excelFiles));
  console.log('Found images:', imageFiles.length);
  
  // Process each bike
  const bikes: BikeData[] = [];
  
  // Process CYCLONE-3rd
  if (excelFiles['CYCLONE-3rd']) {
    const specs = readExcelSpecs(excelFiles['CYCLONE-3rd']);
    console.log('\n📄 CYCLONE-3rd Specifications:', Object.keys(specs));
    
    // Copy images to public folder
    const bikeImages: string[] = [];
    const bikeFolder = path.join(publicBikesPath, 'CYCLONE-3rd');
    if (!fs.existsSync(bikeFolder)) {
      fs.mkdirSync(bikeFolder, { recursive: true });
    }
    
    // For now, we'll need to manually identify which images belong to which bike
    // Copy all images and we'll organize them
    for (let i = 0; i < imageFiles.length; i++) {
      const imageFile = imageFiles[i];
      const imageName = `image-${i + 1}${path.extname(imageFile)}`;
      const destPath = path.join(bikeFolder, imageName);
      fs.copyFileSync(imageFile, destPath);
      bikeImages.push(`/bikes/CYCLONE-3rd/${imageName}`);
    }
    
    bikes.push({
      name: 'RIFT Cyclone 3rd',
      model: 'CYCLONE-3rd',
      description: specs['Description'] || 'High-performance road bike with aerodynamic design. Features Shimano 105 Di2 electronic shifting and carbon frame construction.',
      basePrice: parseFloat(specs['Price']) || 2499,
      category: 'Performance',
      imageUrl: bikeImages[0],
      specifications: specs,
      images: bikeImages
    });
  }
  
  // Process EM19
  if (excelFiles['EM19']) {
    const specs = readExcelSpecs(excelFiles['EM19']);
    console.log('\n📄 EM19 Specifications:', Object.keys(specs));
    
    // Copy images to public folder
    const bikeImages: string[] = [];
    const bikeFolder = path.join(publicBikesPath, 'EM19');
    if (!fs.existsSync(bikeFolder)) {
      fs.mkdirSync(bikeFolder, { recursive: true });
    }
    
    // For EM19, we'll need to identify which images belong to it
    // This might require manual review or image analysis
    for (let i = 0; i < imageFiles.length; i++) {
      const imageFile = imageFiles[i];
      const imageName = `image-${i + 1}${path.extname(imageFile)}`;
      const destPath = path.join(bikeFolder, imageName);
      fs.copyFileSync(imageFile, destPath);
      bikeImages.push(`/bikes/EM19/${imageName}`);
    }
    
    bikes.push({
      name: 'RIFT EM19',
      model: 'EM19',
      description: specs['Description'] || 'Full-suspension electric mountain bike with 140mm travel. Features Bafang M820 mid-drive motor, RockShox suspension, and Shimano Deore 12-speed drivetrain.',
      basePrice: parseFloat(specs['Price']) || 4499,
      category: 'E-Mountain',
      imageUrl: bikeImages[0],
      specifications: specs,
      images: bikeImages
    });
  }
  
  console.log('\n✅ Processed bikes:');
  for (const bike of bikes) {
    console.log(`\n${bike.name}:`);
    console.log(`  Price: £${bike.basePrice}`);
    console.log(`  Category: ${bike.category}`);
    console.log(`  Images: ${bike.images.length}`);
  }
  
  return bikes;
}

// Run if called directly
if (require.main === module) {
  processNewBikes().catch(console.error);
}

export { processNewBikes };
