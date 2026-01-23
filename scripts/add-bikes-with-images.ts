import { openDatabase } from '../lib/db';
import * as fs from 'fs';
import * as path from 'path';

interface BikeData {
  name: string;
  description: string;
  basePrice: number;
  category: string;
  displayImage?: string;
  displayVideo?: string;
  images?: string[];
  videos?: string[];
  specifications?: any;
}

async function addBikesWithImages() {
  const db = await openDatabase();
  const organizedBikesPath = path.join(process.cwd(), 'organized_bikes_refined');

  // Check which bikes exist
  const bikeFolders = fs.readdirSync(organizedBikesPath, { withFileTypes: true })
    .filter(dirent => dirent.isDirectory())
    .map(dirent => dirent.name);

  console.log('Found bike folders:', bikeFolders);

  for (const bikeFolder of bikeFolders) {
    const bikePath = path.join(organizedBikesPath, bikeFolder);

    // Get available images and videos
    const cleanImages = getFiles(path.join(bikePath, 'images/clean'));
    const detailImages = getFiles(path.join(bikePath, 'images/details'));
    const colorImages = getFiles(path.join(bikePath, 'images/colors'));
    const videos = getFiles(path.join(bikePath, 'videos'));
    const specs = getFiles(path.join(bikePath, 'specs'));

    // Get specifications if available
    let specifications: any = null;
    if (specs.length > 0) {
      const specFile = specs[0];
      console.log(`\n📄 Found spec file: ${specFile}`);
      // Note: You'll need to manually extract specs from the image or provide them
    }

    // All available images
    const allImages = [...cleanImages, ...detailImages, ...colorImages];
    
    console.log(`\n📸 ${bikeFolder}:`);
    console.log(`   Clean images: ${cleanImages.length}`);
    console.log(`   Detail images: ${detailImages.length}`);
    console.log(`   Color images: ${colorImages.length}`);
    console.log(`   Videos: ${videos.length}`);

    // Prioritize videos as display images - use first video, fallback to first clean image
    const suggestedDisplayVideo = videos[0];
    const suggestedDisplayImage = cleanImages[0] || allImages[0];

    // Create bike data structure
    const bikeData: BikeData = {
      name: formatBikeName(bikeFolder),
      description: generateDescription(bikeFolder),
      basePrice: estimatePrice(bikeFolder),
      category: determineCategory(bikeFolder),
      displayImage: suggestedDisplayImage ? convertToPublicPath(suggestedDisplayImage, bikeFolder) : undefined,
      displayVideo: suggestedDisplayVideo ? convertToPublicPath(suggestedDisplayVideo, bikeFolder) : undefined,
      images: allImages.map(img => convertToPublicPath(img, bikeFolder)),
      videos: videos.map(vid => convertToPublicPath(vid, bikeFolder)),
      specifications: specifications
    };

    console.log(`\n✅ Prepared bike data for: ${bikeData.name}`);
    console.log(`   Display Image: ${bikeData.displayImage || 'None'}`);
    console.log(`   Display Video: ${bikeData.displayVideo || 'None'}`);
    console.log(`   Total Images: ${bikeData.images?.length || 0}`);
    console.log(`   Total Videos: ${bikeData.videos?.length || 0}`);

    // Add to database - videos are used as display images
    try {
      await db.run(
        `INSERT INTO bikes (name, description, basePrice, specifications, category, imageUrl, videoUrl) 
         VALUES (?, ?, ?, ?, ?, ?, ?)`,
        [
          bikeData.name,
          bikeData.description,
          bikeData.basePrice,
          bikeData.specifications ? JSON.stringify(bikeData.specifications) : null,
          bikeData.category,
          bikeData.displayImage || null,
          bikeData.displayVideo || null  // Video is the primary display
        ]
      );
      console.log(`✅ Added ${bikeData.name} to database`);
    } catch (error) {
      console.error(`❌ Error adding ${bikeData.name}:`, error);
    }
  }

  console.log('\n📋 Summary:');
  console.log('   All bikes have been processed and added to the database.');
}

function getFiles(dirPath: string): string[] {
  try {
    if (!fs.existsSync(dirPath)) return [];
    return fs.readdirSync(dirPath)
      .filter(file => {
        const ext = path.extname(file).toLowerCase();
        return ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.mp4', '.mov', '.webm'].includes(ext);
      })
      .map(file => path.join(dirPath, file));
  } catch {
    return [];
  }
}

function formatBikeName(folderName: string): string {
  // Convert folder names to display names
  const nameMap: { [key: string]: string } = {
    'CYCLONE-3rd': 'RIFT Cyclone 3rd',
    'R10pro-disc': 'RIFT R10 Pro Disc',
    'R5pro-Term': 'RIFT R5 Pro Term',
    'T10pro-2rd': 'RIFT T10 Pro 2nd'
  };
  return nameMap[folderName] || `RIFT ${folderName}`;
}

function generateDescription(folderName: string): string {
  const descriptions: { [key: string]: string } = {
    'CYCLONE-3rd': 'High-performance road bike with aerodynamic design. Features Shimano 105 Di2 electronic shifting and carbon frame construction.',
    'R10pro-disc': 'Premium disc brake road bike with advanced carbon frame technology. Designed for speed and precision.',
    'R5pro-Term': 'Professional-grade road bike with lightweight carbon construction. Perfect for competitive cycling.',
    'T10pro-2rd': 'Top-tier road bike with cutting-edge design and premium components. Built for performance and style.'
  };
  return descriptions[folderName] || 'Premium custom-built bike with top-quality components and craftsmanship.';
}

function estimatePrice(folderName: string): number {
  // Estimate prices based on model
  const prices: { [key: string]: number } = {
    'CYCLONE-3rd': 2499,
    'R10pro-disc': 2999,
    'R5pro-Term': 2799,
    'T10pro-2rd': 3199
  };
  return prices[folderName] || 2500;
}

function determineCategory(folderName: string): string {
  if (folderName.toLowerCase().includes('em') || folderName.toLowerCase().includes('mountain')) {
    return 'E-Mountain';
  }
  return 'Performance';
}

function convertToPublicPath(filePath: string, bikeFolder: string): string {
  // Convert absolute path to public path
  // Example: /home/tau/RIFT/organized_bikes_refined/CYCLONE-3rd/images/clean/4.jpg
  // -> /bikes/CYCLONE-3rd/images/clean/4.jpg
  const relativePath = path.relative(
    path.join(process.cwd(), 'organized_bikes_refined'),
    filePath
  );
  return `/bikes/${relativePath.replace(/\\/g, '/')}`;
}

// Run the script
addBikesWithImages().catch(console.error);
