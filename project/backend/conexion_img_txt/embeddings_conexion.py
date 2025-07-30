import sys
import os

try:
    from sentence_transformers import SentenceTransformer
    print("✅ SentenceTransformer importado correctamente")
except ImportError as e:
    print(f"❌ Error importando SentenceTransformer: {e}")
    print("💡 Instala con: pip install sentence-transformers")
    sys.exit(1)

# Añadir ruta para importar conexion
sys.path.append(os.path.abspath("."))

try:
    # Importar datos conectados
    from conexion import dataset_conexion
    print(f"✅ Dataset de conexión importado: {len(dataset_conexion)} elementos")
except ImportError as e:
    print(f"❌ Error importando dataset_conexion: {e}")
    sys.exit(1)

try:
    # Inicializar modelo de embeddings para texto
    modelo_texto = SentenceTransformer('all-MiniLM-L6-v2')
    print("✅ Modelo de embeddings de conexión cargado")
except Exception as e:
    print(f"❌ Error cargando modelo: {e}")
    sys.exit(1)

try:
    # Preparar textos para embeddings (solo títulos)
    textos_titulos = []
    
    for registro in dataset_conexion:
        titulo = registro['titulo']
        textos_titulos.append(titulo)
    
    print(f"🔄 Generando embeddings para {len(textos_titulos)} títulos conectados...")
    
    # Generar embeddings solo de títulos
    embeddings_titulos = modelo_texto.encode(textos_titulos)
    print(f"✅ Embeddings generados: {embeddings_titulos.shape}")
    
    # Crear dataset con embeddings
    dataset_con_embeddings = []
    for i, registro in enumerate(dataset_conexion):
        dataset_con_embeddings.append({
            'titulo': registro['titulo'],
            'descripcion': registro['descripcion'],  # Agregar descripción
            'archivo_imagen': registro['archivo_imagen'],
            'tokens_procesados': registro['tokens_procesados'],
            'indice_texto': registro['indice_texto'],
            'indice_img': registro['indice_img'],
            'embedding_titulo': embeddings_titulos[i]
        })
    
    print(f"✅ Dataset con embeddings creado: {len(dataset_con_embeddings)} registros")
    print("🎉 Generación de embeddings de conexión completada exitosamente")
    
except Exception as e:
    print(f"❌ Error generando embeddings de conexión: {e}")
    sys.exit(1)
