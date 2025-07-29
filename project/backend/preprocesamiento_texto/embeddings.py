import sys
import os

# Agregar el directorio actual al path para importar el módulo preprocesamiento
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
    # Importar las variables desde el módulo preprocesamiento
    from preprocesamiento import titulos_filtrados, descripciones_filtradas
    print(f"✅ Variables importadas: {len(titulos_filtrados)} títulos, {len(descripciones_filtradas)} descripciones")
except ImportError as e:
    print(f"❌ Error importando variables de preprocesamiento: {e}")
    sys.exit(1)

try:
    # Convertir listas de tokens a strings para el modelo
    titulos_texto = [' '.join(tokens) if isinstance(tokens, list) else str(tokens) for tokens in titulos_filtrados]
    descripciones_texto = [' '.join(tokens) if isinstance(tokens, list) else str(tokens) for tokens in descripciones_filtradas]
    
    print("🔄 Generando embeddings de títulos...")
    titulos_embeddings = model.encode(titulos_texto)
    print(f"✅ Embeddings de títulos generados: {titulos_embeddings.shape}")
    
    print("🔄 Generando embeddings de descripciones...")
    descripciones_embeddings = model.encode(descripciones_texto)
    print(f"✅ Embeddings de descripciones generados: {descripciones_embeddings.shape}")
    
    print("🎉 Generación de embeddings de texto completada exitosamente")
    
except Exception as e:
    print(f"❌ Error generando embeddings: {e}")
    sys.exit(1)
