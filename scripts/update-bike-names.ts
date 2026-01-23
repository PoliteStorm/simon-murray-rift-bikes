import { openDatabase } from '../lib/db';

async function updateBikeNames() {
  const db = await openDatabase();
  
  console.log('🏷️  Updating bike names...\n');
  
  // Update CYCLONE-3rd to RIFT Rapid
  await db.run(
    `UPDATE bikes SET name = ? WHERE name LIKE '%Cyclone%' OR name LIKE '%CYCLONE%'`,
    ['RIFT Rapid']
  );
  console.log('✅ Updated CYCLONE-3rd → RIFT Rapid');
  
  // Update EM19 to RIFT Climb
  await db.run(
    `UPDATE bikes SET name = ? WHERE name LIKE '%EM19%' OR name LIKE '%EM%'`,
    ['RIFT Climb']
  );
  console.log('✅ Updated EM19 → RIFT Climb');
  
  // Verify updates
  const bikes = await db.all('SELECT id, name, category, basePrice FROM bikes');
  console.log('\n📋 Updated bike names:');
  for (const bike of bikes) {
    console.log(`  ${bike.name} (${bike.category}) - £${bike.basePrice}`);
  }
  
  console.log('\n✅ Bike names updated!');
}

updateBikeNames().catch(console.error);
