import tkinter as tk


class Aplicacion:
    def __init__(self):
        # formulario
        self.formulario01 = tk.Tk()
        self.formulario01.title("Operaciones")
        self.formulario01.geometry("300x200")

        # etiqueta
        self.label01 = tk.Label(self.formulario01, text="Número:")
        self.label01.grid(column=0, row=0, padx=5, pady=2)

        # caja de texto
        self.dato01 = tk.StringVar()
        self.entry01 = tk.Entry(self.formulario01, width=10, textvariable=self.dato01)
        self.entry01.grid(column=1, row=0, padx=5, pady=2)

        # etiqueta
        self.label02 = tk.Label(self.formulario01, text="Divisor:")
        self.label02.grid(column=0, row=1, padx=5, pady=2)

        # caja de texto
        self.dato02 = tk.StringVar()
        self.entry02 = tk.Entry(self.formulario01, width=10, textvariable=self.dato02)
        self.entry02.grid(column=1, row=1, padx=5, pady=2)

        # botón
        self.boton01 = tk.Button(self.formulario01, text="Calcular", command=self.calcular)
        self.boton01.grid(column=0, row=2, columnspan=2, pady=5)

        # etiqueta p
        self.label03 = tk.Label(self.formulario01, text="Cuadrado:")
        self.label03.grid(column=0, row=3, padx=5, pady=2)

        # etiqueta
        self.label04 = tk.Label(self.formulario01, text="División:")
        self.label04.grid(column=0, row=4, padx=5, pady=2)

        # mainloop
        self.formulario01.mainloop()

    def calcular(self):
        try:
            valor1 = int(self.dato01.get())
            valor2 = int(self.dato02.get())

            cuadrado = valor1 * valor1
            self.label03.configure(text=f"Cuadrado: {cuadrado}")

            if valor2 == 0:
                self.label04.configure(text="División: Error (÷0)")
            else:
                division = valor1 // valor2  # División entera
                self.label04.configure(text=f"División: {division}")

        except ValueError:
            self.label03.configure(text="Cuadrado: Error")
            self.label04.configure(text="División: Ingrese enteros")
        except Exception:
            self.label03.configure(text="Cuadrado: Error")
            self.label04.configure(text="División: Error")


ejecutar = Aplicacion()