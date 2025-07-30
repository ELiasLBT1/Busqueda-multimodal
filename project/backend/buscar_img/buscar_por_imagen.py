import os
import torch
from torchvision import models, transforms
from PIL import Image
import numpy as np
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EMBEDDINGS_FILE = os.path.join(BASE_DIR, '../img_img/embeddings_dataset.npy')
FILENAMES_FILE = os.path.join(BASE_DIR, '../img_img/filenames_dataset.npy')
DESCRIPCIONES_FILE = os.path.join(BASE_DIR, '../data/dataset_autos_descripciones.json')

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = models.resnet50(pretrained=True)
model = torch.nn.Sequential(*(list(model.children())[:-1]))
model.eval()
model.to(device)

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    ),
])

# Cargar embeddings y nombres de archivo del dataset
embeddings = np.load(EMBEDDINGS_FILE)
filenames = np.load(FILENAMES_FILE, allow_pickle=True)

# Cargar el dataset de descripciones
with open(DESCRIPCIONES_FILE, 'r', encoding='utf-8') as f:
    descripciones_data = json.load(f)

# Crear un diccionario para buscar rápido por filename
desc_por_archivo = {}
for item in descripciones_data:
    if 'filename' in item and 'descripcion' in item:
        desc_por_archivo[item['filename']] = item['descripcion']

def buscar_por_imagen_pil(img: Image.Image):
    img_t = preprocess(img).unsqueeze(0).to(device)
    with torch.no_grad():
        query_emb = model(img_t).cpu().numpy().flatten()
    dists = np.linalg.norm(embeddings - query_emb, axis=1)
    idxs = np.argsort(dists)[:10]
    resultados = []
    for idx in idxs:
        img_path = filenames[idx]
        img_filename = os.path.basename(img_path)
        descripcion = desc_por_archivo.get(img_filename, "Descripción no encontrada")
        resultados.append({
            "titulo": os.path.dirname(img_path).split(os.sep)[-1],
            "descripcion": descripcion,
            "archivo": img_filename,
            "distancia": round(float(dists[idx]), 4)
        })
    return resultados