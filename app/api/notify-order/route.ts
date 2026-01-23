import { NextRequest, NextResponse } from 'next/server';

// This endpoint notifies Simon Murray about new orders
// In production, this would send an email or SMS
// For now, it logs the order details

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { orderId, customerName, customerEmail, amount, message } = body;

    // Log the order notification (in production, send email/SMS to Simon Murray)
    console.log('=== NEW ORDER NOTIFICATION ===');
    console.log('Order ID:', orderId);
    console.log('Customer:', customerName);
    console.log('Email:', customerEmail);
    console.log('Amount:', `£${amount}`);
    console.log('Message:', message);
    console.log('Contact: Simon Murray');
    console.log('=============================');

    // TODO: In production, implement:
    // - Email to si@riftbike.com
    // - SMS notification to 07817174391
    // - Admin dashboard notification
    // Example email service:
    // await sendEmail({
    //   to: 'si@riftbike.com',
    //   subject: `New Order #${orderId} - ${customerName}`,
    //   body: message
    // });

    return NextResponse.json({ 
      success: true,
      message: 'Order notification sent'
    });
  } catch (error: any) {
    console.error('Error sending order notification:', error);
    return NextResponse.json(
      { error: error.message || 'Failed to send notification' },
      { status: 500 }
    );
  }
}
