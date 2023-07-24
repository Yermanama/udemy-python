import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry("500x500")
ventana.title("Tabuladores")
ventana.iconbitmap(
    r"Iconos\app-document-outlined-symbol-of-interface_icon-icons.com_57604.ico"
)


def crear_tabulador():
    # Creamos el controlador de tabuladores (NoteBook)
    notebook = ttk.Notebook(ventana)
    # Ahora creamos el tabulador que dependa del notebook (Frame)
    tabulador = ttk.Frame(notebook)
    # Lo añadimos al notebook
    notebook.add(tabulador, text="Primer tabulador")
    # Mostramos el frame para que ocupe todo el notebook
    notebook.pack(fill="both")

    # Agregamos elementos al frame
    etiqueta = ttk.Label(tabulador, text="Nombre:")
    etiqueta.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
    entrada = ttk.Entry(tabulador, width=30)
    entrada.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

    def enviar():
        messagebox.showinfo("Información usuario", f"Nombre: {entrada.get()}")

    boton = ttk.Button(tabulador, text="Enviar", command=enviar)
    boton.grid(row=1, column=0, columnspan=2)


crear_tabulador()

ventana.mainloop()
