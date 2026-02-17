import { NextRequest, NextResponse } from 'next/server';

// This endpoint notifies Simon Murray about new orders
// In production, this would send an email or SMS
// For now, it logs the order details

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const { 
      orderId, 
      customerName, 
      customerEmail, 
      customerPhone,
      bikeId,
      deposit, 
      totalPrice,
      remainingBalance,
      message 
    } = body;

    // Log the order notification (in production, send email/SMS)
    console.log('=== NEW ORDER NOTIFICATION ===');
    console.log('Order ID:', orderId);
    console.log('Customer:', customerName);
    console.log('Email:', customerEmail);
    console.log('Phone:', customerPhone);
    console.log('Bike ID:', bikeId);
    console.log('Deposit:', `£${deposit}`);
    console.log('Total Price:', `£${totalPrice}`);
    console.log('Remaining Balance:', `£${remainingBalance}`);
    console.log('Message:', message);
    console.log('');
    console.log('DISTRIBUTOR ACTION REQUIRED:');
    console.log('1. Contact customer to arrange £500 deposit payment');
    console.log('2. Discuss bike specifications and customization');
    console.log('3. Send invoice with payment breakdown:');
    console.log(`   - Total Price: £${totalPrice}`);
    console.log(`   - Deposit Paid: £${deposit}`);
    console.log(`   - Remaining Balance: £${remainingBalance}`);
    console.log('4. Update order status after deposit received');
    console.log('');
    console.log('Contact Distributor:');
    console.log('Email: riftbike@outlook.com');
    console.log('WhatsApp: 07817174391');
    console.log('Phone: 01985-844563');
    console.log('=============================');

    // TODO: In production, implement:
    // - Email to riftbike@outlook.com with order details and invoice template
    // - SMS notification to 07817174391
    // - Admin dashboard notification
    // 
    // Email template should include:
    // - Customer contact information
    // - Order details and bike specifications
    // - Payment breakdown (deposit + remaining balance)
    // - Invoice template for distributor to send to customer
    // - Link to admin panel to update order status
    //
    // Example email service integration:
    // await sendEmail({
    //   to: 'riftbike@outlook.com',
    //   subject: `New Order #${orderId} - ${customerName} - Action Required`,
    //   body: generateInvoiceTemplate({
    //     orderId,
    //     customerName,
    //     customerEmail,
    //     customerPhone,
    //     bikeId,
    //     deposit,
    //     totalPrice,
    //     remainingBalance
    //   })
    // });

    return NextResponse.json({ 
      success: true,
      message: 'Order notification logged. Distributor should manually contact customer.',
      details: {
        orderId,
        deposit,
        totalPrice,
        remainingBalance,
        distributorEmail: 'riftbike@outlook.com',
        distributorWhatsApp: '07817174391',
        distributorPhone: '01985-844563'
      }
    });
  } catch (error: any) {
    console.error('Error sending order notification:', error);
    return NextResponse.json(
      { error: error.message || 'Failed to send notification' },
      { status: 500 }
    );
  }
}
