const sqlite3 = require('sqlite3');
const { open } = require('sqlite');
const path = require('path');
const { app } = require('electron');

let db = null;

async function openDatabase() {
  if (db) return db;

  // Use the same database as the main website
  // Adjust path to point to the main project's database
  const dbPath = path.join(__dirname, '..', '..', 'rift.db');
  
  db = await open({
    filename: dbPath,
    driver: sqlite3.Database,
  });

  return db;
}

module.exports = { openDatabase };
