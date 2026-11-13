"""IDL2 - Ejercicio 9: compra de N camisas con descuento por cantidad."""

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
    n = leer_numero("Cantidad de camisas: ", int, 1)
    precio = leer_numero("Precio de cada camisa (S/): ", float, 0)

    compra = n * precio

    if 1 <= n <= 4:
        tasa = 0.125
    elif 5 <= n <= 8:
        tasa = 0.20
    else:
        tasa = 0.315

    descuento = compra * tasa
    final = compra - descuento

    print(f"\nCompra sin descuento: S/ {compra:.2f}")
    print(f"Descuento ({tasa * 100:.1f}%):  S/ {descuento:.2f}")
    print(f"Compra con descuento: S/ {final:.2f}")


if __name__ == "__main__":
    main()
