import { openDatabase } from '../lib/db';

async function updateBikeVideos() {
  const db = await openDatabase();
  
  console.log('📹 Updating bike videos...\n');
  
  // Update CYCLONE-3rd (Aero) with aero video
  await db.run(
    `UPDATE bikes SET videoUrl = ? WHERE name LIKE '%Cyclone%' OR name LIKE '%CYCLONE%'`,
    ['/bikes/CYCLONE-3rd/videos/rift-aero-pro.mp4']
  );
  console.log('✅ Updated CYCLONE-3rd (Aero) video');
  
  // Update EM19 (EV) with EV video
  await db.run(
    `UPDATE bikes SET videoUrl = ? WHERE name LIKE '%EM19%' OR name LIKE '%EM%'`,
    ['/bikes/EM19/videos/rift-em19.mp4']
  );
  console.log('✅ Updated EM19 (EV) video');
  
  // Verify updates
  const bikes = await db.all('SELECT id, name, videoUrl FROM bikes');
  console.log('\n📋 Current bike videos:');
  for (const bike of bikes) {
    console.log(`  ${bike.name}: ${bike.videoUrl || 'No video'}`);
  }
  
  console.log('\n✅ Videos updated!');
}

updateBikeVideos().catch(console.error);
