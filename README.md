# 🔍 Búsqueda Multimodal de Vehículos

Sistema avanzado de búsqueda que permite encontrar vehículos usando **texto** o **imágenes**, utilizando técnicas de IA y procesamiento multimodal.

## 🚀 Inicio Rápido

```bash
# 1. Clonar el repositorio
git clone https://github.com/ELiasLBT1/Busqueda-multimodal.git
cd Busqueda-multimodal/project

# 2. Instalación completa automática + inicio del servidor (RECOMENDADO)
npm run setup

# O alternativamente paso a paso:
npm install                    # Dependencias Node.js
npm run install-python-deps   # Dependencias Python
npm start                      # Inicio inteligente

# Solo instalación sin iniciar servidor:
npm run install-only
```

## 📋 Requisitos

- **Node.js** 16+ 
- **Python** 3.8+
- **Dependencias Python**: `pip install nltk numpy scikit-learn sentence-transformers`

## 🛠️ Scripts Disponibles

| Comando | Descripción |
|---------|-------------|
| `npm start` | **Inicio inteligente** - Verifica y ejecuta preprocesamiento automáticamente |
| `npm run setup` | **Instalación completa + inicio del servidor** |
| `npm run install-only` | Solo instalación (sin iniciar servidor) |
| `npm run install-python-deps` | Instala solo dependencias de Python |
| `npm run dev` | Solo servidor de desarrollo (sin preprocesamiento) |
| `npm run check` | Verificar estado del preprocesamiento |
| `npm run preprocess` | Ejecutar solo preprocesamiento |

## ⚡ Primera Ejecución

**El comando `npm run setup` ejecuta automáticamente:**

1. 📦 Instala dependencias Node.js
2. 🐍 Instala dependencias Python 
3. 📝 Procesa texto (títulos y descripciones)
4. 🖼️ Procesa imágenes 
5. 🔗 Genera conexiones multimodales
6. 🚀 **Inicia automáticamente el servidor de desarrollo**

**El proyecto estará disponible en:** `http://localhost:5173`

## 📁 Estructura

```
project/
├── 🎨 Frontend (React + TypeScript + Vite)
│   └── src/
├── 🧠 Backend (Python + IA)
│   ├── preprocesamiento_texto/
│   ├── preprocesamiento_img/
│   └── conexion_img_txt/
└── 📊 Data/
    └── dataset_autos_descripciones.json
```

## 📖 Documentación Completa

Ver [`SETUP.md`](project/SETUP.md) para instrucciones detalladas y solución de problemas.