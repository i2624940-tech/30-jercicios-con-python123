"""IDL1 - Ejercicio 9: pago con descuento y cambio."""

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
    monto = leer_numero("Monto base (S/): ", float, 0)
    porcentaje = leer_numero("Porcentaje de descuento (%): ", float, 0, 100)

    descuento = monto * porcentaje / 100
    a_pagar = monto - descuento

    print(f"\nDescuento:  S/ {descuento:.2f}")
    print(f"A pagar:    S/ {a_pagar:.2f}")

    pago = leer_numero("¿Con cuánto dinero paga el cliente? (S/): ", float, a_pagar)
    cambio = pago - a_pagar
    print(f"Cambio:     S/ {cambio:.2f}")


if __name__ == "__main__":
    main()
