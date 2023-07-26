import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from time import sleep

class Ventana(tk.Tk):
    
    def __init__(self) -> None:
        super().__init__()
        self.geometry('500x500')
        self.title('Ejercicio en POO')
        self.iconbitmap(r'Iconos\app-document-outlined-symbol-of-interface_icon-icons.com_57604.ico')
        self._crear_notebook()

    def _crear_notebook(self):
        notebook = ttk.Notebook(self)
        usuario = ttk.Frame(notebook)
        self._tab_usuario(usuario)
        contenido = ttk.Frame(notebook)
        self._tab_contenido(contenido)
        datalist = ttk.Frame(notebook)
        self._tab_datalist(datalist)
        imagen = ttk.Frame(notebook)
        self._tab_imagen(imagen)
        barra = ttk.Frame(notebook)
        self._tab_barra(barra)
        notebook.add(usuario, text='Usuario')
        notebook.add(contenido, text='Contenido')
        notebook.add(datalist, text='Datalist')
        notebook.add(imagen, text='Imagen')
        notebook.add(barra, text='Barra de progreso')
        notebook.pack(fill='both')

    def _tab_usuario(self, frame):
        eti = ttk.Label(frame, text='Usuario:')
        eti.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        ent = ttk.Entry(frame, width=20)
        ent.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
        def mostrar():
            messagebox.showinfo('Info usuario', f'Usuario: {ent.get()}')

        bot = ttk.Button(frame, text='Mostrar', command=mostrar)
        bot.grid(row=1, column=0, columnspan=2)

    
    def _tab_contenido(self, frame):
        contenido = 'Esto es una frase para rellenar el contenido de mi scrolled text'
        scroll = scrolledtext.ScrolledText(frame, width=20, height=20, wrap=tk.WORD)
        scroll.insert(tk.INSERT, contenido)
        scroll.grid(row=0, column=0)


    def _tab_datalist(self, frame):
        valores = [x+1 for x in range(100, 110)]
        combobox = ttk.Combobox(frame, values=valores, width=10)
        combobox.current(5)
        combobox.grid(row=0, column=0, padx=5, pady=5)

        def mostrar():
            messagebox.showinfo('Numero seleccionado', f'Has seleccionado el numero {combobox.get()}')

        bot = ttk.Button(frame, text='Mostrar numeero', command=mostrar)
        bot.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

    
    def _tab_imagen(self, frame):
        ruta_imagen = r'C:\Users\marti\OneDrive\Escritorio\Programación\udemy_python\UI Tkinter\Componentes\Iconos\python-logo.png'
        imagen = tk.PhotoImage(file=ruta_imagen)
        
        def showinfo():
            messagebox.showinfo('Info imagen', f'La ruta de la imagen es \n {imagen.cget("file")}')

        bot = ttk.Button(frame, image=imagen, command=showinfo)
        bot.grid(row=0, column=0)

    
    def _tab_barra(self, frame):
        barra = ttk.Progressbar(frame, orient='horizontal', length=400)
        barra.grid(row=0, column=0, columnspan=4)

        def ciclo():
            barra.start()

        def parar():
            barra.stop()

        def retraso():
            tiempo_espera = 100000
            self.after(tiempo_espera, barra.stop)

        def ejecutar():
            barra['maximum'] = 100
            for valor in range(101):
                sleep(0.05)
                barra['value'] = valor
                barra.update()
            barra['value'] = 0

        bot_ciclo = ttk.Button(frame, text='Ciclo', command=ciclo)
        bot_ciclo.grid(row=1, column=0, padx=5, pady=5)
        bot_parar = ttk.Button(frame, text='Parar', command=parar)
        bot_parar.grid(row=1, column=1, padx=5, pady=5)
        bot_retraso = ttk.Button(frame, text='Parar con retraso', command=parar)
        bot_retraso.grid(row=1, column=2, padx=5, pady=5)
        bot_ejecutar = ttk.Button(frame, text='Ejecutar', command=ejecutar)
        bot_ejecutar.grid(row=1, column=3, padx=5, pady=5)


if __name__ == '__main__':
    ventana = Ventana()
    ventana.mainloop()