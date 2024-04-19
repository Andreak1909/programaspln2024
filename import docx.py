import docx
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

# Función para contar palabras y líneas en el texto
def contar_palabras_lineas(texto):
    palabras = texto.split()
    num_palabras = len(palabras)
    num_lineas = texto.count('\n') + 1
    return num_palabras, num_lineas

# Función para contar la frecuencia de una palabra específica
def contar_palabra(texto, palabra):
    tokens = word_tokenize(texto)
    frecuencia = Counter(tokens)
    return frecuencia[palabra]

# Leer el documento de Word
documento = docx.Document("documento.docx")
texto_pagina = ""
for parrafo in documento.paragraphs:
    texto_pagina += parrafo.text + "\n"

# Guardar el texto extraído en un archivo de texto
with open("texto_pagina.txt", "w", encoding="utf-8") as archivo:
    archivo.write(texto_pagina)

# Contar palabras y líneas
num_palabras, num_lineas = contar_palabras_lineas(texto_pagina)
print("Número de palabras en el documento:", num_palabras)
print("Número de líneas de texto en el documento:", num_lineas)

# Contar la frecuencia de una palabra específica
palabra_busqueda = "Python"
frecuencia_palabra = contar_palabra(texto_pagina, palabra_busqueda
