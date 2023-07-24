import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title('Padding')
ventana.geometry('500x500')
ventana.iconbitmap(r'C:\Users\marti\OneDrive\Escritorio\Programación\udemy_python\UI Tkinter\Iconos\boton_menu.ico')

ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=2)
ventana.columnconfigure(0, weight=2)
ventana.columnconfigure(1, weight=2)


def evento1():
    boton1.config(text='Boton pulsado ')


def evento2():
    boton2.config(text='Boton pulsado ')


def evento3():
    boton3.config(text='Boton pulsado ')


def evento4():
    boton4.config(text='Boton pulsado', fg='white', font=('Helvetica', 12), bg='gray', activebackground='darkgray',
                  activeforeground='white')


boton1 = ttk.Button(ventana, text='Boton 1', command=evento1)
boton2 = ttk.Button(ventana, text='Boton 2', command=evento2)
boton3 = ttk.Button(ventana, text='Boton 3', command=evento3)
boton4 = tk.Button(ventana, text='Boton 4', command=evento4)

# Vamos a cambiar el padding en esta parte de aquí, el del botón 1
# Lo que hace padx y pady es añadir un espacio tanto arriba como debajo del botón
# Ipadx ipady añaden espacio dentro del botón
# Column span, expande el botón en un número de columnas
# Se puede hacer lo mismo con row span
boton1.grid(row=0, column=0, padx=40, pady=40, sticky='NSEW', ipadx=20, ipady=150, columnspan=2)

boton2.grid(row=1, column=0)
boton3.grid(row=0, column=1)
boton4.grid(row=1, column=1)

ventana.mainloop()
