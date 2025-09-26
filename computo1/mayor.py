# Capturar dos números desde teclado
num1 = int12(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Comparar y mostrar el mayor
if num1 > num2:
    print(f"El número mayor es: {num1}")
elif num2 > num1:
    print(f"El número mayor es: {num2}")
else:
    print("Ambos números son iguales")