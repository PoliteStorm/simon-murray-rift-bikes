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

    // Log order for contact
    console.log('=== NEW ORDER - CONTACT REQUIRED ===');
    console.log(`Order ID: ${result.lastID}`);
    console.log(`Customer: ${customerInfo.name}`);
    console.log(`Email: ${customerInfo.email}`);
    console.log(`Phone: ${customerInfo.phone}`);
    console.log(`Bike ID: ${bikeId}`);
    console.log(`Deposit Required: £${deposit}`);
    console.log(`Total Price: £${totalPrice}`);
    console.log(`Remaining Balance: £${totalPrice - deposit}`);
    console.log(`Contact Distributor: riftbike@outlook.com, WhatsApp: 07817174391, Phone: 01985-844563`);
    console.log('==========================================');

    // Send notification to distributor
    // In production, this would send an email notification
    // For now, we log the notification details
    try {
      await fetch(`${request.nextUrl.origin}/api/notify-order`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          orderId: result.lastID,
          customerName: customerInfo.name,
          customerEmail: customerInfo.email,
          customerPhone: customerInfo.phone,
          bikeId,
          deposit,
          totalPrice,
          remainingBalance: totalPrice - deposit,
          message: `New order received from ${customerInfo.name}. Please contact customer to arrange deposit payment and discuss specifications.`
        })
      });
    } catch (notifyError) {
      console.error('Failed to send notification:', notifyError);
      // Don't fail the order if notification fails
    }

    return NextResponse.json({ 
      id: result.lastID, 
      success: true,
      deposit,
      totalPrice,
      remainingBalance: totalPrice - deposit
    }, { status: 201 });
  } catch (error) {
    console.error('Error creating order:', error);
    return NextResponse.json({ error: 'Failed to create order' }, { status: 500 });
  }
}


