print("------------------------------------------------")
print("Dany Antonio")
print("Codigo_USTR027124")
print("------------------------------------------------")
# crear la función
def verificar_numero(num):
    if num > 0:
        return "El número es positivo"
    elif num < 0:
        return "El número es negativo"
    else:
        return "El número es cero"

# solicitar número
num = int(input("Introduce un número: "))

# imprimir el resultado
print(verificar_numero(num))
