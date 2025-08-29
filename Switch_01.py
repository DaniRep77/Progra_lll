def operan(operator, num1, num2):
    return {
        "suma": lambda: num1 + num2,
        "resta": lambda: num1 - num2,
        "multi": lambda: num1 * num2,
        "divi": lambda: num1 / num2
    }.get(operator, lambda: None)()

resultado = operan("divi", 8, 2)
print(resultado)