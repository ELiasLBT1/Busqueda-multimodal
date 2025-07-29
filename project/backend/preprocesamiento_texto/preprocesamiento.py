import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import json

file_path = '../data/dataset_autos_descripciones.json'

# Leer el archivo JSON que contiene un array
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

#extraer el filename de los autos
nombres_archivos = [item['filename'] for item in data if 'filename' in item]

#Extraer los titulos de los autos
titulos = [item['titulo'] for item in data if 'titulo' in item]

#extraer las descripciones de los autos
descripciones = [item['descripcion'] for item in data if 'descripcion' in item]

#convertir a minúsculas
def convertir_minusculas(texto):
    return texto.lower()

# Aplicar la conversión a minúsculas a todas las listas
titulos = [convertir_minusculas(titulo) for titulo in titulos]
descripciones = [convertir_minusculas(descripcion) for descripcion in descripciones]


#tokenizar el texto
def tokenizar_texto(texto):
    return word_tokenize(texto)

# Aplicar la tokenización a todas las listas
titulos_tokenizados = [tokenizar_texto(titulo) for titulo in titulos]
descripciones_tokenizadas = [tokenizar_texto(descripcion) for descripcion in descripciones]


#eliminar signos de puntuación y stopwords 
def eliminar_puntuacion_y_stopwords(tokens):
    stop_words = set(stopwords.words('spanish'))
    tokens_sin_puntuacion = [word for word in tokens if word.isalnum()]
    tokens_filtrados = [word for word in tokens_sin_puntuacion if word not in stop_words]
    return tokens_filtrados

# Aplicar la eliminación de puntuación y stopwords a todas las listas
titulos_filtrados = [eliminar_puntuacion_y_stopwords(tokens) for tokens in titulos_tokenizados]
descripciones_filtradas = [eliminar_puntuacion_y_stopwords(tokens) for tokens in descripciones_tokenizadas]
