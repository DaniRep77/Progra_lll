import tkinter as tk
from tkinter import ttk, messagebox as mb, scrolledtext as st
from empleados import empleados
import mysql.connector
import datetime


class empleados:

    # ======================
    # CONEXIÓN A LA BASE DE DATOS
    # ======================
    def abrir(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="empleados"
        )

    # ======================
    # INSERTAR REGISTRO
    # ======================
    def alta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = """INSERT INTO empleados (empleado_id, nombre, apellido_paterno, apellido_materno, email, fecha_contrato, notas)
                 VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    # ======================
    # CONSULTAR REGISTRO POR ID
    # ======================
    def consulta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "SELECT * FROM empleados WHERE empleado_id = %s"
        cursor.execute(sql, datos)
        registros = cursor.fetchall()
        cone.close()
        return registros

    # ======================
    # MODIFICAR REGISTRO
    # ======================
    def modificacion(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = """UPDATE empleados
                 SET nombre=%s, apellido_paterno=%s, apellido_materno=%s,
                     email=%s, fecha_contrato=%s, notas=%s
                 WHERE empleado_id=%s"""
        cursor.execute(sql, datos)
        cone.commit()
        filas = cursor.rowcount
        cone.close()
        return filas

    # ======================
    # ELIMINAR REGISTRO
    # ======================
    def baja(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "DELETE FROM empleados WHERE empleado_id = %s"
        cursor.execute(sql, datos)
        cone.commit()
        filas = cursor.rowcount
        cone.close()
        return filas

    # ======================
    # MOSTRAR TODOS LOS REGISTROS
    # ======================
    def recuperar_todos(self):
        cone = self.abrir()
        cursor = cone.cursor()
        cursor.execute("SELECT * FROM empleados")
        registros = cursor.fetchall()
        cone.close()
        return registros



class FormularioEmpleados:
    def __init__(self):
        self.emp = empleados()
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Empleados")
        self.ventana.geometry("600x500")
        self.ventana.configure(bg="#F0F4F8")

        self.cuaderno = ttk.Notebook(self.ventana)
        self.cuaderno.pack(fill="both", expand=True)

        # Pestañas
        self.frame_alta = ttk.Frame(self.cuaderno)
        self.frame_consulta = ttk.Frame(self.cuaderno)
        self.frame_listado = ttk.Frame(self.cuaderno)
        self.frame_modificacion = ttk.Frame(self.cuaderno)
        self.frame_baja = ttk.Frame(self.cuaderno)

        self.cuaderno.add(self.frame_alta, text="Registrar Empleado")
        self.cuaderno.add(self.frame_consulta, text="Consultar Empleado")
        self.cuaderno.add(self.frame_modificacion, text="Modificar Empleado")
        self.cuaderno.add(self.frame_baja, text="Eliminar Empleado")
        self.cuaderno.add(self.frame_listado, text="Listado General de Empleados")

        self.form_alta()
        self.form_consulta()
        self.form_modificacion()
        self.form_baja()
        self.form_listado()

        self.ventana.mainloop()

    # ======================
    # FORMULARIO DE ALTA
    # ======================
    def form_alta(self):
        self.id = tk.StringVar()
        self.nombre = tk.StringVar()
        self.apellido_p = tk.StringVar()
        self.apellido_m = tk.StringVar()
        self.email = tk.StringVar()
        self.fecha = tk.StringVar()

        ttk.Label(self.frame_alta, text="Empleado ID:").grid(column=0, row=0, padx=10, pady=10, sticky="w")
        ttk.Entry(self.frame_alta, textvariable=self.id).grid(column=1, row=0)

        ttk.Label(self.frame_alta, text="Nombre:").grid(column=0, row=1, padx=10, pady=10, sticky="w")
        ttk.Entry(self.frame_alta, textvariable=self.nombre).grid(column=1, row=1)

        ttk.Label(self.frame_alta, text="Apellido Paterno:").grid(column=0, row=2, padx=10, pady=10, sticky="w")
        ttk.Entry(self.frame_alta, textvariable=self.apellido_p).grid(column=1, row=2)

        ttk.Label(self.frame_alta, text="Apellido Materno:").grid(column=0, row=3, padx=10, pady=10, sticky="w")
        ttk.Entry(self.frame_alta, textvariable=self.apellido_m).grid(column=1, row=3)

        ttk.Label(self.frame_alta, text="Email:").grid(column=0, row=4, padx=10, pady=10, sticky="w")
        ttk.Entry(self.frame_alta, textvariable=self.email).grid(column=1, row=4)

        ttk.Label(self.frame_alta, text="Fecha de Contrato (AAAA-MM-DD):").grid(column=0, row=5, padx=10, pady=10, sticky="w")
        ttk.Entry(self.frame_alta, textvariable=self.fecha).grid(column=1, row=5)

        ttk.Label(self.frame_alta, text="Notas:").grid(column=0, row=6, padx=10, pady=10, sticky="w")
        self.txt_notas = st.ScrolledText(self.frame_alta, width=40, height=5)
        self.txt_notas.grid(column=1, row=6, pady=10)

        ttk.Button(self.frame_alta, text="Registrar", command=self.agregar_empleado).grid(column=1, row=7, pady=15)

    def agregar_empleado(self):
        try:
            fecha_str = self.fecha.get().strip()
            fecha_valida = datetime.date.today() if fecha_str == "" else datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()

            datos = (
                self.id.get().strip(),
                self.nombre.get().strip(),
                self.apellido_p.get().strip(),
                self.apellido_m.get().strip(),
                self.email.get().strip(),
                fecha_valida,
                self.txt_notas.get("1.0", tk.END).strip()
            )

            if any(campo == "" for campo in datos[:-1]):
                mb.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
                return

            self.emp.alta(datos)
            mb.showinfo("Éxito", f"Empleado registrado correctamente con fecha {fecha_valida}.")
            self.limpiar_formulario_alta()

        except ValueError:
            mb.showerror("Error de formato", "La fecha debe tener el formato AAAA-MM-DD.")
        except Exception as e:
            mb.showerror("Error", f"No se pudo registrar el empleado.\n{e}")

    def limpiar_formulario_alta(self):
        self.id.set("")
        self.nombre.set("")
        self.apellido_p.set("")
        self.apellido_m.set("")
        self.email.set("")
        self.fecha.set("")
        self.txt_notas.delete("1.0", tk.END)

    # ======================
    # FORMULARIO DE CONSULTA
    # ======================
    def form_consulta(self):
        self.id_consulta = tk.StringVar()

        ttk.Label(self.frame_consulta, text="Empleado ID:").grid(column=0, row=0, padx=10, pady=10)
        ttk.Entry(self.frame_consulta, textvariable=self.id_consulta).grid(column=1, row=0)
        ttk.Button(self.frame_consulta, text="Consultar", command=self.consultar_empleado).grid(column=1, row=1, pady=10)

        self.txt_resultado = st.ScrolledText(self.frame_consulta, width=60, height=15)
        self.txt_resultado.grid(column=0, row=2, columnspan=2, pady=10)

    def consultar_empleado(self):
        datos = (self.id_consulta.get(),)
        registros = self.emp.consulta(datos)
        self.txt_resultado.delete("1.0", tk.END)
        if len(registros) > 0:
            for fila in registros:
                self.txt_resultado.insert(tk.END,
                    f"ID: {fila[0]}\nNombre: {fila[1]} {fila[2]} {fila[3]}\nEmail: {fila[4]}\nFecha Contrato: {fila[5]}\nNotas: {fila[6]}\n\n")
        else:
            mb.showinfo("Sin resultados", "No se encontró ningún empleado con ese ID.")
        self.id_consulta.set("")  # Limpia el campo de ID tras la consulta

    # ======================
    # FORMULARIO DE MODIFICACIÓN
    # ======================
    def form_modificacion(self):
        self.id_mod = tk.StringVar()
        self.nom_mod = tk.StringVar()
        self.ap_p_mod = tk.StringVar()
        self.ap_m_mod = tk.StringVar()
        self.email_mod = tk.StringVar()
        self.fecha_mod = tk.StringVar()

        etiquetas = ["Empleado ID:", "Nombre:", "Apellido Paterno:", "Apellido Materno:", "Email:", "Fecha de Contrato:", "Notas:"]
        for i, texto in enumerate(etiquetas):
            ttk.Label(self.frame_modificacion, text=texto).grid(column=0, row=i, padx=10, pady=10, sticky="w")

        ttk.Entry(self.frame_modificacion, textvariable=self.id_mod).grid(column=1, row=0)
        ttk.Entry(self.frame_modificacion, textvariable=self.nom_mod).grid(column=1, row=1)
        ttk.Entry(self.frame_modificacion, textvariable=self.ap_p_mod).grid(column=1, row=2)
        ttk.Entry(self.frame_modificacion, textvariable=self.ap_m_mod).grid(column=1, row=3)
        ttk.Entry(self.frame_modificacion, textvariable=self.email_mod).grid(column=1, row=4)
        ttk.Entry(self.frame_modificacion, textvariable=self.fecha_mod).grid(column=1, row=5)
        self.txt_notas_mod = st.ScrolledText(self.frame_modificacion, width=40, height=5)
        self.txt_notas_mod.grid(column=1, row=6)
        ttk.Button(self.frame_modificacion, text="Modificar", command=self.modificar_empleado).grid(column=1, row=7, pady=15)

    def modificar_empleado(self):
        datos = (
            self.nom_mod.get(),
            self.ap_p_mod.get(),
            self.ap_m_mod.get(),
            self.email_mod.get(),
            self.fecha_mod.get(),
            self.txt_notas_mod.get("1.0", tk.END).strip(),
            self.id_mod.get()
        )
        try:
            filas = self.emp.modificacion(datos)
            if filas > 0:
                mb.showinfo("Éxito", "Empleado modificado correctamente.")
                self.limpiar_formulario_mod()
            else:
                mb.showwarning("Aviso", "No se encontró el empleado con ese ID.")
        except Exception as e:
            mb.showerror("Error", f"No se pudo modificar el empleado.\n{e}")

    def limpiar_formulario_mod(self):
        self.id_mod.set("")
        self.nom_mod.set("")
        self.ap_p_mod.set("")
        self.ap_m_mod.set("")
        self.email_mod.set("")
        self.fecha_mod.set("")
        self.txt_notas_mod.delete("1.0", tk.END)

    # ======================
    # FORMULARIO DE BAJA
    # ======================
    def form_baja(self):
        self.id_baja = tk.StringVar()
        ttk.Label(self.frame_baja, text="Empleado ID:").grid(column=0, row=0, padx=10, pady=10)
        ttk.Entry(self.frame_baja, textvariable=self.id_baja).grid(column=1, row=0)
        ttk.Button(self.frame_baja, text="Eliminar", command=self.eliminar_empleado).grid(column=1, row=1, pady=10)

    def eliminar_empleado(self):
        datos = (self.id_baja.get(),)
        try:
            filas = self.emp.baja(datos)
            if filas > 0:
                mb.showinfo("Éxito", "Empleado eliminado correctamente.")
                self.limpiar_formulario_baja()
            else:
                mb.showwarning("Aviso", "No se encontró ningún empleado con ese ID.")
        except Exception as e:
            mb.showerror("Error", f"No se pudo eliminar el empleado.\n{e}")

    def limpiar_formulario_baja(self):
        self.id_baja.set("")

    # ======================
    # LISTADO GENERAL
    # ======================
    def form_listado(self):
        ttk.Button(self.frame_listado, text="Actualizar Listado", command=self.mostrar_todos).pack(pady=10)
        self.txt_listado = st.ScrolledText(self.frame_listado, width=80, height=25)
        self.txt_listado.pack(pady=10)

    def mostrar_todos(self):
        registros = self.emp.recuperar_todos()
        self.txt_listado.delete("1.0", tk.END)
        if len(registros) > 0:
            for fila in registros:
                self.txt_listado.insert(
                    tk.END,
                    f"ID: {fila[0]} | {fila[1]} {fila[2]} {fila[3]} | Email: {fila[4]} | Fecha: {fila[5]}\nNotas: {fila[6]}\n{'-'*80}\n"
                )
        else:
            self.txt_listado.insert(tk.END, "No hay empleados registrados.\n")


if __name__ == "__main__":
    FormularioEmpleados()
