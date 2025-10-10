import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import articulos

class FormularioArticulos:
    def __init__(self):
        self.articulo1 = articulos.Articulos()
        self.ventana1 = tk.Tk()
        self.ventana1.title("Inventario")
        self.cuaderno1 = ttk.Notebook(self.ventana1)

        # Páginas
        self.carga_articulos()          # Página 1
        self.consulta_por_codigo()      # Página 2
        self.borrado()                  # Página 3
        self.modificar()                # Página 4

        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    # -------------------- Pestaña 1: Insertar --------------------
    def carga_articulos(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Insertar")
        self.labelframe1 = ttk.LabelFrame(self.pagina1, text="Producto")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.label1 = ttk.Label(self.labelframe1, text="Nombre:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.descripcioncarga = tk.StringVar()
        self.entrydescripcion = ttk.Entry(self.labelframe1, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe1, text="Precio:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.preciocarga = tk.StringVar()
        self.entryprecio = ttk.Entry(self.labelframe1, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)

        self.boton1 = ttk.Button(self.labelframe1, text="Guardar", command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def agregar(self):
        datos = (self.descripcioncarga.get(), self.preciocarga.get())
        self.articulo1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.descripcioncarga.set("")
        self.preciocarga.set("")

    # -------------------- Pestaña 2: Consulta por código --------------------
    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")
        self.labelframe2 = ttk.LabelFrame(self.pagina2, text="Artículo")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

        self.label1 = ttk.Label(self.labelframe2, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo = tk.StringVar()
        self.entrycodigo = ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe2, text="Descripción:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcion = tk.StringVar()
        self.entrydescripcion = ttk.Entry(self.labelframe2, textvariable=self.descripcion, state="readonly")
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)

        self.label3 = ttk.Label(self.labelframe2, text="Precio:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.precio = tk.StringVar()
        self.entryprecio = ttk.Entry(self.labelframe2, textvariable=self.precio, state="readonly")
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)

        self.boton1 = ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos = (self.codigo.get(), )
        respuesta = self.articulo1.consulta(datos)
        if len(respuesta) > 0:
            self.descripcion.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
        else:
            self.descripcion.set('')
            self.precio.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")

    # -------------------- Pestaña 3: Borrado --------------------
    def borrado(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Borrado de artículos")
        self.labelframe3 = ttk.LabelFrame(self.pagina3, text="Artículo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)

        self.label1 = ttk.Label(self.labelframe3, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigoborra = tk.StringVar()
        self.entryborra = ttk.Entry(self.labelframe3, textvariable=self.codigoborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)

        self.boton1 = ttk.Button(self.labelframe3, text="Borrar", command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos = (self.codigoborra.get(), )
        cantidad = self.articulo1.baja(datos)
        if cantidad == 1:
            mb.showinfo("Información", "Se borró el artículo con dicho código")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

    # -------------------- Pestaña 4: Modificar --------------------
    def modificar(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Modificar artículo")
        self.labelframe4 = ttk.LabelFrame(self.pagina4, text="Artículo")
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)

        self.label1 = ttk.Label(self.labelframe4, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigomod = tk.StringVar()
        self.entrycodigo = ttk.Entry(self.labelframe4, textvariable=self.codigomod)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)

        self.label2 = ttk.Label(self.labelframe4, text="Descripción:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcionmod = tk.StringVar()
        self.entrydescripcion = ttk.Entry(self.labelframe4, textvariable=self.descripcionmod)
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)

        self.label3 = ttk.Label(self.labelframe4, text="Precio:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.preciomod = tk.StringVar()
        self.entryprecio = ttk.Entry(self.labelframe4, textvariable=self.preciomod)
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)

        self.boton1 = ttk.Button(self.labelframe4, text="Consultar", command=self.consultar_mod)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

        self.boton2 = ttk.Button(self.labelframe4, text="Modificar", command=self.modifica)
        self.boton2.grid(column=1, row=4, padx=4, pady=4)


    def consultar_mod(self):
        datos = (self.codigomod.get(), )
        respuesta = self.articulo1.consulta(datos)
        if len(respuesta) > 0:
            self.descripcionmod.set(respuesta[0][0])
            self.preciomod.set(respuesta[0][1])
        else:
            self.descripcionmod.set('')
            self.preciomod.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def modifica(self):
        datos = (self.descripcionmod.get(), self.preciomod.get(), self.codigomod.get())
        cantidad = self.articulo1.modificacion(datos)
        if cantidad == 1:
            mb.showinfo("Información", "Se modificó el artículo")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")


# -------------------- Ejecutar la aplicación --------------------
aplicacion1 = FormularioArticulos()
