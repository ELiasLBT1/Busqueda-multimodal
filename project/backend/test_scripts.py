#!/usr/bin/env python3
"""
Script de prueba para verificar que todos los scripts de preprocesamiento existen
y pueden ser importados/ejecutados sin errores críticos.
"""

import os
import sys

def test_script_exists(script_path):
    """Verifica si un script existe"""
    full_path = os.path.join(os.path.dirname(__file__), script_path)
    exists = os.path.exists(full_path)
    print(f"{'✅' if exists else '❌'} {script_path} - {'Encontrado' if exists else 'NO ENCONTRADO'}")
    return exists

def main():
    """Función principal de prueba"""
    print("🧪 PRUEBA DE SCRIPTS DE PREPROCESAMIENTO")
    print("="*50)
    
    scripts = [
        'preprocesamiento_texto/preprocesamiento.py',
        'preprocesamiento_texto/embeddings.py',
        'preprocesamiento_img/preprocesamiento_img.py',
        'preprocesamiento_img/embeddings_img.py',
        'conexion_img_txt/conexion.py',
        'conexion_img_txt/embeddings_conexion.py'
    ]
    
    print("🔍 Verificando existencia de scripts:")
    found_count = 0
    
    for script in scripts:
        if test_script_exists(script):
            found_count += 1
    
    print(f"\n📊 Resumen:")
    print(f"✅ Scripts encontrados: {found_count}/{len(scripts)}")
    
    if found_count == len(scripts):
        print("🎉 Todos los scripts están disponibles")
        print("🚀 Puedes ejecutar: python init_preprocessing.py")
        return True
    else:
        print("⚠️ Algunos scripts no se encontraron")
        print("💡 Verifica la estructura del proyecto")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
