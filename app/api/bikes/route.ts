import { NextRequest, NextResponse } from 'next/server';
import { openDatabase } from '@/lib/db';
import { initialBikes } from '@/lib/bikes-data';

export async function GET() {
  try {
    const db = await openDatabase();
    const bikes = await db.all('SELECT * FROM bikes ORDER BY id DESC');
    
    // If database is empty or error, return initial bikes
    if (!Array.isArray(bikes) || bikes.length === 0) {
      console.log('Database empty or unavailable, returning initial bikes');
      return NextResponse.json(initialBikes);
    }
    
    return NextResponse.json(bikes);
  } catch (error) {
    console.error('Error fetching bikes from database:', error);
    // Return initial bikes as fallback
    console.log('Returning initial bikes as fallback');
    return NextResponse.json(initialBikes);
  }
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { name, description, basePrice, imageUrl, videoUrl, specifications, category } = body;

    const db = await openDatabase();
    const result = await db.run(
      'INSERT INTO bikes (name, description, basePrice, imageUrl, videoUrl, specifications, category) VALUES (?, ?, ?, ?, ?, ?, ?)',
      [name, description, basePrice, imageUrl || null, videoUrl || null, specifications ? JSON.stringify(specifications) : null, category || null]
    );

    return NextResponse.json({ id: result.lastID, ...body }, { status: 201 });
  } catch (error) {
    console.error('Error adding bike:', error);
    return NextResponse.json({ error: 'Failed to add bike' }, { status: 500 });
  }
}

