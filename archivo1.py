archivo_nombre="documento1.txt"
with open(archivo_nombre, "r") as archivo:
    lineas_lista=archivo.readlines()

num_linea=1
for linea in lineas_lista:
    if linea.strip()=="":
        continue
    print("linea",num_linea,":",linea)
    num_linea=num_linea+1

print("fin del archivo")