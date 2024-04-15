import requests
from bs4 import BeautifulSoup
import re

def obtener_texto_pagina(url):
    try:
        # Realizar la solicitud GET a la URL
        response = requests.get(url)
        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Obtener el contenido de la página
            contenido = response.text
            return contenido
        else:
            print("Error al obtener la página. Código de estado:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error de conexión:", e)
        return None

def contar_palabras(texto):
    # Utilizar expresión regular para separar palabras
    palabras = re.findall(r'\b\w+\b', texto.lower())
    return len(palabras)

# URL de ejemplo
url_ejemplo = "https://classroom.google.com/c/NjYyNTI0NDIwMTgz/a/Njc0MzU2MzUyODI2/details"
# Obtener el texto de la página
texto_pagina = obtener_texto_pagina(url_ejemplo)

# Contar palabras si se obtuvo correctamente el texto
if texto_pagina:
    # Contar palabras en el texto
    num_palabras = contar_palabras(texto_pagina)
    print("Número de palabras en la página:", num_palabras)
