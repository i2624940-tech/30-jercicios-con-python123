"""IDL2 - Ejercicio 2: menor y mayor de tres números."""

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
    a = leer_numero("Primer número: ")
    b = leer_numero("Segundo número: ")
    c = leer_numero("Tercer número: ")

    if a >= b and a >= c:
        mayor = a
    elif b >= a and b >= c:
        mayor = b
    else:
        mayor = c

    if a <= b and a <= c:
        menor = a
    elif b <= a and b <= c:
        menor = b
    else:
        menor = c

    print(f"Mayor: {mayor}")
    print(f"Menor: {menor}")


if __name__ == "__main__":
    main()
