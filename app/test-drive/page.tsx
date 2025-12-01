'use client';

import { useState, useEffect } from 'react';

interface Bike {
  id: number;
  name: string;
}

export default function TestDrivePage() {
  const [bikes, setBikes] = useState<Bike[]>([]);
  const [formData, setFormData] = useState({
    bikeId: '',
    name: '',
    email: '',
    phone: '',
    preferredDate: '',
    preferredTime: '',
    message: '',
  });
  const [submitted, setSubmitted] = useState(false);

  useEffect(() => {
    fetchBikes();
  }, []);

  const fetchBikes = async () => {
    try {
      const response = await fetch('/api/bikes');
      const data = await response.json();
      setBikes(data);
    } catch (error) {
      console.error('Error fetching bikes:', error);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetch('/api/test-drive', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });
      
      if (response.ok) {
        setSubmitted(true);
        setFormData({
          bikeId: '',
          name: '',
          email: '',
          phone: '',
          preferredDate: '',
          preferredTime: '',
          message: '',
        });
      }
    } catch (error) {
      console.error('Error submitting test drive request:', error);
      alert('Error submitting request. Please try again.');
    }
  };

  if (submitted) {
    return (
      <div className="flex-1 flex items-center justify-center bg-rift-dark">
        <div className="text-center p-8 border border-rift-gold rounded-lg bg-rift-card">
          <h2 className="text-3xl font-bold text-rift-gold mb-4">Test Drive Request Submitted</h2>
          <p className="text-white/80 mb-6">We'll contact you soon to confirm your test drive appointment.</p>
          <button
            onClick={() => setSubmitted(false)}
            className="rift-button"
          >
            Book Another Test Drive
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="flex-1 py-12 bg-rift-dark">
      <div className="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-4xl font-bold text-white mb-8 text-center">Book a Test Drive</h1>
        
        <form onSubmit={handleSubmit} className="bg-rift-card border border-rift-emerald rounded-lg p-8">
          <div className="mb-6">
            <label htmlFor="bikeId" className="block text-rift-gold font-bold mb-2">
              Select Bike
            </label>
            <select
              id="bikeId"
              value={formData.bikeId}
              onChange={(e) => setFormData({ ...formData, bikeId: e.target.value })}
              className="w-full bg-emerald-900 text-white border border-rift-emerald rounded px-4 py-2 focus:border-rift-gold focus:outline-none"
              required
            >
              <option value="">Choose a bike...</option>
              {bikes.map((bike) => (
                <option key={bike.id} value={bike.id}>
                  {bike.name}
                </option>
              ))}
            </select>
          </div>

          <div className="mb-6">
            <label htmlFor="name" className="block text-rift-gold font-bold mb-2">
              Full Name
            </label>
            <input
              type="text"
              id="name"
              value={formData.name}
              onChange={(e) => setFormData({ ...formData, name: e.target.value })}
              className="w-full bg-emerald-900 text-white border border-rift-emerald rounded px-4 py-2 focus:border-rift-gold focus:outline-none"
              required
            />
          </div>

          <div className="mb-6">
            <label htmlFor="email" className="block text-rift-gold font-bold mb-2">
              Email
            </label>
            <input
              type="email"
              id="email"
              value={formData.email}
              onChange={(e) => setFormData({ ...formData, email: e.target.value })}
              className="w-full bg-emerald-900 text-white border border-rift-emerald rounded px-4 py-2 focus:border-rift-gold focus:outline-none"
              required
            />
          </div>

          <div className="mb-6">
            <label htmlFor="phone" className="block text-rift-gold font-bold mb-2">
              Phone Number
            </label>
            <input
              type="tel"
              id="phone"
              value={formData.phone}
              onChange={(e) => setFormData({ ...formData, phone: e.target.value })}
              className="w-full bg-emerald-900 text-white border border-rift-emerald rounded px-4 py-2 focus:border-rift-gold focus:outline-none"
              required
            />
          </div>

          <div className="grid md:grid-cols-2 gap-6 mb-6">
            <div>
              <label htmlFor="preferredDate" className="block text-rift-gold font-bold mb-2">
                Preferred Date
              </label>
              <input
                type="date"
                id="preferredDate"
                value={formData.preferredDate}
                onChange={(e) => setFormData({ ...formData, preferredDate: e.target.value })}
                className="w-full bg-emerald-900 text-white border border-rift-emerald rounded px-4 py-2 focus:border-rift-gold focus:outline-none"
                required
              />
            </div>

            <div>
              <label htmlFor="preferredTime" className="block text-rift-gold font-bold mb-2">
                Preferred Time
              </label>
              <input
                type="time"
                id="preferredTime"
                value={formData.preferredTime}
                onChange={(e) => setFormData({ ...formData, preferredTime: e.target.value })}
                className="w-full bg-emerald-900 text-white border border-rift-emerald rounded px-4 py-2 focus:border-rift-gold focus:outline-none"
                required
              />
            </div>
          </div>

          <div className="mb-6">
            <label htmlFor="message" className="block text-rift-gold font-bold mb-2">
              Additional Notes (Optional)
            </label>
            <textarea
              id="message"
              value={formData.message}
              onChange={(e) => setFormData({ ...formData, message: e.target.value })}
              rows={4}
              className="w-full bg-emerald-900 text-white border border-rift-emerald rounded px-4 py-2 focus:border-rift-gold focus:outline-none"
            />
          </div>

          <button type="submit" className="w-full rift-button">
            Submit Test Drive Request
          </button>
        </form>
      </div>
    </div>
  );
}

