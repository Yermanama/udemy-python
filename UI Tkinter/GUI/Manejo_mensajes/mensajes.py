import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.title('Manejo de mensajes')
ventana.iconbitmap(r'C:\Users\marti\OneDrive\Escritorio\Programación\udemy_python\UI Tkinter\Iconos\boton_menu.ico')
ventana.geometry('500x500')

entrada1 = ttk.Entry(ventana, width=50)
entrada1.grid(row=0, column=0)
etiqueta1 = ttk.Label(ventana, text='Hola que tal')
etiqueta1.grid(row=1, column=0, columnspan=2)

def guardar_mostrar():
    mensaje1 = entrada1.get()
    etiqueta1.config(text=entrada1.get())
    if mensaje1:
        messagebox.showinfo('Mensaje informativo -> ', mensaje1)
        messagebox.showerror('Mensaje de error ->', mensaje1)
        messagebox.showwarning('Mensaje de alerta', mensaje1)


boton1 = ttk.Button(ventana, text='Guardar y mostrar', command=guardar_mostrar)
boton1.grid(row=0, column=1)

ventana.mainloop()

