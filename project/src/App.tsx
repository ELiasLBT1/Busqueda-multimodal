import React, { useState } from 'react';
import Header from './components/Header';
import SearchInput from './components/SearchInput';
import ImageUpload from './components/ImageUpload';
import LoadingState from './components/LoadingState';
import ResultsGallery from './components/ResultsGallery';
import DetailModal from './components/DetailModal';

interface Result {
  id: string;
  image: string;
  name: string;
  description?: string;
}

function App() {
  const [selectedModel, setSelectedModel] = useState<'openai' | 'google'>('openai');
  const [isLoading, setIsLoading] = useState(false);
  const [results, setResults] = useState<Result[]>([]);
  const [currentQuery, setCurrentQuery] = useState<string>('');
  const [activeTab, setActiveTab] = useState<'text' | 'upload'>('text');
  const [selectedResult, setSelectedResult] = useState<Result | null>(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');

  // Mock data for demonstration
  const mockResults: Result[] = [
    {
      id: '1',
      image: 'https://images.pexels.com/photos/312418/pexels-photo-312418.jpeg?auto=compress&cs=tinysrgb&w=400',
      name: 'Taza de Café',
      description: 'Una taza de cerámica blanca con asa, comúnmente usada para bebidas calientes.'
    },
    {
      id: '2',
      image: 'https://images.pexels.com/photos/1267320/pexels-photo-1267320.jpeg?auto=compress&cs=tinysrgb&w=400',
      name: 'Computadora Portátil',
      description: 'Una computadora portátil moderna, probablemente usada para trabajo o tareas personales.'
    },
    {
      id: '3',
      image: 'https://images.pexels.com/photos/1402787/pexels-photo-1402787.jpeg?auto=compress&cs=tinysrgb&w=400',
      name: 'Teléfono Inteligente',
      description: 'Un teléfono móvil con capacidades de pantalla táctil y conectividad a internet.'
    }
  ];

  const handleSearch = async (query: string) => {
    setIsLoading(true);
    setCurrentQuery(query);
    setSearchQuery(query);
    
    // Simulate API call
    setTimeout(() => {
      setResults(mockResults);
      setIsLoading(false);
    }, 2000);
  };

  const handleImageUpload = async (file: File) => {
    setIsLoading(true);
    setCurrentQuery(`Imagen: ${file.name}`);
    
    // Simulate API call
    setTimeout(() => {
      setResults(mockResults);
      setIsLoading(false);
    }, 2000);
  };

  const handleViewDetails = (result: Result) => {
    setSelectedResult(result);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setSelectedResult(null);
  };

  const handleSearchSimilar = (query: string) => {
    setSearchQuery(query);
    setActiveTab('text');
    handleSearch(query);
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <Header 
        selectedModel={selectedModel} 
        onModelChange={setSelectedModel} 
      />
      
      <main className="max-w-7xl mx-auto px-6 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Search Panel */}
          <div className="lg:col-span-1 space-y-6">
            <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
              <h2 className="text-lg font-semibold text-gray-900 mb-4">Métodos de Búsqueda</h2>
              
              {/* Tab Navigation */}
              <div className="flex space-x-1 bg-gray-100 rounded-lg p-1 mb-6">
                <button
                  onClick={() => setActiveTab('text')}
                  className={`flex-1 py-2 px-3 text-sm font-medium rounded-md transition-colors ${
                    activeTab === 'text'
                      ? 'bg-white text-indigo-600 shadow-sm'
                      : 'text-gray-500 hover:text-gray-700'
                  }`}
                >
                  Texto
                </button>
                <button
                  onClick={() => setActiveTab('upload')}
                  className={`flex-1 py-2 px-3 text-sm font-medium rounded-md transition-colors ${
                    activeTab === 'upload'
                      ? 'bg-white text-indigo-600 shadow-sm'
                      : 'text-gray-500 hover:text-gray-700'
                  }`}
                >
                  Subir
                </button>
              </div>

              {/* Tab Content */}
              {activeTab === 'text' && (
                <SearchInput 
                  onSearch={handleSearch} 
                  isLoading={isLoading}
                  initialValue={searchQuery}
                />
              )}
              {activeTab === 'upload' && (
                <ImageUpload onImageUpload={handleImageUpload} isLoading={isLoading} />
              )}
            </div>

            {/* Model Info */}
            <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
              <h3 className="text-sm font-semibold text-gray-900 mb-2">Modelo Actual</h3>
              <div className="flex items-center space-x-3">
                <div className="w-2 h-2 bg-green-400 rounded-full"></div>
                <span className="text-sm text-gray-600">
                  {selectedModel === 'openai' ? 'OpenAI GPT-4o' : 'Google Gemini'}
                </span>
              </div>
              <p className="text-xs text-gray-500 mt-2">
                Modelo de IA avanzado para reconocimiento y análisis preciso de objetos
              </p>
            </div>
          </div>

          {/* Results Panel */}
          <div className="lg:col-span-2">
            <div className="bg-white rounded-xl shadow-sm border border-gray-200 min-h-[600px]">
              {isLoading ? (
                <LoadingState message={`Analizando con IA de ${selectedModel === 'openai' ? 'OpenAI' : 'Google'}...`} />
              ) : (
                <div className="p-6">
                  <ResultsGallery 
                    results={results} 
                    query={currentQuery} 
                    onViewDetails={handleViewDetails}
                  />
                </div>
              )}
            </div>
          </div>
        </div>

        <DetailModal
          result={selectedResult}
          isOpen={isModalOpen}
          onClose={closeModal}
          onSearchSimilar={handleSearchSimilar}
        />
      </main>
    </div>
  );
}

export default App;