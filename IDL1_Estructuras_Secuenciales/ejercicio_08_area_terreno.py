"""IDL1 - Ejercicio 8: área del terreno de forma A.
Forma A = rectángulo (B x C) + triángulo (base B, altura A - C).
"""

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
    a = leer_numero("Lado A (lado izquierdo, el más alto): ", float, 0)
    b = leer_numero("Lado B (base): ", float, 0)
    c = leer_numero("Lado C (lado derecho, el más bajo): ", float, 0, a)

    area_rectangulo = b * c
    area_triangulo = b * (a - c) / 2
    area_total = area_rectangulo + area_triangulo

    print(f"\nÁrea del rectángulo: {area_rectangulo:.2f}")
    print(f"Área del triángulo:  {area_triangulo:.2f}")
    print(f"ÁREA TOTAL:          {area_total:.2f}")


if __name__ == "__main__":
    main()
