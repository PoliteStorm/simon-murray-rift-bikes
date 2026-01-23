import { NextRequest, NextResponse } from 'next/server';
import { openDatabase } from '@/lib/db';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { bikeId, customization, customerInfo, deposit, totalPrice, paymentMethod } = body;

    const db = await openDatabase();
    const result = await db.run(
      `INSERT INTO orders (bikeId, customization, customerInfo, deposit, totalPrice, status, paymentMethod) 
       VALUES (?, ?, ?, ?, ?, ?, ?)`,
      [
        bikeId,
        JSON.stringify(customization),
        JSON.stringify(customerInfo),
        deposit,
        totalPrice,
        'pending',
        paymentMethod || 'bank_transfer'
      ]
    );

    // Log order for Simon Murray to contact customer
    console.log('=== NEW ORDER - CONTACT SIMON MURRAY ===');
    console.log(`Order ID: ${result.lastID}`);
    console.log(`Customer: ${customerInfo.name}`);
    console.log(`Email: ${customerInfo.email}`);
    console.log(`Phone: ${customerInfo.phone}`);
    console.log(`Bike ID: ${bikeId}`);
    console.log(`Deposit Required: £${deposit}`);
    console.log(`Total Price: £${totalPrice}`);
    console.log('==========================================');

    return NextResponse.json({ id: result.lastID, success: true }, { status: 201 });
  } catch (error) {
    console.error('Error creating order:', error);
    return NextResponse.json({ error: 'Failed to create order' }, { status: 500 });
  }
}


