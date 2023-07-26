import tkinter as tk


class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x450")
        self.title("Calculadora")
        self.iconbitmap(r"calculadora.ico")
        self.resizable(0, 0)
        self.entrada = None
        self.entrada_texto = tk.StringVar()
        self.expresion = ""
        self._crear_frames()

    def _crear_frames(self):
        # Caja de resultados
        resultado_frame = tk.Frame(self, width=500, height=50)
        resultado_frame.pack(side=tk.TOP)
        caja_resultado = tk.Entry(
            resultado_frame,
            font=("Arial", 18, "bold"),
            textvariable=self.entrada,
            width=35,
            justify=tk.RIGHT,
        )
        caja_resultado.grid(row=0, column=0, sticky="nswe", pady=10, ipady=5)
        

        # Caja de botones
        botones_frame = tk.Frame(self, width=500, height=500)
        botones_frame.pack()

        # Fila 0
        boton_limpiar = tk.Button(
            botones_frame, text="C", command=self._limpiar, width=32
        )
        boton_limpiar.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

        boton_dividir = tk.Button(
            botones_frame, text="/", command=lambda: self._evento_click("/"), width=10
        )
        boton_dividir.grid(row=0, column=3, padx=1, pady=1)

        # Fila 1
        boton_7 = tk.Button(
            botones_frame, text="7", command=lambda: self._evento_click(7), width=10
        )
        boton_7.grid(row=1, column=0, sticky="nswe", padx=1,pady=1)
        boton_8 = tk.Button(
            botones_frame, text="8", command=lambda: self._evento_click(8), width=10
        )
        boton_8.grid(row=1, column=1, sticky="nswe", padx=1, pady=1)
        boton_9 = tk.Button(
            botones_frame, text="9", command=lambda: self._evento_click(9), width=10
        )
        boton_9.grid(row=1, column=2, sticky="nswe", padx=1, pady=1)
        boton_multiplicar = tk.Button(
            botones_frame, text="*", command=lambda: self._evento_click("*"), width=10
        )
        boton_multiplicar.grid(row=1, column=3, sticky="nswe", padx=1, pady=1)

        # Fila 2
        boton_4 = tk.Button(
            botones_frame, text="4", command=lambda: self._evento_click(4), width=10
        )
        boton_4.grid(row=2, column=0, padx=1,pady=1)
        boton_5 = tk.Button(
            botones_frame, text="5", command=lambda: self._evento_click(5), width=10,
        )
        boton_5.grid(row=2, column=1, padx=1, pady=1)
        boton_6 = tk.Button(
            botones_frame, text="6", command=lambda: self._evento_click(6), width=10
        )
        boton_6.grid(row=2, column=2, padx=1, pady=1)
        boton_restar = tk.Button(
            botones_frame, text="-", command=lambda: self._evento_click("-"), width=10
        )
        boton_restar.grid(row=2, column=3, padx=1, pady=1)

        # Fila 3
        boton_1 = tk.Button(
            botones_frame, text="1", command=lambda: self._evento_click(1), width=10
        )
        boton_1.grid(row=3, column=0, padx=1, pady=1)
        boton_2 = tk.Button(
            botones_frame, text="2", command=lambda: self._evento_click(2), width=10
        )
        boton_2.grid(row=3, column=1, padx=1, pady=1)
        boton_3 = tk.Button(
            botones_frame, text="3", command=lambda: self._evento_click(3), width=10
        )
        boton_3.grid(row=3, column=2, padx=1, pady=1)
        boton_sumar = tk.Button(
            botones_frame, text="+", command=lambda: self._evento_click("+"), width=10
        )
        boton_sumar.grid(row=3, column=3, padx=1, pady=1)

        # Fila 4
        boton_0 = tk.Button(
            botones_frame, text="0", command=lambda: self._evento_click(0), width=21
        )
        boton_0.grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        boton_punto = tk.Button(
            botones_frame, text=".", command=lambda: self._evento_click("."), width=10
        )
        boton_punto.grid(row=4, column=2, padx=1, pady=1)
        boton_sumar = tk.Button(
            botones_frame, text="=", command=lambda: self._evento_evaluar("="), width=10
        )
        boton_sumar.grid(row=4, column=3, padx=1, pady=1)

    def _limpiar(self):
        self.expresion = ''
        self.entrada_texto.get(self.expresion)

    def _evento_click(parametro):
        pass

    def _evento_evaluar(parametro):
        pass


if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
