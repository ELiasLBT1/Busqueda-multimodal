# 🚀 Sistema de Búsqueda Multimodal

Este proyecto implementa un sistema de búsqueda multimodal que permite buscar vehículos usando texto o imágenes.

## 📋 Requisitos Previos

- **Node.js** (versión 16 o superior)
- **Python** (versión 3.8 o superior)
- **npm** o **yarn**

### Dependencias Python requeridas:
```bash
pip install nltk numpy scikit-learn sentence-transformers
```

## 🚀 Instalación y Primera Ejecución

### Opción 1: Usando NPM (Recomendado)

```bash
# Instalación completa automática + inicio del servidor (TODO EN UNO)
npm run setup

# O paso a paso:
npm install                   # 1. Dependencias Node.js
npm run install-python-deps  # 2. Dependencias Python
npm run preprocess           # 3. Preprocesamiento
npm run dev                  # 4. Servidor de desarrollo

# Otras opciones útiles:
npm run install-only         # Solo instalación (sin servidor)
npm run start               # Inicio inteligente (verifica automáticamente)
```

### Opción 2: Usando script de Windows

#### Usando Batch (cmd):
```cmd
# Ejecutar el archivo init.bat
init.bat
```

### Opción 3: Ejecución Manual

```bash
# 1. Instalar dependencias del frontend
npm install

# 2. Instalar dependencias Python
npm run install-python-deps

# 3. Ejecutar preprocesamiento (requerido la primera vez)
python backend/init_preprocessing.py

# 4. Iniciar servidor de desarrollo
npm run dev
```

## 💡 ¿Qué comando usar?

- **🚀 `npm run setup`** - **RECOMENDADO para primera vez**: Instala todo y abre automáticamente el proyecto en el navegador
- **🔧 `npm run install-only`** - Solo instalación sin abrir el navegador (útil para CI/CD)
- **⚡ `npm start`** - Para desarrollo diario: verifica automáticamente si necesita preprocesamiento
- **🖥️ `npm run dev`** - Solo servidor (si ya tienes todo instalado y procesado)

# 3. Iniciar el servidor de desarrollo
npm run dev
```

## 🔧 Qué hace el Preprocesamiento

### 🚀 Cuando ejecutas `npm run setup`:

```
1. 📦 npm install                    ← Instala dependencias Node.js
2. 🐍 npm run install-python-deps   ← Instala Python: nltk, numpy, etc.
3. 🔄 npm run preprocess            ← Ejecuta 6 scripts automáticamente:
   ├── 📝 preprocesamiento_texto/preprocesamiento.py
   ├── 📝 preprocesamiento_texto/embeddings.py
   ├── 🖼️ preprocesamiento_img/preprocesamiento_img.py
   ├── 🖼️ preprocesamiento_img/embeddings_img.py
   ├── 🔗 conexion_img_txt/conexion.py
   └── 🔗 conexion_img_txt/embeddings_conexion.py
4. 🌐 npm run dev                   ← Inicia servidor automáticamente
5. 🎉 Se abre http://localhost:5173 ← ¡Listo para usar!
```

### 📋 Scripts ejecutados automáticamente (en orden):

1. **📝 Preprocesamiento de Texto** 
   - `preprocesamiento_texto/preprocesamiento.py` - Procesa títulos y descripciones
   - `preprocesamiento_texto/embeddings.py` - Genera embeddings de texto

2. **🖼️ Preprocesamiento de Imágenes**
   - `preprocesamiento_img/preprocesamiento_img.py` - Procesa nombres de carpetas
   - `preprocesamiento_img/embeddings_img.py` - Genera embeddings de imágenes

3. **🔗 Conexión Imagen-Texto**
   - `conexion_img_txt/conexion.py` - Vincula imágenes con descripciones
   - `conexion_img_txt/embeddings_conexion.py` - Genera embeddings de conexión multimodal

**Total: 6 scripts ejecutados automáticamente** 🚀

## 📊 Estados del Sistema

Durante la inicialización verás mensajes como:

- ✅ **Proceso completado exitosamente**
- ❌ **Error en el proceso**
- 🔄 **Proceso en ejecución**
- ⏰ **Timeout (más de 5 minutos)**

## 🛠️ Scripts Disponibles

| Script | Descripción |
|--------|-------------|
| `npm run setup` | **🚀 Instalación completa + inicio automático del servidor** |
| `npm run install-only` | Instalación completa (sin iniciar servidor) |
| `npm run start` | Inicio inteligente (verifica automáticamente) |
| `npm run dev` | Solo servidor de desarrollo |
| `npm run install-python-deps` | Instala solo dependencias de Python |
| `npm run preprocess` | Ejecuta solo el preprocesamiento |
| `npm run init` | Preprocesamiento + desarrollo |
| `npm run check` | Verificar estado del preprocesamiento |
| `npm run build` | Construye la aplicación para producción |
| `npm run preview` | Vista previa de la versión de producción |

## ⚠️ Solución de Problemas

### Error: "Python no está instalado"
- Instala Python desde [python.org](https://python.org)
- Asegúrate de que esté en el PATH del sistema

### Error: "Paquetes faltantes" 
```bash
# Instalar automáticamente
npm run install-python-deps

# O manualmente
pip install nltk numpy scikit-learn sentence-transformers
```

### Error: "sentence-transformers NO ENCONTRADO" pero está instalado
- Es un problema de verificación, el paquete está instalado correctamente
- Ejecuta: `python -c "import sentence_transformers; print('OK')"`
- Si funciona, continúa con el preprocesamiento

### Error: "Archivo no encontrado"
- Verifica que estés en el directorio correcto del proyecto
- Asegúrate de que la estructura de carpetas esté intacta

### El preprocesamiento es muy lento
- Es normal la primera vez (puede tomar varios minutos)
- Los procesos subsecuentes serán más rápidos

## 📁 Estructura del Proyecto

```
project/
├── backend/
│   ├── init_preprocessing.py      # Script principal de inicialización
│   ├── preprocesamiento_texto/    # Procesamiento de texto
│   ├── preprocesamiento_img/      # Procesamiento de imágenes
│   ├── conexion_img_txt/          # Conexión multimodal
│   └── data/                      # Dataset y archivos de datos
├── src/                          # Código fuente del frontend
├── init.bat                      # Script de inicialización (Windows)
├── init.ps1                      # Script de inicialización (PowerShell)
└── package.json                  # Configuración del proyecto
```

## 🤝 Desarrollo

Una vez completada la inicialización, el proyecto estará listo para desarrollo normal:

```bash
npm run dev  # Para desarrollo diario (no necesita preprocesamiento)
```

El preprocesamiento solo necesita ejecutarse:
- La primera vez que clonas el proyecto
- Cuando se actualiza el dataset
- Cuando se modifican los scripts de preprocesamiento
