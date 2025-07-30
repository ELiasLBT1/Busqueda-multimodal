import os
import torch
from torchvision import models, transforms
from PIL import Image
import numpy as np

DATASET_DIR = '../data/img'  # Ajusta la ruta aquí
EMBEDDINGS_FILE = 'embeddings_dataset.npy'
FILENAMES_FILE = 'filenames_dataset.npy'

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = models.resnet50(pretrained=True)
model = torch.nn.Sequential(*(list(model.children())[:-1]))  # Quitar capa final
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

embeddings = []
filenames = []

for folder in os.listdir(DATASET_DIR):
    folder_path = os.path.join(DATASET_DIR, folder)
    if not os.path.isdir(folder_path):
        continue
    for fname in os.listdir(folder_path):
        if not fname.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue
        img_path = os.path.join(folder_path, fname)
        try:
            img = Image.open(img_path).convert('RGB')
            img_t = preprocess(img).unsqueeze(0).to(device)
            with torch.no_grad():
                feat = model(img_t).cpu().numpy().flatten()
            embeddings.append(feat)
            filenames.append(img_path)
        except Exception as e:
            print(f"Error procesando {img_path}: {e}")

embeddings = np.array(embeddings)
np.save(EMBEDDINGS_FILE, embeddings)
np.save(FILENAMES_FILE, filenames)
print(f"Guardados {len(embeddings)} embeddings en {EMBEDDINGS_FILE}")