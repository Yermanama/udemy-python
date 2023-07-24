import sys
import tkinter as tk
from tkinter import ttk, Menu, messagebox

ventana = tk.Tk()
ventana.iconbitmap(
    r"C:\Users\marti\OneDrive\Escritorio\Programación\udemy_python\UI Tkinter\Iconos\boton_menu.ico"
)
ventana.geometry("500x500")
ventana.title("COnfigurando opción salir")

entrada = ttk.Entry(ventana, width=20)
entrada.grid(row=0, column=0)
etiqueta = ttk.Label(ventana, text="Esto es una etiqueta")
etiqueta.grid(row=1, column=0, columnspan=2)


def lanzar_mensaje():
    mensaje = entrada.get()
    etiqueta.config(text=entrada.get())
    if mensaje:
        messagebox.showinfo(mensaje)


def salir():
    ventana.quit()
    ventana.destroy()
    sys.exit()


boton = ttk.Button(ventana, text="Lanzar mensaje", command=lanzar_mensaje)
boton.grid(row=0, column=1)

def crear_menu():
    menu_principal = Menu(ventana)
    sub_archivo = Menu(menu_principal, tearoff=False)
    sub_archivo.add_command(label='Nuevo')
    sub_archivo.add_separator()
    sub_archivo.add_command(label='Salir', command=salir)
    sub_ayuda = Menu(menu_principal, tearoff=False)
    sub_ayuda.add_command(label='Acerca de')
    menu_principal.add_cascade(menu=sub_archivo, label='Archivo')
    menu_principal.add_cascade(menu=sub_ayuda, label= 'Ayuda')
    ventana.config(menu=menu_principal)


crear_menu()

ventana.mainloop()