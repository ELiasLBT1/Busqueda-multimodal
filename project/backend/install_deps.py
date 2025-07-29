#!/usr/bin/env python3
"""
Script para instalar automáticamente las dependencias de Python necesarias
"""

import subprocess
import sys
import os

def run_command(command, description=""):
    """Ejecuta un comando y retorna si fue exitoso"""
    try:
        print(f"🔄 {description if description else 'Ejecutando comando'}...")
        print(f"💻 Comando: {command}")
        
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        
        if result.stdout:
            print(f"📝 Salida: {result.stdout}")
            
        print(f"✅ {description if description else 'Comando'} completado exitosamente")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error ejecutando: {command}")
        print(f"🔴 Código de error: {e.returncode}")
        if e.stderr:
            print(f"🔴 Error: {e.stderr}")
        return False
    except Exception as e:
        print(f"💥 Excepción: {str(e)}")
        return False

def check_python():
    """Verifica que Python esté disponible"""
    try:
        result = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
        print(f"✅ Python detectado: {result.stdout.strip()}")
        return True
    except:
        print("❌ Python no encontrado")
        return False

def check_pip():
    """Verifica que pip esté disponible"""
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "--version"], capture_output=True, text=True)
        print(f"✅ pip detectado: {result.stdout.strip()}")
        return True
    except:
        print("❌ pip no encontrado")
        return False

def install_package(package):
    """Instala un paquete específico"""
    print(f"\n📦 Instalando {package}...")
    command = f"{sys.executable} -m pip install {package}"
    return run_command(command, f"Instalación de {package}")

def main():
    """Función principal"""
    print("🐍 INSTALADOR DE DEPENDENCIAS PYTHON")
    print("="*50)
    
    # Verificar Python y pip
    if not check_python():
        print("💡 Instala Python desde https://python.org")
        return False
        
    if not check_pip():
        print("💡 pip debería venir con Python. Reinstala Python.")
        return False
    
    # Lista de paquetes a instalar
    packages = [
        "nltk",
        "numpy", 
        "scikit-learn",
        "sentence-transformers"
    ]
    
    print(f"\n📋 Paquetes a instalar: {len(packages)}")
    for i, pkg in enumerate(packages, 1):
        print(f"   {i}. {pkg}")
    
    # Instalar cada paquete
    successful = 0
    failed = []
    
    for package in packages:
        if install_package(package):
            successful += 1
        else:
            failed.append(package)
    
    # Resumen
    print(f"\n{'='*50}")
    print(f"📊 RESUMEN DE INSTALACIÓN")
    print(f"{'='*50}")
    print(f"✅ Paquetes instalados exitosamente: {successful}/{len(packages)}")
    
    if failed:
        print(f"❌ Paquetes que fallaron:")
        for pkg in failed:
            print(f"   - {pkg}")
        print(f"\n💡 Intenta instalar manualmente:")
        print(f"   pip install {' '.join(failed)}")
        return False
    else:
        print(f"🎉 ¡Todas las dependencias instaladas exitosamente!")
        return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
