"""IDL2 - Ejercicio 1: total a pagar en una llantera."""

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
    llantas = leer_numero("Cantidad de llantas: ", int, 1)

    if llantas < 5:
        precio = 150
    else:
        precio = 120

    total = llantas * precio
    print(f"Precio por llanta: S/ {precio}")
    print(f"Total a pagar:     S/ {total:.2f}")


if __name__ == "__main__":
    main()
