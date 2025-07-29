import sys
import os
sys.path.append(os.path.abspath("../conexion_img_txt"))
from embeddings_conexion import dataset_con_embeddings, embeddings_titulos
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

query_txt= 'audi'
#hacer embedding de la query  
model = SentenceTransformer('all-MiniLM-L6-v2')
query_embedding = model.encode(query_txt)

# Convertir la query_embedding a un array de numpy
query_embedding_np = np.array([query_embedding]).astype('float32')
# Usar directamente los embeddings ya calculados
embeddings_np = embeddings_titulos.astype('float32')
# Crear el índice de faiss
index = faiss.IndexFlatL2(embeddings_np.shape[1])
# Añadir los embeddings al índice
index.add(embeddings_np)
# Buscar los k vecinos más cercanos
k = 5
distances, indices = index.search(query_embedding_np, k)
# Mostrar los resultados
print("Indices de los k vecinos más cercanos:", indices[0])
print("Distancias:", distances[0])

# Mostrar los títulos correspondientes
print("\nResultados de búsqueda:")
for i, idx in enumerate(indices[0]):
    titulo = dataset_con_embeddings[idx]['titulo']
    archivo = dataset_con_embeddings[idx]['archivo_imagen']
    print(f"{i+1}. {titulo} (archivo: {archivo}) - Distancia: {distances[0][i]:.4f}")