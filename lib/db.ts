import sqlite3 from 'sqlite3';
import { open } from 'sqlite';
import path from 'path';
import { promisify } from 'util';

let db: any = null;

export async function openDatabase() {
  if (db) return db;

  const dbPath = path.join(process.cwd(), 'rift.db');
  
  db = await open({
    filename: dbPath,
    driver: sqlite3.Database,
  });

  // Initialize tables
  await db.exec(`
    CREATE TABLE IF NOT EXISTS bikes (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      description TEXT NOT NULL,
      basePrice REAL NOT NULL,
      imageUrl TEXT,
      videoUrl TEXT,
      specifications TEXT,
      category TEXT,
      createdAt DATETIME DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS test_drives (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      bikeId INTEGER,
      name TEXT NOT NULL,
      email TEXT NOT NULL,
      phone TEXT NOT NULL,
      preferredDate TEXT NOT NULL,
      preferredTime TEXT NOT NULL,
      message TEXT,
      status TEXT DEFAULT 'pending',
      createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY (bikeId) REFERENCES bikes(id)
    );

    CREATE TABLE IF NOT EXISTS orders (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      bikeId INTEGER,
      customization TEXT NOT NULL,
      customerInfo TEXT NOT NULL,
      deposit REAL NOT NULL,
      totalPrice REAL NOT NULL,
      status TEXT DEFAULT 'pending',
      createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
      FOREIGN KEY (bikeId) REFERENCES bikes(id)
    );
  `);

  return db;
}

