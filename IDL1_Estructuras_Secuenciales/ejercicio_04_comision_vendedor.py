"""IDL1 - Ejercicio 4: sueldo total de un vendedor (sueldo base + 25% de comisión)."""

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
    sueldo_base = leer_numero("Sueldo base (S/): ", float, 0)
    v1 = leer_numero("Venta 1 (S/): ", float, 0)
    v2 = leer_numero("Venta 2 (S/): ", float, 0)
    v3 = leer_numero("Venta 3 (S/): ", float, 0)

    comision = (v1 + v2 + v3) * 0.25
    total = sueldo_base + comision

    print(f"\nComisiones del mes: S/ {comision:.2f}")
    print(f"Total a recibir:    S/ {total:.2f}")


if __name__ == "__main__":
    main()
