import tkinter as tk
from tkinter import messagebox


def calcular_promedio():
    try:
        lab1 = float(entry_lab1.get())
        lab2 = float(entry_lab2.get())
        parcial = float(entry_parcial.get())

        promedio = (lab1 * 0.30) + (lab2 * 0.30) + (parcial * 0.40)

        resultado = f"Tu promedio final es: {promedio:.2f}\n"
        if promedio >= 6:
            resultado += "✅ ¡Felicidades! Aprobaste el cómputo."
        else:
            resultado += "❌ Necesitas mejorar para aprobar."

        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese solo números válidos.")


# Crear ventana principal
ventana = tk.Tk()
ventana.title("Promedio Cómputo 1")
ventana.geometry("350x280")
ventana.configure(bg="#1e1e2f")  # Fondo oscuro elegante

# Estilos
color_label = "#ffffff"   # blanco
color_entry = "#f0f0f0"   # gris claro
color_boton = "#4CAF50"   # verde
color_texto_boton = "#ffffff"

# Etiquetas y entradas
tk.Label(ventana, text="Nota Lab1 (30%):", bg="#1e1e2f", fg=color_label).pack(pady=5)
entry_lab1 = tk.Entry(ventana, bg=color_entry)
entry_lab1.pack()

tk.Label(ventana, text="Nota Lab2 (30%):", bg="#1e1e2f", fg=color_label).pack(pady=5)
entry_lab2 = tk.Entry(ventana, bg=color_entry)
entry_lab2.pack()

tk.Label(ventana, text="Nota Parcial (40%):", bg="#1e1e2f", fg=color_label).pack(pady=5)
entry_parcial = tk.Entry(ventana, bg=color_entry)
entry_parcial.pack()

# Botón para calcular
tk.Button(
    ventana,
    text="Calcular Promedio",
    command=calcular_promedio,
    bg=color_boton,
    fg=color_texto_boton,
    activebackground="#45a049",  # color al presionar
    relief="flat",
    padx=10,
    pady=5
).pack(pady=15)

# Iniciar la ventana
ventana.mainloop()
