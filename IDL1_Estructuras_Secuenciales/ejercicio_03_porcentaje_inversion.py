"""IDL1 - Ejercicio 3: porcentaje invertido por cada socio."""

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
    i1 = leer_numero("Inversión de la persona 1 (S/): ", float, 0)
    i2 = leer_numero("Inversión de la persona 2 (S/): ", float, 0)
    i3 = leer_numero("Inversión de la persona 3 (S/): ", float, 0)

    total = i1 + i2 + i3
    if total == 0:
        print("El total invertido es 0; no se pueden calcular porcentajes.")
        return

    print(f"\nTotal invertido: S/ {total:.2f}")
    print(f"Persona 1: {i1 / total * 100:.2f} %")
    print(f"Persona 2: {i2 / total * 100:.2f} %")
    print(f"Persona 3: {i3 / total * 100:.2f} %")


if __name__ == "__main__":
    main()
