import tkinter as tk
from tkinter import ttk, messagebox

class LoginVentana(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.geometry('300x150')
        self.title('Login con POO')
        self.iconbitmap(r'C:\Users\marti\OneDrive\Escritorio\Programación\udemy_python\UI Tkinter\Iconos\boton_menu.ico')
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=2)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.resizable(0,0)
        self._crear_componentes()

    def _crear_componentes(self):
        u_label = ttk.Label(self, text='Usuario:')
        u_label.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
        self.u_entry = ttk.Entry(self, width=30)
        self.u_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        p_label = ttk.Label(self, text='Password:')
        p_label.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
        self.p_entry = ttk.Entry(self, width=30, show='*')
        self.p_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)


        boton = ttk.Button(self, text='Lanzar mensaje', command=self._login)
        boton.grid(row=2,column=0, columnspan=2)
    
    def _login(self): 
        messagebox.showinfo('Datos login', f'Usuario: {self.u_entry.get()}\nContraseña: {self.p_entry.get()}')

if __name__ == '__main__':
    ventana_login = LoginVentana()
    ventana_login.mainloop()