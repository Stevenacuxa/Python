import os

comandoPygame1 = "python -m pip uninstall pygame"
comandoPygame2 = "python -m pip install pygame"
versiones = "python -m pip list"
while True:
    print ("1. Pygame")
    opcion = input("Instalar Pygame: ")

    if opcion == "1":
        os.system (comandoPygame1)
        os.system (comandoPygame2)
        print(os.system(versiones))

