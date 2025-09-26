# Mini Calculadora

print("=== Mini Calculadora ===")
print("Opciones disponibles:")
print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")

operacion = input("¿Qué operación deseas realizar? (suma, resta, multiplicacion, division): ")

# Ahora pedimos los números después de elegir la operación
x = float(input("Ingrese num1: "))
y = float(input("Ingrese num2: "))

if operacion == "suma":
    print("Resultado:", x + y)
elif operacion == "resta":
    print("Resultado:", x - y)
elif operacion == "multiplicacion":
    print("Resultado:", x * y)
elif operacion == "division":
    if y != 0:
        print("Resultado:", x / y)
    else:
        print("Error: no se puede dividir entre cero")
else:
    print("No existe esa operación en mi código")
