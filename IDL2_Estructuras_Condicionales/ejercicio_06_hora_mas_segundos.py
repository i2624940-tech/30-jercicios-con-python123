"""IDL2 - Ejercicio 6: hora N segundos después."""

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
    hh = leer_numero("Horas (0-23): ", int, 0, 23)
    mm = leer_numero("Minutos (0-59): ", int, 0, 59)
    ss = leer_numero("Segundos (0-59): ", int, 0, 59)
    n = leer_numero("¿Cuántos segundos después? ", int, 0)

    total = hh * 3600 + mm * 60 + ss + n
    dias = total // 86400          # días completos que pasaron
    total = total % 86400          # segundos dentro del día

    h = total // 3600
    m = (total % 3600) // 60
    s = total % 60

    print(f"\nHora inicial: {hh:02d}:{mm:02d}:{ss:02d}")
    print(f"{n} segundos después: {h:02d}:{m:02d}:{s:02d}", end="")
    if dias > 0:
        print(f"  (+{dias} día(s))", end="")
    print()


if __name__ == "__main__":
    main()
