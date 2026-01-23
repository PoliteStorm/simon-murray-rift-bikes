import { NextRequest, NextResponse } from 'next/server';
import { openDatabase } from '@/lib/db';

export async function GET() {
  try {
    const db = await openDatabase();
    const bikes = await db.all('SELECT * FROM bikes ORDER BY id DESC');
    // Always return an array, even if empty
    return NextResponse.json(Array.isArray(bikes) ? bikes : []);
  } catch (error) {
    console.error('Error fetching bikes:', error);
    // Return empty array instead of error object to prevent .map() errors
    return NextResponse.json([]);
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

