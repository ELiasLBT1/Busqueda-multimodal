import sys
import os
from fastapi import FastAPI, Query, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import numpy as np
import torch
from torchvision import models, transforms
from PIL import Image
import json
import io

# Añadir la raíz del proyecto al PYTHONPATH para que 'backend' sea importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Importar función desde tu clase de búsqueda
from backend.busqueda_texto.busqueda_texto import buscar_por_texto
from backend.buscar_img.buscar_por_imagen import buscar_por_imagen_pil

app = FastAPI()

# Configurar CORS para permitir conexión desde tu frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes reemplazar con tu dominio frontend si deseas más seguridad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cargar embeddings y nombres de archivo solo una vez
EMBEDDINGS_FILE = os.path.join(os.path.dirname(__file__), 'img_img/embeddings_dataset.npy')
FILENAMES_FILE = os.path.join(os.path.dirname(__file__), 'img_img/filenames_dataset.npy')
DESCRIPCIONES_FILE = os.path.join(os.path.dirname(__file__), 'data/dataset_autos_descripciones.json')

embeddings = np.load(EMBEDDINGS_FILE)
filenames = np.load(FILENAMES_FILE, allow_pickle=True)

with open(DESCRIPCIONES_FILE, 'r', encoding='utf-8') as f:
    descripciones_data = json.load(f)

desc_por_archivo = {}
for item in descripciones_data:
    if 'filename' in item and 'descripcion' in item:
        desc_por_archivo[item['filename']] = item['descripcion']

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model_cnn = models.resnet50(pretrained=True)
model_cnn = torch.nn.Sequential(*(list(model_cnn.children())[:-1]))
model_cnn.eval()
model_cnn.to(device)

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    ),
])

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

@app.post("/buscar-imagen")
async def buscar_imagen(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        img = Image.open(io.BytesIO(contents)).convert('RGB')
        resultados = buscar_por_imagen_pil(img)
        return {"resultados": resultados}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error procesando imagen: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
