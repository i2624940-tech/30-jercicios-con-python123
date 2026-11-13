"""IDL3 - Ejercicio 3: porcentajes de N números respecto a un número X."""

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
    n = leer_numero("¿Cuántos números vas a ingresar (N)? ", int, 1)
    numeros = []
    for i in range(n):
        numeros.append(leer_numero(f"Número {i + 1}: "))
    x = leer_numero("Número X: ")

    menores = mayores = iguales = entre = ninguna = 0
    for v in numeros:
        cumple = False
        if v < x:
            menores += 1
            cumple = True
        if v > x:
            mayores += 1
            cumple = True
        if v == x:
            iguales += 1
            cumple = True
        if 1 <= v <= x:
            entre += 1
            cumple = True
        if not cumple:
            ninguna += 1

    def pct(c):
        return c / n * 100

    print(f"\nMenores que X:             {pct(menores):.2f} %")
    print(f"Mayores que X:             {pct(mayores):.2f} %")
    print(f"Iguales a X:               {pct(iguales):.2f} %")
    print(f"Entre 1 y X (inclusive):   {pct(entre):.2f} %")
    print(f"No cumplen ninguna:        {pct(ninguna):.2f} %")


if __name__ == "__main__":
    main()
