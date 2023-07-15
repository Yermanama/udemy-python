import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

ventana.geometry('600x600')
ventana.title('Título de mi ventana')
# Ponemos el icono de la ventana
ventana.iconbitmap('Iconos\\boton_menu.ico')

# Creamos un objeto boton1

boton1 = ttk.Button(ventana, text='Dar click')

# Utilizamos el pack layout manager para mostrar el botón en la ventana
boton1.pack()

ventana.mainloop()