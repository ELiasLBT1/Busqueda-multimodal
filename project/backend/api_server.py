import sys
import os
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

# Añadir la raíz del proyecto al PYTHONPATH para que 'project' sea importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Importar función desde tu clase de búsqueda
from project.backend.busqueda_texto.busqueda_texto import buscar_por_texto

app = FastAPI()

# Configurar CORS para permitir conexión desde tu frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes reemplazar con tu dominio frontend si deseas más seguridad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/buscar")
def buscar(query: str = Query(..., min_length=1)):
    """
    Endpoint GET para realizar búsqueda semántica de autos.
    """
    resultados = buscar_por_texto(query)
    return {"resultados": resultados}

@app.get("/imagen/{nombre_archivo}")
def servir_imagen(nombre_archivo: str):
    """
    Endpoint para servir imágenes desde el directorio de datos.
    """
    try:
        # Construir la ruta base al directorio de imágenes
        current_dir = os.path.dirname(os.path.abspath(__file__))
        img_base_path = os.path.join(current_dir, 'data', 'img')
        
        # Buscar la imagen en los subdirectorios
        for root, dirs, files in os.walk(img_base_path):
            if nombre_archivo in files:
                file_path = os.path.join(root, nombre_archivo)
                return FileResponse(file_path)
        
        raise HTTPException(status_code=404, detail="Imagen no encontrada")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al servir imagen: {str(e)}")
