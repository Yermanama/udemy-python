import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

ventana = tk.Tk()
ventana.iconbitmap(
    r"Iconos\app-document-outlined-symbol-of-interface_icon-icons.com_57604.ico"
)
ventana.geometry("500x500")
ventana.title("Trabajando con datalist")


def crear_notebook():
    notebook = ttk.Notebook(ventana)
    tab_nombre = ttk.LabelFrame(notebook, text="Usuario")
    componentes_usuario(tab_nombre)
    tab_contenido = ttk.LabelFrame(notebook, text="Contenido")
    componentes_contenido(tab_contenido)
    tab_datalist = ttk.LabelFrame(notebook, text="Datalist")
    componentes_datalist(tab_datalist)
    notebook.add(tab_nombre, text="Usuario")
    notebook.add(tab_contenido, text="Contenido")
    notebook.add(tab_datalist, text="Prueba datalist")
    notebook.pack(fill="both")


def componentes_usuario(frame):
    etiqueta = ttk.Label(frame, text="Usuario:")
    etiqueta.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
    entrada = ttk.Entry(frame, width=20)
    entrada.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

    def mostrar_mesaje():
        messagebox.showinfo("Mensaje info usuario", f"Usuario -> {entrada.get()}")

    boton = ttk.Button(frame, text='Enviar', command=mostrar_mesaje)
    boton.grid(row=1, column=0, columnspan=2)

def componentes_contenido(frame):
    contenido = 'Esto es un texto de prueba para poder escribir y ver si está bien mi scrolled text'
    scroll = scrolledtext.ScrolledText(frame, width= 20, height=10, wrap=tk.WORD)
    scroll.insert(tk.INSERT, contenido)
    scroll.grid(row=0, column=0)


def componentes_datalist(frame):
    datos = [x+1 for x in range(100, 110)]
    combobox = ttk.Combobox(frame, width=10, values=datos)
    combobox.grid(row=0, column=0)
    combobox.current(4)

    def mostrar():
        messagebox.showinfo('Info del datalist', f'El número seleccionado es: {combobox.get()}')

    boton = ttk.Button(frame, text='Mostrar', command=mostrar)
    boton.grid(row=0, column=1)


crear_notebook()

ventana.mainloop()