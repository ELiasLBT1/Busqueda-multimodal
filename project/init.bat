@echo off
REM Script de inicialización para Windows
REM Ejecuta todos los preprocesadores necesarios

echo.
echo ===============================================
echo 🚀 INICIALIZACION DEL SISTEMA DE BUSQUEDA
echo ===============================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python no está instalado o no está en el PATH
    echo 💡 Por favor instala Python desde https://python.org
    pause
    exit /b 1
)

echo ✅ Python detectado
python --version

REM Cambiar al directorio backend
cd /d "%~dp0backend"

echo.
echo 📁 Directorio actual: %cd%
echo.

REM Instalar dependencias de Python
echo 🐍 Instalando dependencias de Python...
python install_deps.py

if errorlevel 1 (
    echo.
    echo ❌ Error instalando dependencias de Python
    echo 💡 Intenta ejecutar manualmente: pip install nltk numpy scikit-learn sentence-transformers
    pause
    exit /b 1
)

echo.
echo ✅ Dependencias de Python instaladas
echo.

REM Ejecutar el script de inicialización
echo 🔄 Ejecutando preprocesamiento...
python init_preprocessing.py

if errorlevel 1 (
    echo.
    echo ❌ Error durante el preprocesamiento
    echo 💡 Revisa los mensajes arriba para más detalles
    pause
    exit /b 1
) else (
    echo.
    echo ✅ Preprocesamiento completado exitosamente
    echo 🎉 El sistema está listo para usar
)

echo.
echo 🚀 Ahora puedes ejecutar: npm run dev
pause
