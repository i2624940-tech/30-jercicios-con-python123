"""IDL2 - Ejercicio 8: ordenar tres enteros diferentes (ascendente o descendente)."""

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
    while True:
        a = leer_numero("Primer entero: ", int)
        b = leer_numero("Segundo entero: ", int)
        c = leer_numero("Tercer entero: ", int)
        if a != b and a != c and b != c:
            break
        print("  Los tres números deben ser diferentes. Ingrésalos de nuevo.\n")

    orden = ""
    while orden not in ("A", "D"):
        orden = input("¿Orden? (A = ascendente, D = descendente): ").strip().upper()

    # Se obtiene el menor, el mayor y el del medio con comparaciones
    mayor = max(a, b, c)
    menor = min(a, b, c)
    medio = a + b + c - mayor - menor

    if orden == "A":
        print(f"Orden ascendente: {menor}, {medio}, {mayor}")
    else:
        print(f"Orden descendente: {mayor}, {medio}, {menor}")


if __name__ == "__main__":
    main()
