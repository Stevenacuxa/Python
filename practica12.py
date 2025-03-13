#def para definir funciones
def sumar(x,y):
    return x+y

def restar(x,y):
    return x-y

def multiplicar (x,y):
    return x*y

def dividir (x,y):
    if(y != 0):
        return x/y
    else:
        print ("NO SE PUEDE DIVIDIR CON CERO")

while True:
    v1= float(input("Primer número: "))
    v2= float(input("Segundo número: "))
    x=sumar (v1,v2)
    print (f"La suma es: {x}")
    x=restar (v1,v2)
    print (f"La resta es: {x}")
    x=multiplicar (v1,v2)
    print (f"La multiplicacion es: {x}")
    x=dividir (v1,v2)
    print (f"La division es: {x}")