import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title('Manejo eventos entry')
ventana.geometry('500x500')
ventana.iconbitmap(r'C:\Users\marti\OneDrive\Escritorio\Programación\udemy_python\UI Tkinter\Iconos\boton_menu.ico')

entrada1 = ttk.Entry(ventana, width=20)
entrada1.grid(row=0, column=0)


def guardar():
    print(entrada1.get())
    boton1.config(text=entrada1.get())
    # Eliminar el contenido de la caja
    # entrada1.delete(0, tk.END)
    # Seleccionar el texto de la caja
    entrada1.select_range(0, tk.END)
    # Para hacerlo efectivo, debemos de hacer un focus
    entrada1.focus()


# Creamos un boton para manejar los eventos
boton1 = ttk.Button(ventana, text='Guardar información', command=guardar)
boton1.grid(row=0, column=1)

ventana.mainloop()
