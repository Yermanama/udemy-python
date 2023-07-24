import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title('Configuración del grid')
ventana.geometry('500x600')
ventana.iconbitmap(r'C:\Users\marti\OneDrive\Escritorio\Programación\udemy_python\UI Tkinter\Iconos\boton_menu.ico')


# Configurar el grid
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=5)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)

def evento1():
    boton1.config(text='Boton pulsado')


def evento2():
    boton2.config(text='Boton pulsado')


def evento3():
    boton3.config(text='Boton pulsado')


def evento4():
    boton4.config(text='Boton pulsado')


boton1 = ttk.Button(ventana, text='Boton 1', command=evento1)
boton2 = ttk.Button(ventana, text='Boton 2', command=evento2)
boton3 = ttk.Button(ventana, text='Boton 3', command=evento3)
boton4 = ttk.Button(ventana, text='Boton 4', command=evento4)

boton1.grid(row=0, column=0, sticky='NSWE')
boton2.grid(row=1, column=0, sticky='NSWE')
boton3.grid(row=0, column=1, sticky='NSWE')
boton4.grid(row=1, column=1, sticky='NSWE')

ventana.mainloop()
