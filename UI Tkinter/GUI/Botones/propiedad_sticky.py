import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('500x600')
ventana.title('Propiedad sticky')
ventana.iconbitmap(r'C:\Users\marti\OneDrive\Escritorio\Programación\udemy_python\UI Tkinter\Iconos\boton_menu.ico')


def evento1():
    boton1.config(text='Boton presionado')


def evento2():
    boton2.config(text='Boton presionado')


boton1 = ttk.Button(ventana, text='Boton 1', command=evento1)
boton2 = ttk.Button(ventana, text='Boton 2', command=evento2)
boton1.grid(row=0, column=0,sticky='W')
# El argumento sticky nos permite mantener el botón 'pegado' a algún lugar de su grid
boton2.grid(row=1, column=0, sticky='E')
ventana.mainloop()
