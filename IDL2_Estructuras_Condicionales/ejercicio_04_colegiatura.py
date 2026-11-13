"""IDL2 - Ejercicio 4: colegiatura con descuento por promedio >= 18.
Descuento: 50% sobre la mitad de los cursos.
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
    materias = leer_numero("Número de materias que cursa: ", int, 1)
    promedio = leer_numero("Promedio del último periodo (0-20): ", float, 0, 20)

    costo_materia = 100
    total = materias * costo_materia

    if promedio >= 18:
        mitad = materias / 2
        descuento = mitad * costo_materia * 0.50
        pagar = total - descuento
        print(f"Colegiatura sin descuento: S/ {total:.2f}")
        print(f"Descuento aplicado:        S/ {descuento:.2f}")
    else:
        pagar = total
        print("No aplica descuento.")
    print(f"Total a pagar:             S/ {pagar:.2f}")


if __name__ == "__main__":
    main()
