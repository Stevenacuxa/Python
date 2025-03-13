num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

sum = num1 + num2
print (f"Suma = {sum}")

res = num1 - num2
print (f"Resta = {res}")

mul = num1 * num2
print (f"Multiplicacion = {mul}")

if num2 != 0:
    div = num1 / num2
    print (f"Division = {div}")
else: 
    print("NO se puede dividir por cero")
