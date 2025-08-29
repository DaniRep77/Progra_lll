import tkinter as tk


class Aplication:
    def __init__(self):
        self.valor = 1
        self.ventana01 = tk.Tk()
        self.ventana01.title("botones")
        self.ventana01.geometry("200x100")

        self.label01 = tk.Label(self.ventana01, text=self.valor, font=("Arial", 24))
        self.label01.grid(column=0, row=0, columnspan=3, pady=10)
        self.label01.configure(foreground="blue")

        self.boton_restar = tk.Button(self.ventana01, text="restar", command=self.restar, width=6, height=1)
        self.boton_restar.grid(column=0, row=1, padx=5)

        tk.Label(self.ventana01, text="").grid(column=1, row=1)

        self.boton_sumar = tk.Button(self.ventana01, text="sumar", command=self.sumar, width=6, height=1)
        self.boton_sumar.grid(column=2, row=1, padx=5)

        self.ventana01.mainloop()

    def sumar(self):
        self.valor = self.valor + 1
        self.label01.config(text=self.valor)

    def restar(self):
        self.valor = self.valor - 1
        self.label01.config(text=self.valor)


ejecutar = Aplication()