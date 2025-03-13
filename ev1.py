#Ingresar el sueldo de una persona, si supera los 80000000 millones mostrar un mensaje en pantalla indicando que debe abonar IRP.
#sino mostrar el mensaje la persona No debe abonar impuestos

MONTOIRP = 80000000
sueldo = int(input("Ingrese cual es su sueldo: "))

sueldoAnual = sueldo * 12
if sueldoAnual > MONTOIRP : 
    print ("Esta persona debe pagar impuestos")
else:
    print("NO debe abonar impuestos")