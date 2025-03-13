from tkinter import *
from tkinter import ttk
def saludar():
    pass

ventana = Tk ()#constructor
ventana.title ("Mi computadora")
ventana.geometry("400x200")
marco = ttk.Frame(ventana, padding=10)
marco.grid()
etiqueta = ttk.Label(ventana, text="hola").grid(row=0, column=0)
boton = ttk.Button(ventana, text="OK", command=saludar).grid(row=0, column=1)
ventana.mainloop()