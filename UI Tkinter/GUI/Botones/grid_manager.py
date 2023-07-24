import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo del grid')
ventana.iconbitmap(r'C:\Users\marti\OneDrive\Escritorio\Programación\udemy_python\UI Tkinter\Iconos\boton_menu.ico')


def evento1():
    boton1.config(text='Boton 1 presionado')


def evento2():
    boton2.config(text='Botón 2 presionado')


# Definimos dos botones
boton1 = ttk.Button(ventana, text='Botón 1', command=evento1)
boton1.grid(row=0, column=0)
boton2 = ttk.Button(ventana, text='Boton 2', command=evento2)
boton2.grid(row=3, column=4)
ventana.mainloop()
