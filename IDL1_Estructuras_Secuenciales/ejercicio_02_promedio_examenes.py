"""IDL1 - Ejercicio 2: promedio de cuatro exámenes con igual ponderación."""

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
    n1 = leer_numero("Nota del examen 1: ")
    n2 = leer_numero("Nota del examen 2: ")
    n3 = leer_numero("Nota del examen 3: ")
    n4 = leer_numero("Nota del examen 4: ")

    promedio = (n1 + n2 + n3 + n4) / 4
    print(f"Promedio de calificaciones: {promedio:.2f}")


if __name__ == "__main__":
    main()
