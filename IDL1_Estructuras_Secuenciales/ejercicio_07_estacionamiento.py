"""IDL1 - Ejercicio 7: cobro de estacionamiento.
Interpretación: S/ 5.00 por cada hora completa + S/ 0.10 por cada minuto restante.
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
    horas = leer_numero("Horas completas: ", int, 0)
    minutos = leer_numero("Minutos restantes (0-59): ", int, 0, 59)

    cobro_horas = horas * 5.00
    cobro_minutos = minutos * 0.10
    total = cobro_horas + cobro_minutos

    print(f"\nPor horas:   S/ {cobro_horas:.2f}")
    print(f"Por minutos: S/ {cobro_minutos:.2f}")
    print(f"TOTAL:       S/ {total:.2f}")


if __name__ == "__main__":
    main()
