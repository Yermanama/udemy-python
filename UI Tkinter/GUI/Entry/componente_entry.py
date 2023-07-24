import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title('Componente entry')
ventana.geometry('500x500')
ventana.iconbitmap(r'C:\Users\marti\OneDrive\Escritorio\Programación\udemy_python\UI Tkinter\Iconos\boton_menu.ico')

# Width es la cantidad de caracteres que ocupa nuestra caja
# Justify es hacia donde se va a desplazar el texto que escribamos en el
# Con insert, debemos de indicar en qué parte de la caja, y qué queremos que se vea escrito en la caja de texto
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER)
entrada1.grid(row=0, column=0)
entrada1.insert(0, 'Por favor, escribe algo')
entrada1.insert(tk.END, '.')

ventana.mainloop()