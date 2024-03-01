carpeta_nombre= "C:/Users/arodr/OneDrive/Documentos/Escritorio/documentos/"
archivo_nombre="loki.txt" 

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read() 
palabras_lista=texto.split() 
print("palabras separadas: \n", palabras_lista)
palabras_lista.sort() 
print("palabras ordenadas: \n")

for palabra in palabras_lista: 
    print(palabra)  







