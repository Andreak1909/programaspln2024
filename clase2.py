c= "C:\\Users\\arodr\\OneDrive\\Documentos\\optativa\\"
e= "clase2.txt"
s="clas2.txt"

e2=open(c+e,"r")

#print(e2.read())

s2=open(c+s,"w")
t=e2.read()
t2=t
s2.write(t2)

e2.close()
s2.close()

#_Forma 1____
#s3=open(c+s,"r")
#print(s3.read())
#s3.close()

#_Forma 2____

with open(c+s,"r") as archivo:
    texto=archivo.read()
print(texto)
palabra=input("Escribe la palabra a buscar: ")

if palabra in texto:
    print("Encontró la palabra: ",palabra)
else: 
    print("No se encontró la palabra")


