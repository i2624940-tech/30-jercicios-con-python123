"""IDL1 - Ejercicio 10: cajero automático con la menor cantidad de billetes/monedas."""

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
    denominaciones = [200, 100, 50, 20, 10, 5, 1]
    monto = leer_numero("Cantidad a retirar (S/, entero): ", int, 1)

    restante = monto
    print(f"\nPara retirar S/ {monto} el cajero entrega:")
    total_piezas = 0
    for d in denominaciones:
        cantidad = restante // d      # cuántas piezas de esta denominación
        restante = restante % d       # lo que aún falta entregar
        if cantidad > 0:
            print(f"  {cantidad} x S/ {d}")
            total_piezas += cantidad
    print(f"Total de piezas entregadas: {total_piezas}")


if __name__ == "__main__":
    main()
