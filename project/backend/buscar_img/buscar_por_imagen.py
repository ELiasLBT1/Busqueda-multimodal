import os
import torch
from torchvision import models, transforms
from PIL import Image
import numpy as np
import json

EMBEDDINGS_FILE = '../img_img/embeddings_dataset.npy'
FILENAMES_FILE = '../img_img/filenames_dataset.npy'
QUERY_DIR = '.'  # Carpeta buscar_img
DESCRIPCIONES_FILE = '../data/dataset_autos_descripciones.json'

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
    # Algunos items pueden no tener filename
    if 'filename' in item and 'descripcion' in item:
        desc_por_archivo[item['filename']] = item['descripcion']

# Procesar cada imagen de consulta en buscar_img
for fname in os.listdir(QUERY_DIR):
    if not fname.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue
    img_path = os.path.join(QUERY_DIR, fname)
    img = Image.open(img_path).convert('RGB')
    img_t = preprocess(img).unsqueeze(0).to(device)
    with torch.no_grad():
        query_emb = model(img_t).cpu().numpy().flatten()
    # Calcular distancias (L2)
    dists = np.linalg.norm(embeddings - query_emb, axis=1)
    idxs = np.argsort(dists)[:10]  # Top 5
    print(f"\nResultados para {fname}:")
    for i, idx in enumerate(idxs):
        img_path = filenames[idx]
        img_filename = os.path.basename(img_path)
        descripcion = desc_por_archivo.get(img_filename, "Descripción no encontrada")
        print(f"{i+1}. {img_path} (distancia: {dists[idx]:.4f})")
        print(f"   Descripción: {descripcion}")
        # Mostrar la imagen encontrada
        img_result = Image.open(img_path)
        img_result.show(title=f"Resultado {i+1}")