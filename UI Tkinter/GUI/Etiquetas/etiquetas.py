import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title('Manejo de etiquetas')
ventana.geometry('500x500')
ventana.iconbitmap(r'C:\Users\marti\OneDrive\Escritorio\Programación\udemy_python\UI Tkinter\Iconos\boton_menu.ico')


variable1 = tk.StringVar(value='Valor por defecto')
entrada1 = ttk.Entry(ventana, width=20, textvariable=variable1)
entrada1.grid(row=0, column=0)


# Vamos a crear una etiqueta (label)
etiqueta1 = ttk.Label(ventana, text='Aquí se mostrará la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)


def guardar_info():
    boton1.config(text=variable1.get())
    variable1.set('Se ha guardado la info')
    etiqueta1.config(text=variable1.get())


boton1 = ttk.Button(ventana, text='Guardar info', command=guardar_info)
boton1.grid(row=0, column=1)

ventana.mainloop()
