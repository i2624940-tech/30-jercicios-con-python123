"""IDL3 - Ejercicio 7: factorial de dos números y hasta qué valor coinciden."""

def leer_numero(mensaje, tipo=float, minimo=None, maximo=None):
    """Lee un número validando tipo y rango."""
    while True:
        try:
            valor = tipo(input(mensaje))
        except ValueError:
            print("  Entrada no válida, intenta de nuevo.")
            continue
        if minimo is not None and valor < minimo:
            print(f"  El valor debe ser mayor o igual a {minimo}.")
            continue
        if maximo is not None and valor > maximo:
            print(f"  El valor debe ser menor o igual a {maximo}.")
            continue
        return valor


def expresion(n):
    return "x".join(str(i) for i in range(1, n + 1))


def factorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def main():
    a = leer_numero("Primer número: ", int, 1)
    b = leer_numero("Segundo número: ", int, 1)

    print(f"\n{a}! > {expresion(a)} = {factorial(a)}")
    print(f"{b}! > {expresion(b)} = {factorial(b)}")
    print(f">> son iguales hasta el múltiplo {min(a, b)}")


if __name__ == "__main__":
    main()
