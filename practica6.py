num1 = float(input("Ingresar un número"))
num2 = float(input("Ingresar otro número"))

if num1 > num2:
    print (f"{num1}es mayor a {num2}")
    if num1 % 2 == 0:
        print ("es par")
    else:
        print ("es impar")

elif num2 > num1:
    print (f"{num2}es mayor a {num1}")
    if num2 % 2 == 0:
        print ("es par")
    else:
        print ("es impar")
else:
    print ("los numeros son iguales")
                                                                                                                         