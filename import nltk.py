import nltk
nltk.download('punkt')

carpeta_nombre="Documento\\"
archivo_nombre="loki.txt"

with open(archivo_nombre,"r") as archivo:
    texto=archivo.read()

tokens=nltk.word_tokenize(texto,"spanish")

for token in tokens:
    print("token")

print('\n\n\n\--------------------------------' )
palabras_total=len(tokens)
print('el total de palabras es de',palabras_total)
print('n\--------------------------------------')