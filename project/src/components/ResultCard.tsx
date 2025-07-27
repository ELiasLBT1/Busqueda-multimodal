import React from 'react';
import { Eye } from 'lucide-react';

interface ResultCardProps {
  image: string;
  name: string;
  description?: string;
  onViewDetails: () => void;
}

export default function ResultCard({ image, name, description, onViewDetails }: ResultCardProps) {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden hover:shadow-md transition-shadow duration-200 flex flex-col h-full">
      <div className="aspect-square bg-gray-100 relative overflow-hidden">
        <img
          src={image}
          alt={name}
          className="w-full h-full object-cover"
        />
      </div>
      
      <div className="p-4 flex flex-col flex-1">
        <h3 className="text-lg font-semibold text-gray-900 mb-1">{name}</h3>
        {description && (
          <p className="text-sm text-gray-600 line-clamp-2 mb-3">{description}</p>
        )}
        
        <div className="mt-auto">
          <button 
            onClick={onViewDetails}
            className="text-indigo-600 hover:text-indigo-800 text-sm font-medium transition-colors"
          >
            Ver Detalles
          </button>
        </div>
      </div>
    </div>
  );
}