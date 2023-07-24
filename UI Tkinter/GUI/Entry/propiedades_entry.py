import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title('Propiedades de entry')
ventana.geometry('500x500')
ventana.iconbitmap(r'C:\Users\marti\OneDrive\Escritorio\Programación\udemy_python\UI Tkinter\Iconos\boton_menu.ico')
# Con el parámetro show, indicamos los valores que se van a ver, como si fuera una contraseña
# entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, show='*')
# Con parámetro state, podemos añadirle disable para deshabilitar el entry, el estado predeterminado es NORMAL
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.NORMAL)
entrada1.grid(row=0, column=0)
entrada1.insert(0, 'Por favor, introduce un texto')
entrada1.config(state='readonly')


ventana.mainloop()