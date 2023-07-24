import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext

ventana = tk.Tk()
ventana.title('Scrolled text')
ventana.geometry('500x500')
ventana.iconbitmap(r'Iconos\app-document-outlined-symbol-of-interface_icon-icons.com_57604.ico')


def crear_tab():
    notebook = ttk.Notebook(ventana)
    nombre = ttk.LabelFrame(notebook, text='Usuario')
    contenido_nombre(nombre)
    notebook.add(nombre, text='Nombre')
    contenido = ttk.LabelFrame(notebook, text='Contenido')
    contenido_contenido(contenido)
    notebook.add(contenido, text='Contenido')

    notebook.pack(fill='both')


def contenido_nombre(frame):
    etiqueta = ttk.Label(frame, text='Usuario')
    etiqueta.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
    entrada = ttk.Entry(frame, width=30)
    entrada.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
    
    def enviar():
        messagebox.showinfo('Información', f'Usuario: {entrada.get()}')
    
    boton = ttk.Button(frame, text='Enviar', command=enviar)
    boton.grid(row=1, column=0, columnspan=2)


def contenido_contenido(frame):
    contenido = 'Esta es una frase para probar el scrolled text'
    # El wrap es para que cuando se vaya a cortar una palabra, esta salte a la línea siguiente para no cortarse
    scroll = scrolledtext.ScrolledText(frame, width=30, height=10, wrap=tk.WORD)
    # Con el metodo insert, metemos el contenido en la caja
    scroll.insert(tk.INSERT, contenido)
    # Mostramos el componente
    scroll.grid(row=0, column=0)


crear_tab()

ventana.mainloop()