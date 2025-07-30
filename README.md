# 🔍 Búsqueda Multimodal de Vehículos

Sistema avanzado de búsqueda que permite encontrar vehículos usando **texto** o **imágenes**, utilizando técnicas de IA y procesamiento multimodal.

## 🚀 Inicio Rápido

### Opción 1: TODO AUTOMÁTICO - Un solo comando (RECOMENDADO) 🚀
```bash
# 1. Clonar el repositorio
git clone https://github.com/ELiasLBT1/Busqueda-multimodal.git
cd Busqueda-multimodal/project

# 2. Instalación + preprocesamiento + arranque completo automático
npm run setup-and-start
```
**¡Esto arranca automáticamente ambos servidores (backend + frontend)!**

### Opción 2: Instalación y ejecución manual (control total) ⚙️
```bash
# 1. Solo instalación y preprocesamiento
npm run setup

# 2. Luego ejecutar manualmente ambos servidores:
# Terminal 1: Backend API (puerto 8000)
uvicorn backend.api_server:app --reload

# Terminal 2: Frontend (puerto 5173/5174)  
npm run dev
```

### Opción 3: Solo preprocesamiento (sin arrancar servidores) 📦
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
| `npm run setup-and-start` | **🚀 TODO AUTOMÁTICO** - Instalación + preprocesamiento + arranca ambos servidores |
| `npm run setup` | **📦 Solo instalación** - Instala dependencias + preprocesamiento (sin arrancar servidores) |
| `npm run full-stack` | **▶️ Arrancar ambos servidores** - Backend API + Frontend (después de setup) |
| `npm start` | **Inicio inteligente** - Verifica y ejecuta preprocesamiento automáticamente |
| `npm run install-only` | Solo instalación y preprocesamiento (sin iniciar servidores) |
| `npm run install-python-deps` | Instala solo dependencias de Python |
| `npm run dev` | Solo servidor frontend de desarrollo (puerto 5173/5174) |
| `npm run check` | Verificar estado del preprocesamiento |
| `npm run preprocess` | Ejecutar solo preprocesamiento |

## ⚡ Ejecución del Sistema Completo

**Para usar la búsqueda multimodal completa necesitas ejecutar AMBOS servidores:**

1. **📦 Instalación (solo una vez):**
   ```bash
   npm run setup  # Instala todo y ejecuta preprocesamiento
   ```

2. **� Ejecutar sistema completo:**
   ```bash
   # Terminal 1: Backend API 
   uvicorn backend.api_server:app --reload
   
   # Terminal 2: Frontend
   npm run dev
   ```

3. **🌐 Acceder a la aplicación:**
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