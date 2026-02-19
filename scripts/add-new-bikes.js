const sqlite3 = require('sqlite3');
const { open } = require('sqlite');
const path = require('path');

async function addNewBikes() {
  const dbPath = path.join(process.cwd(), 'rift.db');
  
  const db = await open({
    filename: dbPath,
    driver: sqlite3.Database,
  });

  // Check if bikes already exist
  const existingUltimate = await db.get('SELECT id FROM bikes WHERE name = ?', ['RIFT ULTIMATE']);
  const existingGravelExtreme = await db.get('SELECT id FROM bikes WHERE name = ?', ['RIFT GRAVEL EXTREME']);
  const existingGravelV3 = await db.get('SELECT id FROM bikes WHERE name = ?', ['RIFT GRAVEL V3']);

  // Add RIFT ULTIMATE if it doesn't exist (Ultimate video as main + spec sheet)
  if (!existingUltimate) {
    await db.run(`
      INSERT INTO bikes (name, description, basePrice, imageUrl, videoUrl, category, specifications)
      VALUES (?, ?, ?, ?, ?, ?, ?)
    `, [
      'RIFT ULTIMATE',
      'The ultimate performance road bike featuring T1000 aerospace carbon throughout, Di2 electronic gears with Shimano Ultegra setup. Complete with pedals, seat, and water bottle with carrier. Custom built just for you.',
      4500,
      '/bikes/rift-ultimate.jpg',
      '/bikes/rift-ultimate.mp4',
      'Road',
      JSON.stringify({
        frame: 'T1000 Aerospace Carbon',
        gears: 'Shimano Ultegra Di2 Electronic',
        wheels: 'Carbon Wheelset',
        brakes: 'Hydraulic Disc',
        weight: 'Ultra-lightweight',
        included: 'Pedals, Seat, Water Bottle with Carrier',
        images: ['/bikes/rift-ultimate.jpg', '/bikes/rift-ultimate-spec.jpeg'],
        specSheetUrl: '/bikes/rift-ultimate-spec.jpeg'
      })
    ]);
    console.log('✅ Added RIFT ULTIMATE');
  } else {
    console.log('⚠️  RIFT ULTIMATE already exists');
  }

  // Add RIFT GRAVEL EXTREME if it doesn't exist
  if (!existingGravelExtreme) {
    await db.run(`
      INSERT INTO bikes (name, description, basePrice, imageUrl, category, specifications)
      VALUES (?, ?, ?, ?, ?, ?)
    `, [
      'RIFT GRAVEL EXTREME',
      'Extreme gravel performance with T1000 aerospace carbon, Di2 electronic gears with Shimano Ultegra. Built for adventure on any terrain. Complete with pedals, seat, and water bottle with carrier. Custom built just for you.',
      4200,
      '/bikes/rift-gravel-extreme.jpg',
      'Gravel',
      JSON.stringify({
        frame: 'T1000 Aerospace Carbon',
        gears: 'Shimano Ultegra Di2 Electronic',
        wheels: 'Gravel Wheelset',
        brakes: 'Hydraulic Disc',
        tires: 'All-terrain',
        included: 'Pedals, Seat, Water Bottle with Carrier'
      })
    ]);
    console.log('✅ Added RIFT GRAVEL EXTREME');
  } else {
    console.log('⚠️  RIFT GRAVEL EXTREME already exists');
  }

  // Add RIFT GRAVEL V3 (GRAVEL zip - images + video)
  if (!existingGravelV3) {
    await db.run(`
      INSERT INTO bikes (name, description, basePrice, imageUrl, videoUrl, category, specifications)
      VALUES (?, ?, ?, ?, ?, ?, ?)
    `, [
      'RIFT GRAVEL V3',
      'Gravel V3 wireless with T1000 aerospace carbon and Shimano 105 groupset. Built for mixed terrain and adventure. Complete with pedals, seat, and water bottle with carrier. Every bike is custom built just for you.',
      4100,
      '/bikes/rift-gravel-v3.jpg',
      '/bikes/rift-gravel-v3.mp4',
      'Gravel',
      JSON.stringify({
        model: 'Gravel V3 wireless (25yr 105 big)',
        frame: 'T1000 Aerospace Carbon',
        gears: 'Shimano 105',
        wheels: 'Gravel Wheelset',
        brakes: 'Hydraulic Disc',
        tires: 'All-terrain',
        included: 'Pedals, Seat, Water Bottle with Carrier',
        images: ['/bikes/rift-gravel-v3.jpg', '/bikes/rift-gravel-v3-2.jpg']
      })
    ]);
    console.log('✅ Added RIFT GRAVEL V3');
  } else {
    console.log('⚠️  RIFT GRAVEL V3 already exists');
  }

  await db.close();
  console.log('\n✅ Done! New bikes added to database.');
}

addNewBikes().catch(console.error);
