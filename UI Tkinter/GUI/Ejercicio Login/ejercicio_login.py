import tkinter as tk
from tkinter import messagebox, ttk

ventana = tk.Tk()
ventana.geometry("300x130")
ventana.title("Login")
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=1)
ventana.grid_rowconfigure(2, weight=2)
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=3)
ventana.resizable(0, 0)

l_usuario = ttk.Label(ventana, text="Usuario:")
l_usuario.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
l_pass = ttk.Label(ventana, text="Contraseña:")
l_pass.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
e_usuario = ttk.Entry(ventana, width=30)
e_usuario.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
e_pass = ttk.Entry(ventana, width=30, show='*')
e_pass.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)


def login():
    usuario = e_usuario.get()
    password = e_pass.get()
    messagebox.showinfo("Datos info", f"Usuario: {usuario}\nContraseña: {password}")


boton = ttk.Button(ventana, text="Login", command=login)
boton.grid(row=2, column=0, columnspan=2)

ventana.mainloop()
