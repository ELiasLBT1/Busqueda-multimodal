#!/usr/bin/env python3
"""
Script inteligente de desarrollo que verifica automáticamente
si necesita ejecutar el preprocesamiento antes de iniciar
"""

import sys
import os
import subprocess
from check_preprocessing import PreprocessingChecker

def run_command(command, description=""):
    """Ejecuta un comando y retorna si fue exitoso"""
    try:
        print(f"🔄 {description if description else 'Ejecutando comando'}...")
        result = subprocess.run(command, shell=True, check=True)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"❌ Error ejecutando: {command}")
        print(f"🔴 Código de error: {e.returncode}")
        return False
    except Exception as e:
        print(f"💥 Excepción: {str(e)}")
        return False

def main():
    """Función principal"""
    print("🚀 INICIADOR INTELIGENTE DE DESARROLLO")
    print("="*50)
    
    # Cambiar al directorio del proyecto si es necesario
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    os.chdir(project_dir)
    
    print(f"📁 Directorio del proyecto: {project_dir}")
    
    # Verificar si Node.js está disponible
    try:
        subprocess.run(["npm", "--version"], check=True, capture_output=True)
        print("✅ npm detectado")
    except:
        print("❌ npm no encontrado. Instala Node.js primero.")
        return False
    
    # Verificar estado del preprocesamiento
    checker = PreprocessingChecker(backend_dir="backend")
    
    print("\n🔍 Verificando preprocesamiento...")
    needs_prep = checker.needs_preprocessing()
    
    if needs_prep:
        print("\n🚨 Se requiere preprocesamiento")
        print("🔄 Ejecutando preprocesamiento automáticamente...")
        
        if not run_command("npm run preprocess", "Ejecutando preprocesamiento"):
            print("❌ Fallo el preprocesamiento")
            return False
    else:
        print("\n✅ Preprocesamiento ya completado")
    
    # Iniciar el servidor de desarrollo
    print("\n🚀 Iniciando servidor de desarrollo...")
    print("🌐 El servidor se abrirá en http://localhost:5173")
    print("⏹️ Presiona Ctrl+C para detener")
    
    return run_command("npm run dev", "Iniciando servidor Vite")

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n⏹️ Detenido por el usuario")
        sys.exit(0)
