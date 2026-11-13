"""IDL3 - Ejercicio 2: clasificar 10 números (pares, impares, positivos, neutros, negativos)."""

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
    pares = impares = positivos = neutros = negativos = 0
    for i in range(1, 11):
        num = leer_numero(f"Número {i}: ", int)
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
        if num > 0:
            positivos += 1
        elif num == 0:
            neutros += 1
        else:
            negativos += 1

    print(f"\nPares:     {pares}")
    print(f"Impares:   {impares}")
    print(f"Positivos: {positivos}")
    print(f"Neutros:   {neutros}")
    print(f"Negativos: {negativos}")


if __name__ == "__main__":
    main()
