usuarios = {"admin":"12345","pepe":"abc123"}
usuario = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")
intentos = 1
if usuario in usuarios:
    while True:
        if usuarios[usuario] == password:
            print("Acceso correcto")
            break
        else:
            intentos = intentos + 1 
            if (intentos < 4):
                print(f"Error de contraseña, {intentos} de 3")
                password = input ("Ingrese su contraseña: ")
            else:
                print(f"Haz alcanzado los intentos permitidos, {intentos - 1} de 3.\nCuenta bloqueada")
                break
else:
    print("El usuario no existe")
