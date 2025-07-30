# Importaciones necesarias
import sys
import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Agregar ruta para importar desde conexion_img_txt
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(os.path.join(parent_dir, "conexion_img_txt"))

from embeddings_conexion import dataset_con_embeddings, embeddings_titulos

model = SentenceTransformer('all-MiniLM-L6-v2')

def buscar_por_texto(query_txt: str):
    query_embedding = model.encode(query_txt).astype('float32')
    query_embedding_np = np.array([query_embedding])
    embeddings_np = embeddings_titulos.astype('float32')

    index = faiss.IndexFlatL2(embeddings_np.shape[1])
    index.add(embeddings_np)

    k = 10
    distances, indices = index.search(query_embedding_np, k)

    resultados = []
    for i, idx in enumerate(indices[0]):
        item = dataset_con_embeddings[idx]
        resultados.append({
            "titulo": item["titulo"],
            "descripcion": item.get("descripcion", ""), 
            "archivo": item["archivo_imagen"],
            "distancia": round(float(distances[0][i]), 4)
        })
    return resultados
