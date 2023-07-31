import tkinter as tk
from tkinter import messagebox


class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x450")
        self.resizable(0, 0)
        self.title("Calculadora")
        self.iconbitmap(r"calculadora.ico")
        # Atributos de clase
        self.expresion = ""
        # Caja de texto
        self.entrada = None
        # StringVar lo utlizamos para obtener o actualizar el valor del input
        self.entrada_texto = tk.StringVar()
        # Creamos los componentes
        self._creacion_componentes()

    # Metodos de clase
    # Metodo para crear los componentes
    def _creacion_componentes(self):
        # Creamos un frame para la caja de texto
        entrada_frame = tk.Frame(self, width=400, height=50, bg="grey")
        entrada_frame.pack(side=tk.TOP)
        # Caja de texto
        entrada = tk.Entry(
            entrada_frame,
            font=("arial", 18, "bold"),
            textvariable=self.entrada_texto,
            width=30,
            justify=tk.RIGHT,
        )
        entrada.grid(row=0, column=0, padx=5, pady=5)

        # Creamos otro frame para la parte inferior
        botones_frame = tk.Frame(self, width=400, height=450, bg="grey")
        botones_frame.pack()

        # Primer renglón
        # Boton limpiar
        boton_limpiar = tk.Button(
            botones_frame,
            text="C",
            width=32,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=self._evento_limpiar,
        ).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
        # Boton dividir
        boton_division = tk.Button(
            botones_frame,
            text="/",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self._evento_click("/"),
        ).grid(row=0, column=3, padx=1, pady=1)

        # Segundo renglón
        boton_siete = tk.Button(
            botones_frame,
            text="7",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self._evento_click(7),
        ).grid(row=1, column=0, padx=1, pady=1)

        boton_ocho = tk.Button(
            botones_frame,
            text="8",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self._evento_click(8),
        ).grid(row=1, column=1, padx=1, pady=1)

        boton_nueve = tk.Button(
            botones_frame,
            text="9",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self._evento_click(9)
        ).grid(row=1, column=2, padx=1, pady=1)


        boton_multiplicacion = tk.Button(
            botones_frame,
            text="*",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self._evento_click("*"),
        ).grid(row=1, column=3, padx=1, pady=1)
    
        # Tercer renglon
        boton_cuatro = tk.Button(
            botones_frame,
            text="4",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self._evento_click(4)
        ).grid(row=2, column=0, padx=1, pady=1)

        boton_cinco = tk.Button(
            botones_frame,
            text="5",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self._evento_click(5)
        ).grid(row=2, column=1, padx=1, pady=1)

        boton_seis = tk.Button(
            botones_frame,
            text="6",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self._evento_click(6)
        ).grid(row=2, column=2, padx=1, pady=1)
            
        boton_resta = tk.Button(
            botones_frame,
            text="-",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self._evento_click("-"),
        ).grid(row=2, column=3, padx=1, pady=1)

        # Cuarto renglon
        boton_uno = tk.Button(
            botones_frame,
            text="1",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self._evento_click(1)
        ).grid(row=3, column=0, padx=1, pady=1)

        boton_dos = tk.Button(
            botones_frame,
            text="2",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self._evento_click(2)
        ).grid(row=3, column=1, padx=1, pady=1)

        boton_tres = tk.Button(
            botones_frame,
            text="3",
            width=10,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self._evento_click(3)
        ).grid(row=3, column=2, padx=1, pady=1)
            
        boton_suma = tk.Button(
            botones_frame,
            text="+",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self._evento_click("+"),
        ).grid(row=3, column=3, padx=1, pady=1)

        # Quinto renglon
        boton_cero = tk.Button(
            botones_frame,
            text="0",
            width=21,
            height=3,
            bd=0,
            bg="#fff",
            cursor="hand2",
            command=lambda: self._evento_click(0)
        ).grid(row=4, column=0, padx=1, pady=1, columnspan=2)

        boton_punto = tk.Button(
            botones_frame,
            text=".",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=lambda: self._evento_click("."),
        ).grid(row=4, column=2, padx=1, pady=1)
            
        boton_igual = tk.Button(
            botones_frame,
            text="=",
            width=10,
            height=3,
            bd=0,
            bg="#eee",
            cursor="hand2",
            command=self._evento_evaluar,
        ).grid(row=4, column=3, padx=1, pady=1)

    def _evento_limpiar(self):
        self.expresion = ""
        self.entrada_texto.set(self.expresion)

    def _evento_click(self, elemento):
        # concatenamos el nuevo elmento a al expresoin ya existente
        self.expresion = f"{self.expresion}{elemento}"
        self.entrada_texto.set(self.expresion)

    def _evento_evaluar(self):
        # eval evalua la expresoin str como una expresión aritmética
        try:
            if self.expresion:
                resultado = str(eval(self.expresion)) 
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror('Error', f'Ocurrió un error: {e}')
            self.entrada_texto.set('')
        finally:
            self.expresion = ''


if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.mainloop()
