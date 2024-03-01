#clase 09/02/2024

print("Universidad de Colima")
print("Ingeniería en computación Inteligente")
print("Procesamiento de Lenguaje Natural")

nombre = "Andrea Ketzabel Madrigal Rodriguez"

print("Hola", nombre)

edad= input("Escribe tu edad:")
print(nombre, "tiene la edad de", edad," años")
print("Operacion1: ",4*5-6)

x=4+7
y=x-2
z=x+y

print("x =",x)
print("y =",y)
print("z =",z)



archivo_abierto= open("C:\\Users\\arodr\\OneDrive\\Documentos\\optativa\\clase2.txt\\","w")
archivo_abierto.write("Esto se escribe en el archivo\n")
archivo_abierto.write("Esto también\n")
archivo_abierto.write("Mira, puedo escribir \"cosillas\"\n")
archivo_abierto.write("Gracias a la diagonal invertida \n")

archivo_abierto.close()

archivo_abierto= open("C:\\Users\\arodr\\OneDrive\\Documentos\\optativa\\clase2\\.txt")
texto=archivo_abierto.read()
print(texto)
archivo_abierto.close()