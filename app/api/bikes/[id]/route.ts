import { NextRequest, NextResponse } from 'next/server';
import { openDatabase } from '@/lib/db';

export async function GET(
  request: NextRequest,
  { params }: { params: { id: string } }
) {
  try {
    const db = await openDatabase();
    const bike = await db.get('SELECT * FROM bikes WHERE id = ?', [params.id]);
    
    if (!bike) {
      return NextResponse.json({ error: 'Bike not found' }, { status: 404 });
    }
    
    return NextResponse.json(bike);
  } catch (error) {
    console.error('Error fetching bike:', error);
    return NextResponse.json({ error: 'Failed to fetch bike' }, { status: 500 });
  }
}

export async function PUT(
  request: NextRequest,
  { params }: { params: { id: string } }
) {
  try {
    const body = await request.json();
    const { name, description, basePrice, imageUrl, videoUrl } = body;

    const db = await openDatabase();
    await db.run(
      'UPDATE bikes SET name = ?, description = ?, basePrice = ?, imageUrl = ?, videoUrl = ? WHERE id = ?',
      [name, description, basePrice, imageUrl || null, videoUrl || null, params.id]
    );

    return NextResponse.json({ success: true });
  } catch (error) {
    console.error('Error updating bike:', error);
    return NextResponse.json({ error: 'Failed to update bike' }, { status: 500 });
  }
}

export async function DELETE(
  request: NextRequest,
  { params }: { params: { id: string } }
) {
  try {
    const db = await openDatabase();
    await db.run('DELETE FROM bikes WHERE id = ?', [params.id]);

    return NextResponse.json({ success: true });
  } catch (error) {
    console.error('Error deleting bike:', error);
    return NextResponse.json({ error: 'Failed to delete bike' }, { status: 500 });
  }
}


