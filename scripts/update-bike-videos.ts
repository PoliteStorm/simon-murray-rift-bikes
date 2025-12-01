import { openDatabase } from '../lib/db';

async function updateBikeVideos() {
  const db = await openDatabase();

  try {
    // Update RIFT Aero Pro with video
    await db.run(
      'UPDATE bikes SET videoUrl = ? WHERE name = ?',
      ['/videos/rift-aero-pro.mp4', 'RIFT Aero Pro']
    );

    // Update RIFT EM19 with video
    await db.run(
      'UPDATE bikes SET videoUrl = ? WHERE name = ?',
      ['/videos/rift-em19.mp4', 'RIFT EM19']
    );

    console.log('Bike videos updated successfully!');
    
    // Show updated bikes
    const bikes = await db.all('SELECT id, name, videoUrl FROM bikes');
    console.log('Updated bikes:');
    bikes.forEach((bike: any) => {
      console.log(`- ${bike.name}: ${bike.videoUrl || 'No video'}`);
    });
  } catch (error) {
    console.error('Error updating bike videos:', error);
  }
}

updateBikeVideos();

