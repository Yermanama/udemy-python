import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext

ventana = tk.Tk()
ventana.iconbitmap(
    r"Iconos\app-document-outlined-symbol-of-interface_icon-icons.com_57604.ico"
)
ventana.title("Imagenes")
ventana.geometry("500x500")


def crear_notebook():
    notebook = ttk.Notebook(ventana)
    tab_usuario = ttk.LabelFrame(notebook, text="Usuario")
    crear_comp_usuario(tab_usuario)
    tab_contenido = ttk.LabelFrame(notebook, text="Contenido")
    crear_comp_contenido(tab_contenido)
    tab_datalist = ttk.LabelFrame(notebook, text="Datalist")
    crear_comp_data(tab_datalist)
    tab_imagen = ttk.LabelFrame(notebook, text="Imagen")
    crear_comp_imagen(tab_imagen)
    notebook.add(tab_usuario, text="Usuario")
    notebook.add(tab_contenido, text="Contenido")
    notebook.add(tab_datalist, text="Datalist")
    notebook.add(tab_imagen, text="Imagen")
    notebook.pack(fill="both")


def crear_comp_usuario(frame):
    eti = ttk.Label(frame, text="Usuario:")
    eti.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
    ent = ttk.Entry(frame, width=20)
    ent.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

    def mostrar():
        messagebox.showinfo("Info usuario", f"Usuario -> {ent.get()}")

    bot = ttk.Button(frame, text="Mostrar", command=mostrar)
    bot.grid(row=1, column=0, columnspan=2)
    

def crear_comp_contenido(frame):
    contenido = """Far over the Misty Mountains cold
    To dungeons deep and caverns old
    We must await, ere break of day,
    To find our long forgotten gold.
    The pines were roaring on the height,
    The winds were moaning in the night.
    The fire was red, it flaming spread;
    The trees like torches blazed with light.
    The wind was on the withered heath,
    But in the forest stirred no leaf:
    There shadows lay be night or day,
    And dark things silent crept beneath.
    The wind went on from West to East;
    All movement in the forest ceased,
    But shrill and harsh across the marsh
    Its whistling voices were released.
    Farewell we call to hearth and hall!
    Though wind may blow and rain may fall,
    We must await ere break of day
    Far over wood and mountain tall."""

    scroll = scrolledtext.ScrolledText(frame, width=20, height=10, wrap=tk.WORD)
    scroll.insert(tk.INSERT, contenido)
    scroll.grid(row=0, column=0)


def crear_comp_data(frame):
    valores = [x+1 for x in range(100, 110)]
    combobox = ttk.Combobox(frame, width=10, values= valores)
    combobox.grid(row=0, column=0, padx=10, pady=10)
    combobox.current(4)
    
    def mostrar():
        messagebox.showinfo('Valor seleccionado', f'El valor seleccionado es -> {combobox.get()}')

    boton = ttk.Button(frame, text='Mostrar', command=mostrar)
    boton.grid(row=1, column=0)


def crear_comp_imagen(frame):
    ruta_imagen = r'C:\Users\marti\OneDrive\Escritorio\Programación\udemy_python\UI Tkinter\Componentes\Iconos\python-logo.png'
    imagen = tk.PhotoImage(file=ruta_imagen)
    def info():
        messagebox.showinfo('Info imagen', f'El nombre de la imagen es -> {imagen.cget("file")}')
    boton_imagen = ttk.Button(frame, image=imagen, command=info)
    boton_imagen.grid(row=0, column=0)


crear_notebook()

ventana.mainloop()