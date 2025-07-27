import React from 'react';
import { Search, AlertCircle } from 'lucide-react';
import ResultCard from './ResultCard';

interface Result {
  id: string;
  image: string;
  name: string;
  description?: string;
}

interface ResultsGalleryProps {
  results: Result[];
  query?: string;
  onViewDetails: (result: Result) => void;
}

export default function ResultsGallery({ results, query, onViewDetails }: ResultsGalleryProps) {
  if (results.length === 0) {
    return (
      <div className="text-center py-16">
        <div className="mx-auto w-16 h-16 bg-gray-100 rounded-full flex items-center justify-center mb-4">
          <Search className="w-8 h-8 text-gray-400" />
        </div>
        <h3 className="text-lg font-medium text-gray-900 mb-2">No se encontraron resultados</h3>
        <p className="text-gray-500">
          Intenta ajustar tu búsqueda o subir una imagen diferente
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-xl font-semibold text-gray-900">Resultados de Búsqueda</h2>
          {query && (
            <p className="text-sm text-gray-500 mt-1">
              Se encontraron {results.length} resultado{results.length !== 1 ? 's' : ''} para "{query}"
            </p>
          )}
        </div>
        <div className="flex items-center space-x-2 text-sm text-gray-500">
          <AlertCircle className="w-4 h-4" />
          <span>Resultados ordenados por relevancia</span>
        </div>
      </div>
      
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        {results.map((result) => (
          <ResultCard
            key={result.id}
            image={result.image}
            name={result.name}
            description={result.description}
            onViewDetails={() => onViewDetails(result)}
          />
        ))}
      </div>
    </div>
  );
}