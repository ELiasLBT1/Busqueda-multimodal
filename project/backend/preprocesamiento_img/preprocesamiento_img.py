import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Descargar recursos necesarios de NLTK
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# Definir la ruta a las carpetas de imágenes
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
img_path = os.path.join(parent_dir, 'data', 'img')

# Extraer los títulos de los nombres de las carpetas
def obtener_titulos_desde_carpetas(ruta):
    """
    Extrae los nombres de las carpetas que contienen las imágenes de los autos
    """
    titulos = []
    try:
        # Listar todas las carpetas en el directorio
        for item in os.listdir(ruta):
            item_path = os.path.join(ruta, item)
            # Verificar que sea una carpeta
            if os.path.isdir(item_path):
                titulos.append(item)
        return titulos
    except FileNotFoundError:
        print(f"Error: No se encontró la ruta {ruta}")
        return []

# Obtener los títulos desde las carpetas
titulos = obtener_titulos_desde_carpetas(img_path)

#convertir a minúsculas
def convertir_minusculas(texto):
    return texto.lower()

# Aplicar la conversión a minúsculas a los títulos
titulos = [convertir_minusculas(titulo) for titulo in titulos]

#tokenizar el texto
def tokenizar_texto(texto):
    return word_tokenize(texto)

# Aplicar la tokenización a los títulos
titulos_tokenizados = [tokenizar_texto(titulo) for titulo in titulos]

#eliminar signos de puntuación y stopwords 
def eliminar_puntuacion_y_stopwords(tokens):
    # Usar stopwords en inglés ya que los nombres de autos están en inglés
    stop_words = set(stopwords.words('english'))
    tokens_sin_puntuacion = [word for word in tokens if word.isalnum()]
    tokens_filtrados = [word for word in tokens_sin_puntuacion if word not in stop_words]
    return tokens_filtrados

# Aplicar la eliminación de puntuación y stopwords a los títulos
titulos_img = [eliminar_puntuacion_y_stopwords(tokens) for tokens in titulos_tokenizados]
