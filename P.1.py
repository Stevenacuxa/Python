notas = []
sum= 0 

for x in range(3):
    nota=0
    while nota < 1 or nota > 5:
        nota=int(input(f"Ingrese la nota {x + 1}:"))
        notas.append(nota)

        sum = sum + nota

        promedio= sum/3

print(f"El promedio de las notas {notas} es: {promedio}")

if promedio >1.7:
        print("Aprobado")
else:
        print("Reprobado")





