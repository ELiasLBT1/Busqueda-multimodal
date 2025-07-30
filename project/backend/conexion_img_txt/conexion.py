import sys
import os

# Añadir rutas de los paquetes locales
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(os.path.join(parent_dir, "preprocesamiento_texto"))
sys.path.append(os.path.join(parent_dir, "preprocesamiento_img"))

try:
    import preprocesamiento
    print("✅ Módulo preprocesamiento (texto) importado")
except ImportError as e:
    print(f"❌ Error importando preprocesamiento (texto): {e}")
    sys.exit(1)

try:
    import preprocesamiento_img
    print("✅ Módulo preprocesamiento_img importado")
except ImportError as e:
    print(f"❌ Error importando preprocesamiento_img: {e}")
    sys.exit(1)

# Importar variables del preprocesamiento de texto
try:
    titulos_texto = preprocesamiento.titulos_filtrados
    nombres_archivos = preprocesamiento.nombres_archivos
    descripciones_originales = preprocesamiento.descripciones  # Descripción original sin procesar
    print(f"✅ Variables de texto importadas: {len(titulos_texto)} títulos")
except AttributeError as e:
    print(f"❌ Error accediendo a variables de preprocesamiento: {e}")
    sys.exit(1)

try:
    titulos_img = preprocesamiento_img.titulos_img
    titulos_originales_img = preprocesamiento_img.titulos
    print(f"✅ Variables de imágenes importadas: {len(titulos_img)} títulos")
except AttributeError as e:
    print(f"❌ Error accediendo a variables de preprocesamiento_img: {e}")
    sys.exit(1)

# Función para normalizar títulos para comparación
def normalizar_titulo(titulo_tokens):
    """Convierte lista de tokens a string normalizado"""
    return ' '.join(sorted(titulo_tokens)).lower()

# Crear diccionarios para mapear títulos
titulos_texto_map = {}
for i, titulo in enumerate(titulos_texto):
    titulo_norm = normalizar_titulo(titulo)
    titulos_texto_map[titulo_norm] = {
        'indice': i, 
        'titulo_original': preprocesamiento.titulos[i],
        'descripcion_original': descripciones_originales[i],  # Agregar descripción
        'tokens': titulo,
        'archivo': nombres_archivos[i]
    }

titulos_img_map = {}
for i, titulo in enumerate(titulos_img):
    titulo_norm = normalizar_titulo(titulo)
    titulos_img_map[titulo_norm] = {
        'indice': i,
        'titulo_original': titulos_originales_img[i], 
        'tokens': titulo
    }

# Encontrar coincidencias y crear dataset final
print("🔄 Creando conexiones entre imágenes y texto...")
dataset_conexion = []
for titulo_norm, datos_texto in titulos_texto_map.items():
    if titulo_norm in titulos_img_map:
        datos_img = titulos_img_map[titulo_norm]
        dataset_conexion.append({
            'titulo': datos_texto['titulo_original'],
            'descripcion': datos_texto['descripcion_original'],  # Agregar descripción
            'archivo_imagen': datos_texto['archivo'],
            'tokens_procesados': datos_texto['tokens'],
            'indice_texto': datos_texto['indice'],
            'indice_img': datos_img['indice']
        })

print(f"✅ Conexiones creadas: {len(dataset_conexion)} coincidencias encontradas")
print(f"📊 Total títulos texto: {len(titulos_texto_map)}")
print(f"📊 Total títulos imagen: {len(titulos_img_map)}")
print("🎉 Conexión img-txt completada exitosamente")
