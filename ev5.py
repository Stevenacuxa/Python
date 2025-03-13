cadena = input("Ingrese una oracion: ")
longCad = len(cadena)
vocales = 0

for i in range (0, longCad):
    if (cadena[i] == " "):
        vocales +=1

print("La oracion ingresada es: ", cadena)
print("La cantidad de vocales es: ",vocales)