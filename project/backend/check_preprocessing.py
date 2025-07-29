"""
Verificador de estado del preprocesamiento
Comprueba si todos los archivos necesarios han sido generados
"""

import os
import json
from datetime import datetime

class PreprocessingChecker:
    def __init__(self, backend_dir="./backend"):
        self.backend_dir = backend_dir
        self.status_file = os.path.join(backend_dir, ".preprocessing_status.json")
        
    def check_file_exists(self, file_path, description):
        """Verifica si un archivo existe"""
        full_path = os.path.join(self.backend_dir, file_path)
        exists = os.path.exists(full_path)
        
        print(f"{'✅' if exists else '❌'} {description}")
        if exists:
            # Mostrar fecha de modificación
            mod_time = os.path.getmtime(full_path)
            mod_date = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d %H:%M:%S")
            print(f"   📅 Última modificación: {mod_date}")
        else:
            print(f"   📁 Esperado en: {full_path}")
            
        return exists
    
    def check_preprocessing_status(self):
        """Verifica el estado del preprocesamiento"""
        print("🔍 Verificando estado del preprocesamiento...\n")
        
        # Lista de archivos que deberían existir después del preprocesamiento
        required_files = [
            # Archivos de texto procesado (pueden variar según implementación)
            ("preprocesamiento_texto/__pycache__/", "Cache de preprocesamiento de texto"),
            
            # Archivos de imágenes procesadas
            ("preprocesamiento_img/__pycache__/", "Cache de preprocesamiento de imágenes"),
            
            # Archivos de conexión
            ("conexion_img_txt/__pycache__/", "Cache de conexión img-txt"),
            
            # Dataset principal
            ("data/dataset_autos_descripciones.json", "Dataset principal"),
            
            # Carpeta de imágenes
            ("data/img/", "Carpeta de imágenes"),
        ]
        
        all_good = True
        checked_files = 0
        
        for file_path, description in required_files:
            exists = self.check_file_exists(file_path, description)
            if not exists:
                all_good = False
            checked_files += 1
            print()  # Línea en blanco
        
        # Verificar status file
        status_exists = os.path.exists(self.status_file)
        
        print(f"📊 Resumen:")
        print(f"   📁 Archivos verificados: {checked_files}")
        print(f"   {'✅' if all_good else '❌'} Estado general: {'Completo' if all_good else 'Incompleto'}")
        
        if status_exists:
            self.show_last_preprocessing_info()
        else:
            print(f"   ℹ️ No hay registro de preprocesamiento previo")
            
        return all_good
    
    def show_last_preprocessing_info(self):
        """Muestra información del último preprocesamiento"""
        try:
            with open(self.status_file, 'r', encoding='utf-8') as f:
                status = json.load(f)
                
            print(f"   📅 Último preprocesamiento: {status.get('last_run', 'Desconocido')}")
            print(f"   ⏱️ Duración: {status.get('duration', 'Desconocido')} segundos")
            print(f"   ✅ Scripts exitosos: {status.get('successful_scripts', 0)}")
            
        except Exception as e:
            print(f"   ⚠️ Error leyendo status: {str(e)}")
    
    def mark_preprocessing_complete(self, duration=0, successful_scripts=0):
        """Marca el preprocesamiento como completado"""
        status = {
            'last_run': datetime.now().isoformat(),
            'duration': duration,
            'successful_scripts': successful_scripts,
            'status': 'completed'
        }
        
        try:
            with open(self.status_file, 'w', encoding='utf-8') as f:
                json.dump(status, f, indent=2, ensure_ascii=False)
            print(f"✅ Estado guardado en: {self.status_file}")
        except Exception as e:
            print(f"⚠️ Error guardando estado: {str(e)}")
    
    def needs_preprocessing(self):
        """Determina si se necesita ejecutar el preprocesamiento"""
        return not self.check_preprocessing_status()

def main():
    """Función principal para verificación standalone"""
    print("🔍 VERIFICADOR DE PREPROCESAMIENTO")
    print("="*50)
    
    checker = PreprocessingChecker()
    needs_prep = checker.needs_preprocessing()
    
    print("\n" + "="*50)
    if needs_prep:
        print("🚨 Se requiere ejecutar el preprocesamiento")
        print("💡 Ejecuta: python init_preprocessing.py")
    else:
        print("🎉 El preprocesamiento está completo")
        print("🚀 Puedes ejecutar: npm run dev")
    
    return not needs_prep

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
