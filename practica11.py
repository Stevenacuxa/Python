numero = 100
while True:
    bandera: False
    for x in range (2, int(numero/2)):
        if(numero % x == 0):
            bandera = True
            break
    if (bandera == False):
       print(f" | {numero}")
       
    numero = numero + 1