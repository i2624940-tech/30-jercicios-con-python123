"""IDL3 - Ejercicio 4: máximo y mínimo de una lista de N números en un solo recorrido."""

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


def main():
    n = leer_numero("¿Cuántos números (N)? ", int, 1)

    primero = leer_numero("Número 1: ")
    maximo = minimo = primero
    for i in range(2, n + 1):
        num = leer_numero(f"Número {i}: ")
        if num > maximo:
            maximo = num
        if num < minimo:
            minimo = num

    print(f"\nMáximo: {maximo}")
    print(f"Mínimo: {minimo}")


if __name__ == "__main__":
    main()
