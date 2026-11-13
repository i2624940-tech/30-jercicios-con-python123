"""IDL3 - Ejercicio 5: ahorro acumulado mes a mes durante 12 meses."""

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
    ahorro = 0.0
    for mes in range(1, 13):
        deposito = leer_numero(f"Depósito del mes {mes} (S/): ", float, 0)
        ahorro += deposito
        print(f"  Ahorro acumulado hasta el mes {mes}: S/ {ahorro:.2f}")

    print(f"\nAHORRO FINAL DE 12 MESES: S/ {ahorro:.2f}")


if __name__ == "__main__":
    main()
