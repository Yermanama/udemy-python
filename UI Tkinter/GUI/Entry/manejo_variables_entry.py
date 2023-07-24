import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title('Manejo variables entry')
ventana.geometry('500x500')
ventana.iconbitmap(r'C:\Users\marti\OneDrive\Escritorio\Programación\udemy_python\UI Tkinter\Iconos\boton_menu.ico')

# Definimos una variable que podremos modificar posteriormente (set), leer (get)
# Value es el valor por defecto que va a tener la variable
entrada_var1 = tk.StringVar(value='Valor por default')
entrada1 = ttk.Entry(ventana, width=20, textvariable=entrada_var1)
entrada1.grid(row=0, column=0)


def guardar_info():
    boton_guardar.config(
        text=entrada_var1.get())  # recuperamos la información a partir de la varible asociada con la caja de texto
    # Modificación, utilizamos la varibale de texto y el método set
    entrada_var1.set('Cambio...')
    # Para recuperar la información
    print(entrada_var1.get())
    print(entrada1.get())


boton_guardar = ttk.Button(ventana, text='Guardar info', command=guardar_info)
boton_guardar.grid(row=0, column=1)

ventana.mainloop()
