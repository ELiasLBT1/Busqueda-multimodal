#!/usr/bin/env python3
"""
Script de inicialización para ejecutar todos los preprocesadores necesarios
cuando se ejecuta el proyecto por primera vez.
"""

import os
import sys
import subprocess
import time
from check_preprocessing import PreprocessingChecker

def run_script(script_path, description):
    """Ejecuta un script Python y maneja errores"""
    print(f"\n{'='*50}")
    print(f"🔄 Ejecutando: {description}")
    print(f"📁 Archivo: {script_path}")
    print(f"{'='*50}")
    
    try:
        # Cambiar al directorio del script para manejar rutas relativas
        script_dir = os.path.dirname(script_path)
        script_name = os.path.basename(script_path)
        
        original_dir = os.getcwd()
        os.chdir(script_dir)
        
        print(f"📂 Ejecutando en directorio: {script_dir}")
        print(f"🐍 Comando: {sys.executable} {script_name}")
        
        # Ejecutar el script mostrando salida en tiempo real
        result = subprocess.run([sys.executable, script_name], 
                              text=True, 
                              timeout=600)  # 10 minutos de timeout
        
        os.chdir(original_dir)
        
        if result.returncode == 0:
            print(f"✅ {description} - Completado exitosamente")
        else:
            print(f"❌ {description} - Error")
            print(f"🔴 Código de error: {result.returncode}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"⏰ {description} - Timeout (más de 10 minutos)")
        os.chdir(original_dir)
        return False
    except Exception as e:
        print(f"💥 {description} - Excepción: {str(e)}")
        os.chdir(original_dir)
        return False
    
    return True

def check_dependencies():
    """Verifica que las dependencias necesarias estén instaladas"""
    print("🔍 Verificando dependencias de Python...")
    
    # Lista de paquetes con sus nombres de importación
    required_packages = [
        ('nltk', 'nltk', 'Natural Language Toolkit'),
        ('numpy', 'numpy', 'Numerical Python'),
        ('scikit-learn', 'sklearn', 'Machine Learning Library'),
        ('sentence-transformers', 'sentence_transformers', 'Sentence Transformers for embeddings'),
        ('json', 'json', 'JSON (built-in)'),
        ('os', 'os', 'Operating System interface (built-in)')
    ]
    
    missing_packages = []
    
    for package_name, import_name, description in required_packages:
        try:
            __import__(import_name)
            print(f"   ✅ {package_name} - {description}")
        except ImportError:
            print(f"   ❌ {package_name} - {description} (NO ENCONTRADO)")
            if package_name not in ['json', 'os']:  # No agregar built-ins a missing
                missing_packages.append(package_name)
    
    if missing_packages:
        print(f"\n🚨 Paquetes faltantes: {', '.join(missing_packages)}")
        print("💡 Instala con el siguiente comando:")
        print(f"   pip install {' '.join(missing_packages)}")
        print("\n🔧 O usa el instalador automático:")
        print(f"   npm run install-python-deps")
        return False
    
    print("✅ Todas las dependencias están instaladas")
    return True

def main():
    """Función principal que ejecuta todos los preprocesadores"""
    print("🚀 Iniciando preprocesamiento del sistema...")
    print("📋 Este proceso puede tomar varios minutos la primera vez")
    
    # Verificar si ya se ejecutó el preprocesamiento
    checker = PreprocessingChecker()
    
    print("\n🔍 Verificando estado actual...")
    if not checker.needs_preprocessing():
        print("✅ El preprocesamiento ya fue ejecutado previamente")
        print("🚀 El sistema está listo para usar")
        
        # Preguntar si se quiere ejecutar de nuevo
        try:
            response = input("\n❓ ¿Quieres ejecutar el preprocesamiento de nuevo? (s/N): ").lower().strip()
            if response not in ['s', 'si', 'sí', 'y', 'yes']:
                print("⏭️ Saltando preprocesamiento")
                return True
        except KeyboardInterrupt:
            print("\n⏹️ Cancelado por el usuario")
            return False
    
    start_time = time.time()
    
    # Verificar dependencias
    if not check_dependencies():
        print("\n❌ Faltan dependencias. Por favor instálalas antes de continuar.")
        return False
    
    # Definir los scripts a ejecutar en orden
    scripts = [
        {
            'path': 'preprocesamiento_texto/preprocesamiento.py',
            'description': 'Preprocesamiento de texto (títulos y descripciones)'
        },
        {
            'path': 'preprocesamiento_texto/embeddings.py',
            'description': 'Generación de embeddings de texto'
        },
        {
            'path': 'preprocesamiento_img/preprocesamiento_img.py',
            'description': 'Preprocesamiento de imágenes (nombres de carpetas)'
        },
        {
            'path': 'preprocesamiento_img/embeddings_img.py',
            'description': 'Generación de embeddings de imágenes'
        },
        {
            'path': 'conexion_img_txt/conexion.py',
            'description': 'Conexión entre imágenes y texto'
        },
        {
            'path': 'conexion_img_txt/embeddings_conexion.py',
            'description': 'Generación de embeddings de conexión multimodal'
        }
    ]
    
    print(f"\n📋 Scripts a ejecutar: {len(scripts)}")
    for i, script in enumerate(scripts, 1):
        print(f"   {i}. {script['description']}")
    print()
    
    # Ejecutar cada script
    success_count = 0
    failed_scripts = []
    
    for i, script in enumerate(scripts, 1):
        script_path = os.path.join(os.path.dirname(__file__), script['path'])
        
        print(f"\n🔢 Script {i}/{len(scripts)}")
        
        if os.path.exists(script_path):
            print(f"✅ Archivo encontrado: {script_path}")
            if run_script(script_path, script['description']):
                success_count += 1
                print(f"🎉 Script {i} completado exitosamente")
            else:
                failed_scripts.append(script['description'])
                print(f"💥 Script {i} falló: {script['description']}")
                print("⚠️ Continuando con el siguiente script...")
        else:
            print(f"❌ Archivo no encontrado: {script_path}")
            failed_scripts.append(f"{script['description']} (archivo no encontrado)")
            print("⚠️ Continuando con el siguiente script...")
        
        print(f"{'─'*50}")  # Separador visual
    
    # Resumen final
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"\n{'='*60}")
    print(f"📊 RESUMEN DE PREPROCESAMIENTO")
    print(f"{'='*60}")
    print(f"✅ Scripts ejecutados exitosamente: {success_count}/{len(scripts)}")
    print(f"⏱️ Tiempo total: {duration:.2f} segundos ({duration/60:.1f} minutos)")
    
    if failed_scripts:
        print(f"\n❌ Scripts que fallaron:")
        for i, failed in enumerate(failed_scripts, 1):
            print(f"   {i}. {failed}")
    
    print(f"\n📋 Lista completa de scripts:")
    for i, script in enumerate(scripts, 1):
        status = "✅" if i <= success_count else "❌"
        print(f"   {status} {i}. {script['description']}")
    
    # Guardar estado del preprocesamiento
    checker.mark_preprocessing_complete(duration, success_count)
    
    if success_count == len(scripts):
        print(f"\n🎉 ¡PREPROCESAMIENTO COMPLETADO EXITOSAMENTE!")
        print(f"🚀 Todos los {len(scripts)} scripts se ejecutaron correctamente")
        print(f"✨ El sistema está listo para usar")
        return True
    else:
        print(f"\n⚠️ PREPROCESAMIENTO PARCIALMENTE COMPLETADO")
        print(f"✅ {success_count} scripts exitosos, ❌ {len(scripts) - success_count} scripts fallaron")
        print(f"💡 Revisa los mensajes de error arriba")
        print(f"🔄 Puedes ejecutar de nuevo para reintentar")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
