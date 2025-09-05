import tkinter as tk
from tkinter import messagebox
from datetime import date

def calcular_edad():
    try:
        dia, mes, anio = map(int, entry_fecha.get().split("/"))
        hoy = date.today()
        nacimiento = date(anio, mes, dia)

        # diferencia de años y meses
        edad_anios = hoy.year - nacimiento.year
        edad_meses = hoy.month - nacimiento.month

        if hoy.day < nacimiento.day:
            edad_meses -= 1  # si no ha cumplido día del mes, restar un mes

        if edad_meses < 0:
            edad_anios -= 1
            edad_meses += 12

        if edad_anios < 0:
            messagebox.showerror("Error", "La fecha ingresada no es válida.")
        else:
            messagebox.showinfo("Resultado", f"Tienes {edad_anios} años y {edad_meses} meses.")
    except:
        messagebox.showerror("Error", "Formato incorrecto. Usa DD/MM/AAAA")

# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Edad")
ventana.geometry("350x180")
ventana.configure(bg="#1e1e2f")

# Estilos
tk.Label(ventana, text="Introduce tu fecha de nacimiento (DD/MM/AAAA):",
         bg="#1e1e2f", fg="white", font=("Arial", 11)).pack(pady=10)

entry_fecha = tk.Entry(ventana, font=("Arial", 12), bg="#f0f0f0")
entry_fecha.pack(pady=5)

tk.Button(ventana, text="Calcular Edad", command=calcular_edad,
          bg="#4CAF50", fg="white", font=("Arial", 12, "bold"),
          relief="flat", padx=10, pady=5).pack(pady=15)

ventana.mainloop()
