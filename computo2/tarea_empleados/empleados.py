import mysql.connector

class empleados:

    # ======================
    # CONEXIÓN A LA BASE DE DATOS
    # ======================
    def abrir(self):
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="empleados"
        )
        return conexion

    # ======================
    # INSERTAR REGISTRO
    # ======================
    def alta(self, datos):
        """
        datos = (empleado_id, nombre, apellido_paterno, apellido_materno, email, fecha_contrato, notas)
        """
        cone = self.abrir()
        cursor = cone.cursor()
        sql = """INSERT INTO empleados
                 (empleado_id, nombre, apellido_paterno, apellido_materno, email, fecha_contrato, notas)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    # ======================
    # CONSULTAR UN EMPLEADO POR ID
    # ======================
    def consulta(self, datos):
        """
        datos = (empleado_id,)
        """
        cone = self.abrir()
        cursor = cone.cursor()
        sql = """SELECT empleado_id, nombre, apellido_paterno, apellido_materno, email, fecha_contrato, notas
                 FROM empleados
                 WHERE empleado_id = %s"""
        cursor.execute(sql, datos)
        resultado = cursor.fetchall()
        cone.close()
        return resultado

    # ======================
    # RECUPERAR TODOS LOS EMPLEADOS
    # ======================
    def recuperar_todos(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = """SELECT empleado_id, nombre, apellido_paterno, apellido_materno, email, fecha_contrato, notas
                 FROM empleados"""
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cone.close()
        return resultados

    # ======================
    # ELIMINAR EMPLEADO
    # ======================
    def baja(self, datos):
        """
        datos = (empleado_id,)
        """
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "DELETE FROM empleados WHERE empleado_id = %s"
        cursor.execute(sql, datos)
        cone.commit()
        filas_borradas = cursor.rowcount
        cone.close()
        return filas_borradas  # cantidad de filas borradas

    # ======================
    # MODIFICAR DATOS DE UN EMPLEADO
    # ======================
    def modificacion(self, datos):
        """
        datos = (nombre, apellido_paterno, apellido_materno, email, fecha_contrato, notas, empleado_id)
        """
        cone = self.abrir()
        cursor = cone.cursor()
        sql = """UPDATE empleados
                 SET nombre = %s,
                     apellido_paterno = %s,
                     apellido_materno = %s,
                     email = %s,
                     fecha_contrato = %s,
                     notas = %s
                 WHERE empleado_id = %s"""
        cursor.execute(sql, datos)
        cone.commit()
        filas_modificadas = cursor.rowcount
        cone.close()
        return filas_modificadas  # cantidad de filas modificadas
