'use client';

import { useState, useEffect } from 'react';

interface Bike {
  id: number;
  name: string;
  description: string;
  basePrice: number;
  imageUrl?: string;
  videoUrl?: string;
}

export default function AdminPage() {
  const [bikes, setBikes] = useState<Bike[]>([]);
  const [loading, setLoading] = useState(true);
  const [showAddForm, setShowAddForm] = useState(false);
  const [editingBike, setEditingBike] = useState<Bike | null>(null);
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    basePrice: '',
    imageUrl: '',
    videoUrl: '',
  });

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
    } finally {
      setLoading(false);
    }
  };

  const handleAddBike = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await fetch('/api/bikes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          ...formData,
          basePrice: parseFloat(formData.basePrice),
        }),
      });
      
      if (response.ok) {
        fetchBikes();
        setFormData({ name: '', description: '', basePrice: '', imageUrl: '', videoUrl: '' });
        setShowAddForm(false);
      }
    } catch (error) {
      console.error('Error adding bike:', error);
      alert('Error adding bike. Please try again.');
    }
  };

  const handleUpdateBike = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!editingBike) return;
    
    try {
      const response = await fetch(`/api/bikes/${editingBike.id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          ...formData,
          basePrice: parseFloat(formData.basePrice),
        }),
      });
      
      if (response.ok) {
        fetchBikes();
        setEditingBike(null);
        setFormData({ name: '', description: '', basePrice: '', imageUrl: '', videoUrl: '' });
      }
    } catch (error) {
      console.error('Error updating bike:', error);
      alert('Error updating bike. Please try again.');
    }
  };

  const handleDeleteBike = async (id: number) => {
    if (!confirm('Are you sure you want to delete this bike?')) return;
    
    try {
      const response = await fetch(`/api/bikes/${id}`, {
        method: 'DELETE',
      });
      
      if (response.ok) {
        fetchBikes();
      }
    } catch (error) {
      console.error('Error deleting bike:', error);
      alert('Error deleting bike. Please try again.');
    }
  };

  const startEdit = (bike: Bike) => {
    setEditingBike(bike);
    setFormData({
      name: bike.name,
      description: bike.description,
      basePrice: bike.basePrice.toString(),
      imageUrl: bike.imageUrl || '',
      videoUrl: bike.videoUrl || '',
    });
    setShowAddForm(true);
  };

  if (loading) {
    return (
      <div className="flex-1 flex items-center justify-center bg-rift-dark">
        <p className="text-rift-gold text-xl">Loading...</p>
      </div>
    );
  }

  return (
    <div className="flex-1 py-12 bg-rift-dark">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-4xl font-bold text-white">Admin Panel</h1>
          <button
            onClick={() => {
              setShowAddForm(!showAddForm);
              setEditingBike(null);
              setFormData({ name: '', description: '', basePrice: '', imageUrl: '', videoUrl: '' });
            }}
            className="rift-button"
          >
            {showAddForm ? 'Cancel' : 'Add New Bike'}
          </button>
        </div>

        {showAddForm && (
          <div className="bg-rift-card border border-rift-emerald rounded-lg p-6 mb-8">
            <h2 className="text-2xl font-bold text-white mb-4">
              {editingBike ? 'Edit Bike' : 'Add New Bike'}
            </h2>
            <form onSubmit={editingBike ? handleUpdateBike : handleAddBike} className="space-y-4">
              <div>
                <label className="block text-rift-gold font-bold mb-2">Bike Name</label>
                <input
                  type="text"
                  value={formData.name}
                  onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                  className="w-full bg-emerald-900 text-white border border-rift-emerald rounded px-4 py-2 focus:border-rift-gold focus:outline-none"
                  required
                />
              </div>

              <div>
                <label className="block text-rift-gold font-bold mb-2">Description</label>
                <textarea
                  value={formData.description}
                  onChange={(e) => setFormData({ ...formData, description: e.target.value })}
                  rows={3}
                  className="w-full bg-emerald-900 text-white border border-rift-emerald rounded px-4 py-2 focus:border-rift-gold focus:outline-none"
                  required
                />
              </div>

              <div>
                <label className="block text-rift-gold font-bold mb-2">Base Price (£)</label>
                <input
                  type="number"
                  step="0.01"
                  value={formData.basePrice}
                  onChange={(e) => setFormData({ ...formData, basePrice: e.target.value })}
                  className="w-full bg-emerald-900 text-white border border-rift-emerald rounded px-4 py-2 focus:border-rift-gold focus:outline-none"
                  required
                />
              </div>

              <div>
                <label className="block text-rift-gold font-bold mb-2">Image URL (Optional)</label>
                <input
                  type="url"
                  value={formData.imageUrl}
                  onChange={(e) => setFormData({ ...formData, imageUrl: e.target.value })}
                  className="w-full bg-emerald-900 text-white border border-rift-emerald rounded px-4 py-2 focus:border-rift-gold focus:outline-none"
                  placeholder="https://example.com/image.jpg"
                />
              </div>

              <div>
                <label className="block text-rift-gold font-bold mb-2">Video URL (Optional)</label>
                <input
                  type="url"
                  value={formData.videoUrl}
                  onChange={(e) => setFormData({ ...formData, videoUrl: e.target.value })}
                  className="w-full bg-emerald-900 text-white border border-rift-emerald rounded px-4 py-2 focus:border-rift-gold focus:outline-none"
                  placeholder="https://example.com/video.mp4"
                />
              </div>

              <button type="submit" className="rift-button">
                {editingBike ? 'Update Bike' : 'Add Bike'}
              </button>
            </form>
          </div>
        )}

        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
          {bikes.map((bike) => (
            <div key={bike.id} className="bg-rift-card border border-rift-emerald rounded-lg p-6">
              <h3 className="text-xl font-bold text-white mb-2">{bike.name}</h3>
              <p className="text-white/80 mb-4 text-sm">{bike.description}</p>
              <p className="text-white font-bold mb-4">£{bike.basePrice.toLocaleString()}</p>
              <div className="flex space-x-2">
                <button
                  onClick={() => startEdit(bike)}
                  className="flex-1 rift-button-secondary text-sm py-2"
                >
                  Edit
                </button>
                <button
                  onClick={() => handleDeleteBike(bike.id)}
                  className="flex-1 bg-red-600 hover:bg-red-700 text-white font-bold py-2 px-4 rounded-lg transition-colors text-sm"
                >
                  Delete
                </button>
              </div>
            </div>
          ))}
        </div>

        {bikes.length === 0 && !showAddForm && (
          <div className="text-center py-12">
            <p className="text-white/60 text-lg">No bikes added yet. Click "Add New Bike" to get started.</p>
          </div>
        )}
      </div>
    </div>
  );
}

