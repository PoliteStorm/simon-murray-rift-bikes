import { NextRequest, NextResponse } from 'next/server';
import { openDatabase } from '@/lib/db';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { bikeId, name, email, phone, preferredDate, preferredTime, message } = body;

    const db = await openDatabase();
    await db.run(
      'INSERT INTO test_drives (bikeId, name, email, phone, preferredDate, preferredTime, message) VALUES (?, ?, ?, ?, ?, ?, ?)',
      [bikeId, name, email, phone, preferredDate, preferredTime, message || null]
    );

    return NextResponse.json({ success: true }, { status: 201 });
  } catch (error) {
    console.error('Error submitting test drive request:', error);
    return NextResponse.json({ error: 'Failed to submit test drive request' }, { status: 500 });
  }
}


