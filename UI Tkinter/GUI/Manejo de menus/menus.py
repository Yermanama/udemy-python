import tkinter as tk
from tkinter import ttk, messagebox, Menu

ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title("Creando un menu")
ventana.iconbitmap(
    r"C:\Users\marti\OneDrive\Escritorio\Programación\udemy_python\UI Tkinter\Manejo de menus"
)

entrada1 = ttk.Entry(ventana, width=30)
entrada1.grid(row=0, column=0)
etiqueta = ttk.Label(ventana, text="Esto es una etiqueta")
etiqueta.grid(row=1, column=0, columnspan=2)


def mostrar_mensaje():
    mensaje = entrada1.get()
    etiqueta.config(text=entrada1.get())
    if mensaje:
        messagebox.showinfo(mensaje)


def crear_menu():
    # Creamos un menu principal
    menu_principal = Menu(ventana)
    # Creamos un menu que sirgurá del menu principal, y además ponemos tear_off falso para que no se se separe del principal
    submenu = Menu(menu_principal, tearoff=False)
    # Agregamos una nueva opción al submenu
    submenu.add_command(label="Nuevo")
    # Agregamos el submenu al menu principal, en forma de cascada, y añadimos label archivo para que salga ese menu pinchando esa opción 
    menu_principal.add_cascade(menu=submenu, label="Archivo")
    # Mostramos el menu en la ventana principal
    ventana.config(menu=menu_principal)


boton1 = ttk.Button(ventana, text="Mostrar mensaje", command=mostrar_mensaje)
boton1.grid(row=0, column=1)


crear_menu()


ventana.mainloop()
