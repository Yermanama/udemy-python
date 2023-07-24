import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry("500x500")
ventana.iconbitmap(
    r"Iconos\app-document-outlined-symbol-of-interface_icon-icons.com_57604.ico"
)
ventana.title("Segundo tabulador")


def crear_componentes(frame):
    etiqueta = ttk.Label(frame, text="Nombre:")
    etiqueta.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
    entrada = ttk.Entry(frame, width=30)
    entrada.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

    def enviar():
        messagebox.showinfo("Información", f"Usuario: {entrada.get()}")

    boton = ttk.Button(frame, text="Enviar", command=enviar)
    boton.grid(row=1, column=0, columnspan=2)


def crear_tabuladores():
    notebook = ttk.Notebook(ventana)
    frame1 = ttk.Frame(notebook)
    crear_componentes(frame1)
    frame2 = ttk.LabelFrame(notebook, text='Contenido')
    crear_componentes(frame2)
    notebook.add(frame1, text='Usuario')
    notebook.add(frame2, text='Contenido')
    notebook.pack(fill='both')

crear_tabuladores()

ventana.mainloop()