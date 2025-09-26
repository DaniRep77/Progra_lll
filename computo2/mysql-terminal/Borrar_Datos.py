import mysql.connector

# Conexión a la base de datos
conexion1 = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="BD1"
)

cursor1 = conexion1.cursor()

# Mostrar datos actuales
cursor1.execute("SELECT ID, descripcion, precio FROM articulos")
print("Datos actuales en la tabla:")
for datos in cursor1:
    print(datos)

# ======== BORRAR REGISTRO =========
id_borrar = 48
sql = "DELETE FROM articulos WHERE ID = %s"
val = (id_borrar,)
cursor1.execute(sql, val)

# Confirmar cambios
conexion1.commit()
print(f"Se borró el registro con ID = {id_borrar}")

# Verificar datos después de borrar
cursor1.execute("SELECT ID, descripcion, precio FROM articulos")
print("Datos después de borrar:")
for datos in cursor1:
    print(datos)

# Cerrar conexión
conexion1.close()
print("Listo.........")