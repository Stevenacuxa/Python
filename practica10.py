#cuadrado
for x in range (6):
    print ("* "*6)

#triangulo 
for x in range (1,5):
    print("* "*x)

#borde
m= 5
for x in range (m):
    if x == 0 or x == m -1:
        print ("**********")
    else:
        print ("*        *")