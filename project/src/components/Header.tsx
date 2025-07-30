import React from 'react';
import { Search, Settings } from 'lucide-react';

interface HeaderProps {
  selectedModel: 'openai' | 'google';
  onModelChange: (model: 'openai' | 'google') => void;
}

export default function Header({ selectedModel, onModelChange }: HeaderProps) {
  return (
    <header className="bg-white border-b border-gray-200 px-6 py-4">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        <div className="flex items-center space-x-3">
          <div className="p-2 bg-indigo-50 rounded-lg">
            <Search className="w-6 h-6 text-indigo-600" />
          </div>
          <div>
            <h1 className="text-xl font-semibold text-gray-900">Búsqueda Visual</h1>
            <p className="text-sm text-gray-500">Identifica objetos y analiza sus detalles mediante IA</p>
          </div>
        </div>

        <div className="flex items-center space-x-4">
          <div className="flex items-center space-x-2">
            <Settings className="w-4 h-4 text-gray-400" />
            <label htmlFor="ai-model" className="text-sm font-medium text-gray-700">
              Modelo de IA:
            </label>
            <select
              id="ai-model"
              value={selectedModel}
              onChange={(e) => onModelChange(e.target.value as 'openai' | 'google')}
              className="px-3 py-1.5 text-sm border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 bg-white"
            >
              <option value="openai">ChatGPT</option>
              <option value="google">Google Gemini</option>
            </select>
          </div>
        </div>
      </div>
    </header>
  );
}