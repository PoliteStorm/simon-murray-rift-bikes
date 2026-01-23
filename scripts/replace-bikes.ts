import { openDatabase } from '../lib/db';
import { processNewBikes } from './process-new-bikes';
import * as fs from 'fs';
import * as path from 'path';

async function replaceAllBikes() {
  const db = await openDatabase();
  
  console.log('🗑️  Removing all existing bikes...\n');
  
  // Delete all existing bikes
  await db.run('DELETE FROM bikes');
  console.log('✅ All existing bikes removed\n');
  
  // Process new bikes
  const bikes = await processNewBikes();
  
  console.log('\n📝 Adding new bikes to database...\n');
  
  for (const bike of bikes) {
    try {
      // Read the Excel file to get full specs
      const newBikesPath = path.join(process.cwd(), 'new_bikes_extract');
      let specFile = '';
      
      if (bike.model === 'CYCLONE-3rd') {
        specFile = path.join(newBikesPath, 'CYCLONE-3rd (105 big)-Specifications.xlsx');
      } else if (bike.model === 'EM19') {
        specFile = path.join(newBikesPath, 'EM19-Specifications.xlsx');
      }
      
      // Store spec file path and images array
      const specifications = {
        model: bike.model,
        specFile: specFile,
        images: bike.images || [],
        ...bike.specifications
      };
      
      await db.run(
        `INSERT INTO bikes (name, description, basePrice, specifications, category, imageUrl, videoUrl) 
         VALUES (?, ?, ?, ?, ?, ?, ?)`,
        [
          bike.name,
          bike.description,
          bike.basePrice,
          JSON.stringify(specifications),
          bike.category,
          bike.imageUrl || null,
          bike.videoUrl || null
        ]
      );
      
      console.log(`✅ Added ${bike.name} to database`);
    } catch (error) {
      console.error(`❌ Error adding ${bike.name}:`, error);
    }
  }
  
  console.log('\n✅ Database updated with new bikes!');
}

replaceAllBikes().catch(console.error);
