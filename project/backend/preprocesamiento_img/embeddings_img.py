import sys
import os

# Agregar el directorio actual al path para importar el módulo preprocesamiento_img
sys.path.append(os.path.dirname(__file__))

try:
    from sentence_transformers import SentenceTransformer
    print("✅ SentenceTransformer importado correctamente")
except ImportError as e:
    print(f"❌ Error importando SentenceTransformer: {e}")
    print("💡 Instala con: pip install sentence-transformers")
    sys.exit(1)

try:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("✅ Modelo SentenceTransformer cargado")
except Exception as e:
    print(f"❌ Error cargando modelo: {e}")
    sys.exit(1)

try:
    # Importar las variables desde el módulo preprocesamiento_img
    from preprocesamiento_img import titulos_img
    print(f"✅ Variables importadas: {len(titulos_img)} títulos de imágenes")
except ImportError as e:
    print(f"❌ Error importando variables de preprocesamiento_img: {e}")
    sys.exit(1)

try:
    # Convertir listas de tokens a strings para el modelo
    titulos_texto = [' '.join(tokens) if isinstance(tokens, list) else str(tokens) for tokens in titulos_img]
    
    print("🔄 Generando embeddings de títulos de imágenes...")
    titulos_embeddings = model.encode(titulos_texto)
    print(f"✅ Embeddings de títulos generados: {titulos_embeddings.shape}")
    
    print("🎉 Generación de embeddings de imágenes completada exitosamente")
    
except Exception as e:
    print(f"❌ Error generando embeddings: {e}")
    sys.exit(1)
