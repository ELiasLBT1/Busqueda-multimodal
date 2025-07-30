# 🔍 Búsqueda Multimodal de Vehículos

Sistema avanzado1. **📦 Ejecutar sistema completo:**
   ```bash
   # Terminal 1: Backend API 
   uvicorn backend.api_server:app --reload
   
   # Terminal 2: Frontend (instala dependencias, preprocesa y ejecuta)
   npm run setup
   ```ueda que permite encontrar vehículos usando **texto** o **imágenes**, utilizando técnicas de IA y procesamiento multimodal.

## 🚀 Inicio Rápido

### Opción 1: Instalación completa automática (RECOMENDADO)
```bash
# 1. Clonar el repositorio
git clone https://github.com/ELiasLBT1/Busqueda-multimodal.git
cd Busqueda-multimodal/project

# 2. Instalación completa + preprocesamiento
npm run setup

# 3. Inicializar el backend
uvicorn backend.api_server:app --reload
```

### Opción 2: Ejecución manual (después de la instalación)
```bash
# Terminal 1: Backend API (puerto 8000)
cd project
uvicorn backend.api_server:app --reload

# Terminal 2: Frontend (puerto 5173/5174)
cd project  
npm run dev
```

### Opción 3: Solo preprocesamiento (sin iniciar servidores)
```bash
npm run install-only
```

## 📋 Requisitos

- **Node.js** 16+ 
- **Python** 3.8+
- **Dependencias Python**: `pip install nltk numpy scikit-learn sentence-transformers fastapi uvicorn`

## 🛠️ Scripts Disponibles

| Comando | Descripción |
|---------|-------------|
| `npm run setup` | **Instalación completa + preprocesamiento + inicializar frontend** |
| `npm start` | **Inicio inteligente** - Verifica y ejecuta preprocesamiento automáticamente |
| `npm run install-only` | Solo instalación y preprocesamiento (sin iniciar servidores) |
| `npm run install-python-deps` | Instala solo dependencias de Python |
| `npm run dev` | Solo servidor frontend de desarrollo (puerto 5173/5174) |
| `npm run check` | Verificar estado del preprocesamiento |
| `npm run preprocess` | Ejecutar solo preprocesamiento |

## ⚡ Ejecución del Sistema Completo

**Para usar la búsqueda multimodal completa necesitas ejecutar AMBOS servidores:**

1. **� Ejecutar sistema completo:**
   ```bash
   # Terminal 1: Backend API 
   uvicorn backend.api_server:app --reload
   
   # Terminal 2: Frontend
   npm run setup
   ```

2. **🌐 Acceder a la aplicación:**
   - **Frontend:** `http://localhost:5173` o `http://localhost:5174`
   - **API Backend:** `http://localhost:8000`

## 🔄 Flujo del Sistema

1. **Frontend (React)** → Interfaz de usuario para búsquedas
2. **Backend API (FastAPI)** → Procesamiento de búsquedas con IA
3. **Dataset real** → 190 vehículos con imágenes y descripciones
4. **Búsqueda semántica** → Similarity search con sentence-transformers + faiss

## 📁 Estructura

```
project/
├── 🎨 Frontend (React + TypeScript + Vite)
│   └── src/
├── 🧠 Backend API (FastAPI + Python)
│   ├── api_server.py              # Servidor principal
│   ├── preprocesamiento_texto/    # Procesamiento de descripciones
│   ├── preprocesamiento_img/      # Procesamiento de imágenes  
│   ├── conexion_img_txt/          # Conexión multimodal
│   └── busqueda_texto/            # Lógica de búsqueda
└── 📊 Data/
    ├── dataset_autos_descripciones.json  # Dataset principal
    └── img/                              # Imágenes de vehículos
```

## 🔍 Funcionalidades

- ✅ **Búsqueda por texto**: Encuentra vehículos usando descripciones naturales
- ✅ **Imágenes reales**: Visualiza los vehículos del dataset
- ✅ **Descripciones reales**: Información detallada de cada vehículo  
- ✅ **Búsqueda semántica**: Similarity search con IA (sentence-transformers + faiss)
- ✅ **Dataset real**: 190 vehículos procesados y conectados
- ✅ **API completa**: Endpoints para búsqueda y servir imágenes

## 📖 Documentación Completa

Ver [`SETUP.md`](project/SETUP.md) para instrucciones detalladas y solución de problemas.