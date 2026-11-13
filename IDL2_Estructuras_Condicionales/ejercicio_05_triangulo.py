"""IDL2 - Ejercicio 5: clasificación de un triángulo por sus lados."""
import math

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
    a = leer_numero("Lado 1: ", float, 0.0001)
    b = leer_numero("Lado 2: ", float, 0.0001)
    c = leer_numero("Lado 3: ", float, 0.0001)

    # Desigualdad triangular: cada lado debe ser menor que la suma de los otros dos
    if a + b <= c or a + c <= b or b + c <= a:
        print("Con esos lados NO se puede formar un triángulo.")
        return

    if a == b == c:
        print("Triángulo EQUILÁTERO")
        print(f"Perímetro: {a + b + c:.2f}")
    elif a == b or a == c or b == c:
        print("Triángulo ISÓSCELES")
        if a == b and b != c:
            print("Lados iguales: lado 1 y lado 2")
        elif a == c:
            print("Lados iguales: lado 1 y lado 3")
        else:
            print("Lados iguales: lado 2 y lado 3")
    else:
        print("Triángulo ESCALENO")
        s = (a + b + c) / 2                                # semiperímetro
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # fórmula de Herón
        print(f"Área: {area:.2f}")


if __name__ == "__main__":
    main()
