num1 = float(input("Introducir el primer numero: "))
num2 = float(input("Introducir el segundo numero: "))
num3 = float(input("Introducir el tercer numero: "))

mayor = max(num1, num2, num3)

if num1 >= mayor:
    print (f"El numero {num1} es el mayor")
elif num2 >= mayor:
    print (f"El numero {num2} es el mayor")
else:
    print (f"El numero {num3} es el mayor")