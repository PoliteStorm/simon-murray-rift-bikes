#!/usr/bin/env node
/**
 * One-off update: RIFT ULTIMATE and RIFT GRAVEL EXTREME to £4,995;
 * RIFT GRAVEL EXTREME: remove wrong image, set video to mp4;
 * Remove RIFT GRAVEL V3.
 */
const sqlite3 = require('sqlite3');
const { open } = require('sqlite');
const path = require('path');

async function run() {
  const dbPath = path.join(process.cwd(), 'rift.db');
  const db = await open({
    filename: dbPath,
    driver: sqlite3.Database,
  });

  await db.run(`UPDATE bikes SET basePrice = 4995 WHERE name = 'RIFT ULTIMATE'`);
  console.log('✅ RIFT ULTIMATE price set to £4,995');

  await db.run(
    `UPDATE bikes SET basePrice = 4995, imageUrl = NULL, videoUrl = ? WHERE name = 'RIFT GRAVEL EXTREME'`,
    ['/bikes/rift-gravel-extreme.mp4']
  );
  console.log('✅ RIFT GRAVEL EXTREME: price £4,995, image removed, video set to mp4');

  const del = await db.run(`DELETE FROM bikes WHERE name = 'RIFT GRAVEL V3'`);
  console.log('✅ RIFT GRAVEL V3 removed from database');

  await db.close();
  console.log('\nDone.');
}

run().catch((e) => {
  console.error(e);
  process.exit(1);
});
