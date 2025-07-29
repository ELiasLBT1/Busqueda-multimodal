# Script de inicialización para PowerShell
# Ejecuta todos los preprocesadores necesarios

Write-Host ""
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "🚀 INICIALIZACION DEL SISTEMA DE BUSQUEDA" -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si Python está instalado
try {
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ Python detectado: $pythonVersion" -ForegroundColor Green
    } else {
        throw "Python no encontrado"
    }
} catch {
    Write-Host "❌ Python no está instalado o no está en el PATH" -ForegroundColor Red
    Write-Host "💡 Por favor instala Python desde https://python.org" -ForegroundColor Yellow
    Read-Host "Presiona Enter para salir"
    exit 1
}

# Cambiar al directorio backend
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$backendDir = Join-Path $scriptDir "backend"

Write-Host ""
Write-Host "📁 Cambiando a directorio: $backendDir" -ForegroundColor Blue

if (Test-Path $backendDir) {
    Set-Location $backendDir
    Write-Host "✅ Directorio encontrado" -ForegroundColor Green
} else {
    Write-Host "❌ Directorio backend no encontrado" -ForegroundColor Red
    Read-Host "Presiona Enter para salir"
    exit 1
}

Write-Host ""
Write-Host "🔄 Ejecutando preprocesamiento..." -ForegroundColor Yellow
Write-Host ""

# Ejecutar el script de inicialización
try {
    python init_preprocessing.py
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host ""
        Write-Host "✅ Preprocesamiento completado exitosamente" -ForegroundColor Green
        Write-Host "🎉 El sistema está listo para usar" -ForegroundColor Green
        Write-Host ""
        Write-Host "🚀 Ahora puedes ejecutar: npm run dev" -ForegroundColor Cyan
    } else {
        throw "Error en preprocesamiento"
    }
} catch {
    Write-Host ""
    Write-Host "❌ Error durante el preprocesamiento" -ForegroundColor Red
    Write-Host "💡 Revisa los mensajes arriba para más detalles" -ForegroundColor Yellow
}

Write-Host ""
Read-Host "Presiona Enter para continuar"
