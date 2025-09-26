import os
import tkinter as tk
from tkinter import ttk

# Corrección aquí: __file__ en lugar de file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

main = tk.Tk()
main.title("Controles TTK")
main.config(bg="#2E2E2E")  # fondo gris oscuro
main.geometry("600x400")

contador = tk.IntVar(value=0)  # variable para el número

style = ttk.Style(main)
style.theme_use("clam")

# ===== LABEL =====
style.configure("label.TLabel", background="#2E2E2E", foreground="#FFFFFF", font=("Arial", 16, "bold"))
label = ttk.Label(master=main, textvariable=contador, style="label.TLabel", anchor="center")
label.place(x=271, y=75, width=80, height=40)

# ===== FUNCIONES =====
def aumentar():
    contador.set(contador.get() + 1)

def disminuir():
    contador.set(contador.get() - 1)

def salir():
    main.destroy()

def cambiar_fondo():
    if radio_button_var.get() == 0:
        main.config(bg="#1ABC9C")   # verde azulado
    elif radio_button_var.get() == 1:
        main.config(bg="#E67E22")   # naranja
    elif radio_button_var.get() == 2:
        main.config(bg="#9B59B6")   # morado elegante

# ===== BOTONES =====
style.configure("boton.TButton", font=("Arial", 11, "bold"))

boton_aumentar = ttk.Button(master=main, text="Aumentar", style="boton.TButton", command=aumentar)
boton_aumentar.place(x=271, y=157, width=100, height=40)

boton_disminuir = ttk.Button(master=main, text="Disminuir", style="boton.TButton", command=disminuir)
boton_disminuir.place(x=272, y=216, width=100, height=40)

boton_salir = ttk.Button(master=main, text="Salir", style="boton.TButton", command=salir)
boton_salir.place(x=275, y=288, width=100, height=40)

# ===== RADIO BUTTONS =====
radio_button_var = tk.IntVar()

style.configure("radio_button.TRadiobutton", background="#2E2E2E", foreground="#FFFFFF", font=("Arial", 10))

radio_button_0 = ttk.Radiobutton(
    master=main, variable=radio_button_var, text="Verde Azulado", value=0,
    style="radio_button.TRadiobutton", command=cambiar_fondo
)
radio_button_0.place(x=80, y=136)

radio_button_1 = ttk.Radiobutton(
    master=main, variable=radio_button_var, text="Naranja", value=1,
    style="radio_button.TRadiobutton", command=cambiar_fondo
)
radio_button_1.place(x=80, y=160)

radio_button_2 = ttk.Radiobutton(
    master=main, variable=radio_button_var, text="Morado", value=2,
    style="radio_button.TRadiobutton", command=cambiar_fondo
)
radio_button_2.place(x=80, y=184)

main.mainloop()
