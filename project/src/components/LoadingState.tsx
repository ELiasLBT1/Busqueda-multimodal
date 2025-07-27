import React from 'react';
import { Loader2 } from 'lucide-react';

interface LoadingStateProps {
  message?: string;
}

export default function LoadingState({ message = "Analizando con IA..." }: LoadingStateProps) {
  return (
    <div className="flex flex-col items-center justify-center py-16 space-y-4">
      <Loader2 className="w-12 h-12 text-indigo-600 animate-spin" />
      <div className="text-center">
        <p className="text-lg font-medium text-gray-900">{message}</p>
        <p className="text-sm text-gray-500 mt-1">Esto puede tomar unos momentos...</p>
      </div>
    </div>
  );
}