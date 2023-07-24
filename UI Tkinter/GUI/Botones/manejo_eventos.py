import tkinter as tk
from tkinter import ttk 

ventana = tk.Tk()

ventana.geometry('600x600')
ventana.title('Manejo de eventos')
ventana.iconbitmap(r'Iconos\boton_menu.ico')

# Definimos nuesto método
def evento_click():
    boton1.config(text='Boton presionado', state=tk.DISABLED)
    print('Ejecución del evento -> evento_click')
    # Creamos un nuevo componente
    boton2 = ttk.Button(ventana, text='Nuevo botón')
    boton2.pack()
boton1 = ttk.Button(ventana, text='Manejo de eventos', command= evento_click)
boton1.pack()

ventana.mainloop()