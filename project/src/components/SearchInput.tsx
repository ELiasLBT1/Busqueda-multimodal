import React, { useState } from 'react';
import { Search, X } from 'lucide-react';

interface SearchInputProps {
  onSearch: (query: string) => void;
  isLoading?: boolean;
  initialValue?: string;
}

export default function SearchInput({ onSearch, isLoading, initialValue = '' }: SearchInputProps) {
  const [query, setQuery] = useState(initialValue);

  React.useEffect(() => {
    setQuery(initialValue);
  }, [initialValue]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (query.trim() && !isLoading) {
      onSearch(query.trim());
    }
  };

  const handleClear = () => {
    setQuery('');
  };

  return (
    <form onSubmit={handleSubmit} className="relative">
      <div className="relative">
        <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
          <Search className="h-5 w-5 text-gray-400" />
        </div>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Buscar automóviles..."
          className="w-full pl-12 pr-12 py-4 text-lg border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition-colors"
          disabled={isLoading}
        />
        {query && (
          <button
            type="button"
            onClick={handleClear}
            className="absolute inset-y-0 right-0 pr-4 flex items-center"
            disabled={isLoading}
          >
            <X className="h-5 w-5 text-gray-400 hover:text-gray-600 transition-colors" />
          </button>
        )}
      </div>
      <button
        type="submit"
        disabled={!query.trim() || isLoading}
        className="mt-3 w-full bg-indigo-600 text-white py-3 px-6 rounded-xl font-medium hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors"
      >
        {isLoading ? 'Buscando...' : 'Buscar'}
      </button>
    </form>
  );
}