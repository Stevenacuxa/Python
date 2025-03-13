calificacion = 1
sumador = 0
cantidad = 0
promedio = 0.0
#alumnos = (input("introducir nombre del alumno: "))
while calificacion != 0:
    calificacion = int(input("introducir calificación"))
    if calificacion >= 1 and calificacion <= 5:
        cantidad = cantidad + 1
        sumador = sumador + calificacion

if cantidad > 0 :
    promedio = sumador / cantidad
    print(f"El promedio general es {promedio}")
else:
    print("No hay nada que calcular")