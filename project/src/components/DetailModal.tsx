import React from 'react';
import { X } from 'lucide-react';

interface Result {
  id: string;
  image: string;
  name: string;
  description?: string;
}

interface DetailModalProps {
  result: Result | null;
  isOpen: boolean;
  onClose: () => void;
  onSearchSimilar: (query: string) => void;
}

export default function DetailModal({ result, isOpen, onClose, onSearchSimilar }: DetailModalProps) {
  if (!isOpen || !result) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
      <div className="bg-white rounded-xl shadow-xl max-w-2xl w-full max-h-[90vh] flex flex-col">
        {/* Header */}
        <div className="flex items-center justify-between p-6 border-b border-gray-200">
          <h2 className="text-xl font-semibold text-gray-900">Detalles del Objeto</h2>
          <button
            onClick={onClose}
            className="p-2 hover:bg-gray-100 rounded-lg transition-colors"
          >
            <X className="w-5 h-5 text-gray-500" />
          </button>
        </div>

        {/* Content */}
        <div className="p-6 space-y-6 flex-1 overflow-y-auto">
          {/* Image */}
          <div className="aspect-video bg-gray-100 rounded-lg overflow-hidden">
            <img
              src={result.image}
              alt={result.name}
              className="w-full h-full object-cover"
            />
          </div>

          {/* Object Info */}
          <div className="space-y-4">
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2">{result.name}</h3>
              {result.description && (
                <p className="text-gray-600 leading-relaxed">{result.description}</p>
              )}
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="flex justify-end space-x-3 p-6 border-t border-gray-200 bg-gray-50 flex-shrink-0">
          <button
            onClick={onClose}
            className="px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
          >
            Cerrar
          </button>
          <button 
            onClick={() => {
              onSearchSimilar(result.name);
              onClose();
            }}
            className="px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors"
          >
            Buscar Similar
          </button>
        </div>
      </div>
    </div>
  );
}