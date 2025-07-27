import React, { useRef, useState } from 'react';
import { Upload, Image, X } from 'lucide-react';

interface ImageUploadProps {
  onImageUpload: (file: File) => void;
  isLoading?: boolean;
}

export default function ImageUpload({ onImageUpload, isLoading }: ImageUploadProps) {
  const [dragActive, setDragActive] = useState(false);
  const [selectedImage, setSelectedImage] = useState<string | null>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  const handleDrag = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === 'dragenter' || e.type === 'dragover') {
      setDragActive(true);
    } else if (e.type === 'dragleave') {
      setDragActive(false);
    }
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);

    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFile(e.dataTransfer.files[0]);
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    e.preventDefault();
    if (e.target.files && e.target.files[0]) {
      handleFile(e.target.files[0]);
    }
  };

  const handleFile = (file: File) => {
    if (file.type.startsWith('image/')) {
      const url = URL.createObjectURL(file);
      setSelectedImage(url);
      onImageUpload(file);
    }
  };

  const clearImage = () => {
    setSelectedImage(null);
    if (inputRef.current) {
      inputRef.current.value = '';
    }
  };

  return (
    <div className="space-y-4">
      <div
        className={`relative border-2 border-dashed rounded-xl p-8 text-center transition-colors ${
          dragActive
            ? 'border-indigo-400 bg-indigo-50'
            : selectedImage
            ? 'border-green-300 bg-green-50'
            : 'border-gray-300 hover:border-gray-400'
        } ${isLoading ? 'opacity-50 cursor-not-allowed' : 'cursor-pointer'}`}
        onDragEnter={handleDrag}
        onDragLeave={handleDrag}
        onDragOver={handleDrag}
        onDrop={handleDrop}
        onClick={() => !isLoading && inputRef.current?.click()}
      >
        <input
          ref={inputRef}
          type="file"
          accept="image/*"
          onChange={handleChange}
          className="hidden"
          disabled={isLoading}
        />

        {selectedImage ? (
          <div className="space-y-4">
            <div className="relative inline-block">
              <img
                src={selectedImage}
                alt="Selected"
                className="max-h-32 rounded-lg shadow-sm"
              />
              <button
                onClick={(e) => {
                  e.stopPropagation();
                  clearImage();
                }}
                className="absolute -top-2 -right-2 bg-red-500 text-white rounded-full p-1 hover:bg-red-600 transition-colors"
                disabled={isLoading}
              >
                <X className="w-4 h-4" />
              </button>
            </div>
            <p className="text-sm text-green-600 font-medium">Imagen lista para análisis</p>
          </div>
        ) : (
          <div className="space-y-4">
            <div className="mx-auto w-12 h-12 bg-gray-100 rounded-full flex items-center justify-center">
              <Upload className="w-6 h-6 text-gray-400" />
            </div>
            <div>
              <p className="text-lg font-medium text-gray-700">
                Arrastra tu imagen aquí, o <span className="text-indigo-600">examinar</span>
              </p>
              <p className="text-sm text-gray-500 mt-1">
                Soporta JPG, PNG, GIF hasta 10MB
              </p>
            </div>
          </div>
        )}
      </div>

      {selectedImage && (
        <button
          onClick={() => selectedImage && inputRef.current?.files?.[0] && onImageUpload(inputRef.current.files[0])}
          disabled={isLoading}
          className="w-full bg-indigo-600 text-white py-3 px-6 rounded-xl font-medium hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 disabled:bg-gray-300 disabled:cursor-not-allowed transition-colors"
        >
          {isLoading ? 'Analizando...' : 'Analizar Imagen'}
        </button>
      )}
    </div>
  );
}