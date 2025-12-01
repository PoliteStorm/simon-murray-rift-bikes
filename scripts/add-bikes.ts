import { openDatabase } from '../lib/db';

async function addBikes() {
  const db = await openDatabase();

  // RIFT Aero Pro (Road Bike) - White road bike
  const roadBikeSpecs = {
    model: "RIFT Aero Pro",
    confRev: "R7170-24S, Di2 big, carbon Rim&Wave",
    wheelSize: "700C",
    frameHeight: "43.5cm, 46cm, 48cm, 50cm, 52cm, 54cm",
    bikeColor: "White / MatteBlack / MatteDarkGray / Others, Full Holographic color / 3K gloss Black / 3K gloss Green",
    netWeight: "8.3KG",
    frame: "RIFT Aero Pro (Disc&thru-axle 12x142), high modulus Carbon fiber, Aero, Inner-Cables",
    handlebarSets: "TW, high modulus Carbon fiber 3K, Integrated Handlebar&Stem (400*90mm), full Inner-Cables",
    seatPost: "High modulus Carbon fiber, Aero-Racing",
    clamps: "Hidden Screw Fit to Frame",
    fork: "RIFT Aero Pro (Disc&thru-axle 12×100), high modulus Carbon fiber, 700C",
    headSets: "Alu alloy CNC with sealed-Bearings 52*52mm",
    washer: "Dedicated for Inner-Cables",
    derailleurHandle: "SHIMANO 105/R7170 - 2*12S, DI2",
    frontDerailleur: "SHIMANO 105/R7150 - 2S, DI2",
    rearDerailleur: "SHIMANO 105/R7150 - 12S, DI2",
    cranksets: "SHIMANO 105/R7100, 34-50T",
    cassettes: "SHIMANO 105/R7100-12S, 11-34T",
    chain: "SHIMANO M7100-12S",
    bb: "Threaded T47*24mm, Hollow&Bearings",
    brake: "SHIMANO 105/R7170 Hydr.disc, 160/160",
    hubs: "RS, Alu alloy&SuperLight, 54T Ratchet, 4-sealed Bearings, HG, F24*R24H, Centerlock Disc&thru-axle F12*100_R12*142",
    rim: "RS, high modulus Carbon fiber&Wave, W28×H50mm",
    spoke: "SHUNJIU, Flat 14G",
    tyre: "MAXXIS-PURSUER, Foldable & LighWeight, 700*28C, Black",
    belt: "PU with Comfortable&Skid resistant",
    saddle: "SR, lightweight for racing",
    pedals: "Alu alloy with sealed-Bearings",
    cables: "JAGWIRE",
    accessories: "Standard safety reflector for Handlebar+Seat post+Front wheel+Rear wheel, PC bottle cage+Tools, Manual+Warranty card"
  };

  // RIFT EM19 (E-Mountain Bike) - Dark green e-MTB
  const emtbSpecs = {
    model: "RIFT EM19",
    confRev: "M6100/12S+M820, HIGH",
    frameSize: "29(27.5)×16\"/18\"",
    bikeColor: "Black / DarkGray / DarkGreen / DarkRed",
    netWeight: "21.3KG",
    frame: "RIFT EM19, High modulus Carbon fiber, Inner cables, Thru-axle 12*148 Boost, UDH tail hook, 140mm Travel, DNM rear shox200*55",
    handlebarSets: "RS, Alu alloy, Matte, Handlebar 31.8×720, Stem 60, Clamps 34.9mm",
    seatPost: "KS adjustable lifting with hydr., Remote, 31.6**395*125",
    fork: "ROCKSHOX-RECON, Air, Manual, 150, Thru-axle 15*110",
    headSets: "Alu alloy CNC with sealed Bearings 52*52mm",
    derailleurLever: "SHIMANO DEORE/M6100-12S",
    rearDerailleur: "SHIMANO DEORE/M6100-12S",
    cranksets: "Matching with Mid Motor, 34T",
    cassettes: "SUNSHINE-12S, 11-50T",
    chain: "SUMC-12S",
    brake: "TEKTRO-M535, 4-piston hydraulic disc, 203/203mm",
    hub: "RS, Alu alloy, 4-sealed Bearings, Slotted, Disc, 32Holes, Thru-axle F15×110_R12×148mm Boost",
    rim: "RS, Alu alloy with Double-wall&Rivets, W24×H19mm",
    spoke: "SHUNJIU, Circular 14G",
    tire: "MAXXIS, 29/27.5×2.4\"",
    grips: "Circular 22.2×120mm, PU leather&locking Ring",
    saddle: "RS, Comfortable and Thickened for MTB",
    pedals: "RS, Alu alloy CNC with Bearings for MTB",
    motorSystem: "Bafang Mid, M820, 36V250W (48V250W)",
    maxTorque: "75 N.m (Peak 95N.m)",
    speedLimit: "25KMh Default (max 45KMh)",
    pedalSensor: "Torque+Speed(cadence)",
    battery: "Samsung 21700 Li-ion, 720Wh, 36V20A (48V15A)",
    endurance: "Max 130-150KM (pedal assist)",
    chargingTime: "6-7 Hours",
    charger: "3A, DC2.1",
    hmi: "Bafang C030, LCD digital",
    waterproof: "IP X6",
    maxLoad: "130 KG"
  };

  try {
    // Add Road Bike
    await db.run(
      `INSERT INTO bikes (name, description, basePrice, specifications, category) 
       VALUES (?, ?, ?, ?, ?)`,
      [
        'RIFT Aero Pro',
        'High-performance aerodynamic road bike designed for speed and efficiency. Carbon frame with aggressive geometry for competitive riders. Features Shimano 105 Di2 electronic shifting and carbon wheels.',
        2499,
        JSON.stringify(roadBikeSpecs),
        'Performance'
      ]
    );

    // Add E-Mountain Bike
    await db.run(
      `INSERT INTO bikes (name, description, basePrice, specifications, category) 
       VALUES (?, ?, ?, ?, ?)`,
      [
        'RIFT EM19',
        'Full-suspension electric mountain bike with 140mm travel. Features Bafang M820 mid-drive motor, RockShox suspension, and Shimano Deore 12-speed drivetrain. Perfect for trail riding and mountain adventures.',
        4499,
        JSON.stringify(emtbSpecs),
        'E-Mountain'
      ]
    );

    console.log('Bikes added successfully!');
  } catch (error) {
    console.error('Error adding bikes:', error);
  }
}

addBikes();


