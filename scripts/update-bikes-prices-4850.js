#!/usr/bin/env node
/**
 * One-off update: drop RIFT ULTIMATE and RIFT GRAVEL EXTREME to £4,850.
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

  await db.run(
    `UPDATE bikes SET basePrice = 4850 WHERE name IN ('RIFT ULTIMATE', 'RIFT GRAVEL EXTREME')`
  );
  console.log('✅ RIFT ULTIMATE and RIFT GRAVEL EXTREME price set to £4,850');

  await db.close();
  console.log('\nDone.');
}

run().catch((e) => {
  console.error(e);
  process.exit(1);
});
