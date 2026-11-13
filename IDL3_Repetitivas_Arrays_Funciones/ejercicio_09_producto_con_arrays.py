"""IDL3 - Ejercicio 9: producto 100 x 98 x 96 x ... usando un array (lista).
Nota: al bajar de 2 en 2 desde 100 el último factor es 2 (no se llega a 1).
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
    factores = []
    for valor in range(100, 0, -2):     # 100, 98, 96, ..., 4, 2
        factores.append(valor)

    producto = 1
    for f in factores:
        producto *= f

    print("Factores:", " x ".join(str(f) for f in factores))
    print(f"\nCantidad de factores: {len(factores)}")
    print(f"Producto: {producto}")


if __name__ == "__main__":
    main()
