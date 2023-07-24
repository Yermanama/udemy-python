import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title('Configuracion botones')
ventana.geometry('500x500')
ventana.iconbitmap(r'C:\Users\marti\OneDrive\Escritorio\Programación\udemy_python\UI Tkinter\Iconos\boton_menu.ico')

ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=2)
ventana.columnconfigure(0, weight=2)
ventana.columnconfigure(1, weight=2)


def evento1():
    boton1.config(text='Botón presionado')


def evento2():
    boton2.config(text='Botón presionado')


def evento3():
    boton3.config(text='Botón presionado')


def evento4():
    # Foreground (fg) nos permite cambiar el color de las letras del botón
    # Relief nos permite cambiar el relieve del botón
    # Background (bg) es el color de fondo
    boton4.config(text='Botón presionado', fg='blue', relief=tk.GROOVE, bg='gray')


boton1 = ttk.Button(ventana, text='Boton 1', command=evento1)
boton2 = ttk.Button(ventana, text='Boton 2', command=evento2)
boton3 = ttk.Button(ventana, text='Boton 3', command=evento3)

# En vez de usar el módulo de ttk, el cual permite obtener una configuración predeterminada más homogenea entre los
# distintos SO, podemos trabajar directamente sobre tk para añadir un estilo que nos guste más
boton4 = tk.Button(ventana, text='Boton 4', command=evento4)


boton1.grid(row=0, column=0)
boton2.grid(row=1, column=0)
boton3.grid(row=0, column=1)
boton4.grid(row=1, column=1)

ventana.mainloop()
