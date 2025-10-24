import tkinter as tk
from tkinter import ttk, messagebox as mb, scrolledtext as st
import mysql.connector


class AlumnosDB:

    def abrir(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="hola_mundo1"
        )

    # INSERTAR
    def insertar(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "INSERT INTO alumnos (StudentID, LastName, FirstName, Address, Phone) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    # CONSULTAR
    def consultar(self, id_alumno):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "SELECT * FROM alumnos WHERE StudentID = %s"
        cursor.execute(sql, (id_alumno,))
        resultado = cursor.fetchall()
        cone.close()
        return resultado

    # ACTUALIZAR
    def actualizar(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = """UPDATE alumnos 
                 SET LastName=%s, FirstName=%s, Address=%s, Phone=%s 
                 WHERE StudentID=%s"""
        cursor.execute(sql, datos)
        cone.commit()
        filas = cursor.rowcount
        cone.close()
        return filas

    # ELIMINAR
    def eliminar(self, id_alumno):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "DELETE FROM alumnos WHERE StudentID = %s"
        cursor.execute(sql, (id_alumno,))
        cone.commit()
        filas = cursor.rowcount
        cone.close()
        return filas

    # MOSTRAR TODOS
    def mostrar_todos(self):
        cone = self.abrir()
        cursor = cone.cursor()
        cursor.execute("SELECT * FROM alumnos")
        registros = cursor.fetchall()
        cone.close()
        return registros


class FormularioAlumnos:
    def __init__(self):
        self.db = AlumnosDB()
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Alumnos - Jumdol")
        self.ventana.geometry("600x500")

        self.cuaderno = ttk.Notebook(self.ventana)
        self.cuaderno.pack(fill="both", expand=True)

        self.frame_insertar = ttk.Frame(self.cuaderno)
        self.frame_consultar = ttk.Frame(self.cuaderno)
        self.frame_actualizar = ttk.Frame(self.cuaderno)
        self.frame_eliminar = ttk.Frame(self.cuaderno)
        self.frame_listar = ttk.Frame(self.cuaderno)

        self.cuaderno.add(self.frame_insertar, text="Insertar Alumno")
        self.cuaderno.add(self.frame_consultar, text="Consultar Alumno")
        self.cuaderno.add(self.frame_actualizar, text="Actualizar Alumno")
        self.cuaderno.add(self.frame_eliminar, text="Eliminar Alumno")
        self.cuaderno.add(self.frame_listar, text="Listado General")

        self.form_insertar()
        self.form_consultar()
        self.form_actualizar()
        self.form_eliminar()
        self.form_listar()

        self.ventana.mainloop()

    # INSERTAR
    def form_insertar(self):
        self.id_student = tk.StringVar()
        self.last = tk.StringVar()
        self.first = tk.StringVar()
        self.address = tk.StringVar()
        self.phone = tk.StringVar()

        ttk.Label(self.frame_insertar, text="ID del Alumno:").grid(column=0, row=0, padx=10, pady=10, sticky="w")
        ttk.Entry(self.frame_insertar, textvariable=self.id_student).grid(column=1, row=0)

        ttk.Label(self.frame_insertar, text="Apellido:").grid(column=0, row=1, padx=10, pady=10, sticky="w")
        ttk.Entry(self.frame_insertar, textvariable=self.last).grid(column=1, row=1)

        ttk.Label(self.frame_insertar, text="Nombre:").grid(column=0, row=2, padx=10, pady=10, sticky="w")
        ttk.Entry(self.frame_insertar, textvariable=self.first).grid(column=1, row=2)

        ttk.Label(self.frame_insertar, text="Dirección:").grid(column=0, row=3, padx=10, pady=10, sticky="w")
        ttk.Entry(self.frame_insertar, textvariable=self.address).grid(column=1, row=3)

        ttk.Label(self.frame_insertar, text="Teléfono:").grid(column=0, row=4, padx=10, pady=10, sticky="w")
        ttk.Entry(self.frame_insertar, textvariable=self.phone).grid(column=1, row=4)

        ttk.Button(self.frame_insertar, text="Guardar", command=self.insertar_alumno).grid(column=1, row=5, pady=10)

    def insertar_alumno(self):
        datos = (self.id_student.get(), self.last.get(), self.first.get(), self.address.get(), self.phone.get())
        try:
            self.db.insertar(datos)
            mb.showinfo("Éxito", "Alumno insertado correctamente.")
            self.id_student.set("")
            self.last.set("")
            self.first.set("")
            self.address.set("")
            self.phone.set("")
        except Exception as e:
            mb.showerror("Error", f"No se pudo insertar.\n{e}")

    # CONSULTAR
    def form_consultar(self):
        self.id_consulta = tk.StringVar()
        ttk.Label(self.frame_consultar, text="ID del Alumno:").grid(column=0, row=0, padx=10, pady=10)
        ttk.Entry(self.frame_consultar, textvariable=self.id_consulta).grid(column=1, row=0)
        ttk.Button(self.frame_consultar, text="Consultar", command=self.consultar_alumno).grid(column=1, row=1, pady=10)
        self.txt_resultado = st.ScrolledText(self.frame_consultar, width=60, height=15)
        self.txt_resultado.grid(column=0, row=2, columnspan=2, pady=10)

    def consultar_alumno(self):
        registros = self.db.consultar(self.id_consulta.get())
        self.txt_resultado.delete("1.0", tk.END)
        if registros:
            for fila in registros:
                self.txt_resultado.insert(tk.END, f"ID: {fila[0]}\nApellido: {fila[1]}\nNombre: {fila[2]}\nDirección: {fila[3]}\nTeléfono: {fila[4]}\n\n")
        else:
            mb.showinfo("Sin resultados", "No se encontró el alumno.")

    # ACTUALIZAR
    def form_actualizar(self):
        self.id_upd = tk.StringVar()
        self.last_upd = tk.StringVar()
        self.first_upd = tk.StringVar()
        self.address_upd = tk.StringVar()
        self.phone_upd = tk.StringVar()

        labels = ["ID:", "Apellido:", "Nombre:", "Dirección:", "Teléfono:"]
        variables = [self.id_upd, self.last_upd, self.first_upd, self.address_upd, self.phone_upd]

        for i, lbl in enumerate(labels):
            ttk.Label(self.frame_actualizar, text=lbl).grid(column=0, row=i, padx=10, pady=10, sticky="w")
            ttk.Entry(self.frame_actualizar, textvariable=variables[i]).grid(column=1, row=i)

        ttk.Button(self.frame_actualizar, text="Actualizar", command=self.actualizar_alumno).grid(column=1, row=6, pady=10)

    def actualizar_alumno(self):
        datos = (self.last_upd.get(), self.first_upd.get(), self.address_upd.get(), self.phone_upd.get(), self.id_upd.get())
        filas = self.db.actualizar(datos)
        if filas > 0:
            mb.showinfo("Éxito", "Alumno actualizado correctamente.")
        else:
            mb.showwarning("Aviso", "No se encontró el alumno.")

    # ELIMINAR
    def form_eliminar(self):
        self.id_del = tk.StringVar()
        ttk.Label(self.frame_eliminar, text="ID del Alumno:").grid(column=0, row=0, padx=10, pady=10)
        ttk.Entry(self.frame_eliminar, textvariable=self.id_del).grid(column=1, row=0)
        ttk.Button(self.frame_eliminar, text="Eliminar", command=self.eliminar_alumno).grid(column=1, row=1, pady=10)

    def eliminar_alumno(self):
        filas = self.db.eliminar(self.id_del.get())
        if filas > 0:
            mb.showinfo("Éxito", "Alumno eliminado correctamente.")
        else:
            mb.showwarning("Aviso", "No se encontró el alumno.")

    # LISTAR TODOS
    def form_listar(self):
        ttk.Button(self.frame_listar, text="Mostrar Todos", command=self.mostrar_todos).pack(pady=10)
        self.txt_listado = st.ScrolledText(self.frame_listar, width=80, height=20)
        self.txt_listado.pack(pady=10)

    def mostrar_todos(self):
        registros = self.db.mostrar_todos()
        self.txt_listado.delete("1.0", tk.END)
        if registros:
            for fila in registros:
                self.txt_listado.insert(tk.END, f"ID: {fila[0]} | {fila[1]}, {fila[2]} | {fila[3]} | {fila[4]}\n")
        else:
            self.txt_listado.insert(tk.END, "No hay alumnos registrados.\n")


if __name__ == "__main__":
    FormularioAlumnos()
