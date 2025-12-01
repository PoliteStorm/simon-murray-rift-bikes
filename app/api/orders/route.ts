import { NextRequest, NextResponse } from 'next/server';
import { openDatabase } from '@/lib/db';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { bikeId, customization, customerInfo, deposit, totalPrice } = body;

    const db = await openDatabase();
    const result = await db.run(
      `INSERT INTO orders (bikeId, customization, customerInfo, deposit, totalPrice, status) 
       VALUES (?, ?, ?, ?, ?, ?)`,
      [
        bikeId,
        JSON.stringify(customization),
        JSON.stringify(customerInfo),
        deposit,
        totalPrice,
        'pending'
      ]
    );

    return NextResponse.json({ id: result.lastID, success: true }, { status: 201 });
  } catch (error) {
    console.error('Error creating order:', error);
    return NextResponse.json({ error: 'Failed to create order' }, { status: 500 });
  }
}


