"""IDL1 - Ejercicio 6: meses, semanas, días y horas vividos (aproximado)."""

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
    edad = leer_numero("Edad (años): ", int, 0)

    meses = edad * 12
    dias = edad * 365
    semanas = dias // 7
    horas = dias * 24

    print(f"\nCon {edad} años has vivido aproximadamente:")
    print(f"  Meses:   {meses:,}")
    print(f"  Semanas: {semanas:,}")
    print(f"  Días:    {dias:,}")
    print(f"  Horas:   {horas:,}")


if __name__ == "__main__":
    main()
