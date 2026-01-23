import { openDatabase } from '../lib/db';
import * as fs from 'fs';
import * as path from 'path';

async function exportBikes() {
  try {
    const db = await openDatabase();
    const bikes = await db.all('SELECT * FROM bikes ORDER BY id');
    
    const exportPath = path.join(process.cwd(), 'lib', 'bikes-data.ts');
    
    const bikesData = `// Exported bikes data - used as fallback when database is unavailable
// This file is auto-generated - do not edit manually
export const initialBikes = ${JSON.stringify(bikes, null, 2)};
`;
    
    fs.writeFileSync(exportPath, bikesData);
    console.log(`✅ Exported ${bikes.length} bikes to ${exportPath}`);
    console.log(`\nBikes exported:`);
    bikes.forEach((bike: any) => {
      console.log(`  - ${bike.name} (ID: ${bike.id})`);
    });
  } catch (error) {
    console.error('Error exporting bikes:', error);
  }
}

exportBikes().catch(console.error);
