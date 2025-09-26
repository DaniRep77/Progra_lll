print("------------------------------------------------")
print("Lista")
print("------------------------------------------------")

# solicitar un numero final de la lista
num1 = int(input("Ingresar un numero hasta 100: "))

# crea la lista desde 1 hasta num1
lista = list(range(1, num1 + 1))

# calcular la suma
resultado = sum(lista)

# imprimir el resultado
print(f"La suma de la Lista hasta {num1} es {resultado}")
