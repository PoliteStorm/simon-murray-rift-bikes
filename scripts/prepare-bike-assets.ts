import * as fs from 'fs';
import * as path from 'path';

/**
 * This script helps prepare bike assets by:
 * 1. Listing all available images and videos for each bike
 * 2. Copying selected assets to public/bikes folder
 * 3. Generating a summary for manual review
 */

const organizedBikesPath = path.join(process.cwd(), 'organized_bikes_refined');
const publicBikesPath = path.join(process.cwd(), 'public/bikes');

interface BikeAssetInfo {
  folder: string;
  cleanImages: string[];
  detailImages: string[];
  colorImages: string[];
  videos: string[];
  specs: string[];
  suggestedDisplayImage?: string;
  suggestedDisplayVideo?: string;
}

function getAllBikeAssets(): BikeAssetInfo[] {
  if (!fs.existsSync(organizedBikesPath)) {
    console.error('❌ organized_bikes_refined folder not found!');
    return [];
  }

  const bikeFolders = fs.readdirSync(organizedBikesPath, { withFileTypes: true })
    .filter(dirent => dirent.isDirectory())
    .map(dirent => dirent.name);

  const assets: BikeAssetInfo[] = [];

  for (const folder of bikeFolders) {
    const bikePath = path.join(organizedBikesPath, folder);
    
    const cleanImages = getImageFiles(path.join(bikePath, 'images/clean'));
    const detailImages = getImageFiles(path.join(bikePath, 'images/details'));
    const colorImages = getImageFiles(path.join(bikePath, 'images/colors'));
    const videos = getVideoFiles(path.join(bikePath, 'videos'));
    const specs = getFiles(path.join(bikePath, 'specs'));

    assets.push({
      folder,
      cleanImages,
      detailImages,
      colorImages,
      videos,
      specs,
      suggestedDisplayImage: cleanImages[0] || detailImages[0] || colorImages[0],
      suggestedDisplayVideo: videos[0]
    });
  }

  return assets;
}

function getImageFiles(dirPath: string): string[] {
  return getFiles(dirPath).filter(file => {
    const ext = path.extname(file).toLowerCase();
    return ['.jpg', '.jpeg', '.png', '.gif', '.webp'].includes(ext);
  });
}

function getVideoFiles(dirPath: string): string[] {
  return getFiles(dirPath).filter(file => {
    const ext = path.extname(file).toLowerCase();
    return ['.mp4', '.mov', '.webm', '.avi'].includes(ext);
  });
}

function getFiles(dirPath: string): string[] {
  try {
    if (!fs.existsSync(dirPath)) return [];
    return fs.readdirSync(dirPath)
      .map(file => path.join(dirPath, file))
      .filter(filePath => fs.statSync(filePath).isFile());
  } catch {
    return [];
  }
}

function copyAssetToPublic(sourcePath: string, bikeFolder: string, relativePath: string): string {
  const publicPath = path.join(publicBikesPath, bikeFolder, relativePath);
  const publicDir = path.dirname(publicPath);
  
  // Create directory structure
  if (!fs.existsSync(publicDir)) {
    fs.mkdirSync(publicDir, { recursive: true });
  }

  // Copy file
  fs.copyFileSync(sourcePath, publicPath);
  return `/bikes/${bikeFolder}/${relativePath.replace(/\\/g, '/')}`;
}

function generateSummary(assets: BikeAssetInfo[]): void {
  console.log('\n📋 BIKE ASSETS SUMMARY\n');
  console.log('='.repeat(60));

  for (const asset of assets) {
    console.log(`\n🚲 ${asset.folder}`);
    console.log('-'.repeat(60));
    console.log(`   Clean Images: ${asset.cleanImages.length}`);
    if (asset.cleanImages.length > 0) {
      console.log(`   → Suggested Display: ${path.basename(asset.suggestedDisplayImage || '')}`);
    }
    console.log(`   Detail Images: ${asset.detailImages.length}`);
    console.log(`   Color Images: ${asset.colorImages.length}`);
    console.log(`   Videos: ${asset.videos.length}`);
    if (asset.videos.length > 0) {
      console.log(`   → Suggested Display Video: ${path.basename(asset.suggestedDisplayVideo || '')}`);
    }
    console.log(`   Spec Files: ${asset.specs.length}`);
  }

  console.log('\n' + '='.repeat(60));
  console.log('\n💡 Next Steps:');
  console.log('   1. Review the suggested display images/videos above');
  console.log('   2. Run: npm run prepare-bikes to copy assets to public folder');
  console.log('   3. Update add-bikes-with-images.ts with your selections');
  console.log('   4. Run the add-bikes script to add to database\n');
}

function copyAllAssets(assets: BikeAssetInfo[]): void {
  console.log('\n📦 Copying assets to public/bikes folder...\n');

  // Ensure public/bikes exists
  if (!fs.existsSync(publicBikesPath)) {
    fs.mkdirSync(publicBikesPath, { recursive: true });
  }

  let totalCopied = 0;

  for (const asset of assets) {
    console.log(`📁 Processing ${asset.folder}...`);
    
    // Copy clean images
    for (const img of asset.cleanImages) {
      const relativePath = path.relative(
        path.join(organizedBikesPath, asset.folder, 'images/clean'),
        img
      );
      copyAssetToPublic(img, asset.folder, `images/clean/${relativePath}`);
      totalCopied++;
    }

    // Copy detail images
    for (const img of asset.detailImages) {
      const relativePath = path.relative(
        path.join(organizedBikesPath, asset.folder, 'images/details'),
        img
      );
      copyAssetToPublic(img, asset.folder, `images/details/${relativePath}`);
      totalCopied++;
    }

    // Copy color images
    for (const img of asset.colorImages) {
      const relativePath = path.relative(
        path.join(organizedBikesPath, asset.folder, 'images/colors'),
        img
      );
      copyAssetToPublic(img, asset.folder, `images/colors/${relativePath}`);
      totalCopied++;
    }

    // Copy videos
    for (const vid of asset.videos) {
      const relativePath = path.relative(
        path.join(organizedBikesPath, asset.folder, 'videos'),
        vid
      );
      copyAssetToPublic(vid, asset.folder, `videos/${relativePath}`);
      totalCopied++;
    }

    console.log(`   ✅ Copied ${asset.cleanImages.length + asset.detailImages.length + asset.colorImages.length + asset.videos.length} files`);
  }

  console.log(`\n✅ Total files copied: ${totalCopied}`);
}

// Main execution
const command = process.argv[2];

if (command === 'copy') {
  const assets = getAllBikeAssets();
  copyAllAssets(assets);
} else {
  const assets = getAllBikeAssets();
  generateSummary(assets);
}
