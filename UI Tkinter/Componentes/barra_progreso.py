import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from time import sleep

ventana = tk.Tk()
ventana.geometry("500x500")
ventana.iconbitmap(
    r"Iconos\app-document-outlined-symbol-of-interface_icon-icons.com_57604.ico"
)
ventana.title("Barra de progreso")


def crear_notebook():
    notebook = ttk.Notebook(ventana)
    usuario = ttk.Frame(notebook)
    comp_usuario(usuario)
    contenido = ttk.Frame(notebook)
    comp_contenido(contenido)
    datalist = ttk.Frame(notebook)
    comp_datalist(datalist)
    imagen = ttk.Frame(notebook)
    comp_imagen(imagen)
    barra = ttk.Frame(notebook)
    comp_barra(barra)
    notebook.add(usuario, text="Usuario")
    notebook.add(contenido, text="Contenido")
    notebook.add(datalist, text="Datalist")
    notebook.add(imagen, text="Imagen")
    notebook.add(barra, text="Barra progreso")
    notebook.pack(fill="both")


def comp_usuario(frame):
    eti = ttk.Label(frame, text="Usuario")
    eti.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
    ent = ttk.Entry(frame, width=20)
    ent.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

    def mostrar():
        messagebox.showinfo("Info usuario", f"Usuario -> {ent.get()}")

    boton = ttk.Button(frame, text="Mostrar", command=mostrar)
    boton.grid(row=1, column=0, columnspan=2)


def comp_contenido(frame):
    contenido = "Este es mi texto con el contenido"
    scroll = scrolledtext.ScrolledText(frame, width=20, height=20, wrap=tk.WORD)
    scroll.insert(tk.INSERT, contenido)
    scroll.grid(row=0, column=0)


def comp_datalist(frame):
    valores = [x + 1 for x in range(100, 110)]
    datalist = ttk.Combobox(frame, values=valores, width=10)
    datalist.current(4)
    datalist.grid(row=0, column=0)

    def mostrar():
        messagebox.showinfo(
            "Numero seleccionado", f"Numero seleccionado -> {datalist.get()}"
        )

    boton = ttk.Button(frame, text="Mostrar", command=mostrar)
    boton.grid(row=1, column=0, columnspan=2)


def comp_imagen(frame):
    ruta_imagen = r"C:\Users\marti\OneDrive\Escritorio\Programación\udemy_python\UI Tkinter\Componentes\Iconos\python-logo.png"
    imagen = tk.PhotoImage(file=ruta_imagen)

    def mostrar():
        messagebox.showinfo('Info de imagen', f'Nombre archivo {imagen.cget("file")}')
    
    boton = ttk.Button(frame, image=imagen, command=mostrar)
    boton.grid(row=0, column=0)


def comp_barra(frame):
    barra_progreso = ttk.Progressbar(frame, orient='horizontal', length=400)
    barra_progreso.grid(row=0, column=0, columnspan=4)

    def iniciar():
        barra_progreso.start()

    def parar():
        barra_progreso.stop()

    def parar_delayed():
        esperar_ms = 1000
        ventana.after(esperar_ms, barra_progreso.stop)
    
    def ejecutar_barra():
        barra_progreso['maximum'] = 100
        for valor in range(101):
            sleep(0.05)
            barra_progreso['value'] = valor
            barra_progreso.update()
        
    inicio = ttk.Button(frame, text='Iniciar', command=iniciar)
    inicio.grid(row=1, column=0)
    parada = ttk.Button(frame, text='Detener', command=parar)
    parada.grid(row=1, column=1)
    retardo = ttk.Button(frame, text='Parada con retraso', command=parar_delayed)
    retardo.grid(row=1, column=2)
    empezar = ttk.Button(frame, text='Empezar barra', command=ejecutar_barra)
    empezar.grid(row=1, column=3)


crear_notebook()

ventana.mainloop()