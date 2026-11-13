"""IDL2 - Ejercicio 7: pago de una llamada.
Tarifas por minuto: 1-5 -> S/ 1.00 | 6-8 -> S/ 0.80 | 9-10 -> S/ 0.70 | 11 en adelante -> S/ 0.50
Impuesto: 3% si es domingo; 5% si es domingo en turno nocturno.
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
    minutos = leer_numero("Duración de la llamada (minutos): ", int, 1)
    domingo = input("¿La llamada fue en domingo? (s/n): ").strip().lower() == "s"
    nocturno = False
    if domingo:
        nocturno = input("¿Fue en turno nocturno? (s/n): ").strip().lower() == "s"

    tramo1 = min(minutos, 5)                    # minutos 1 a 5
    tramo2 = min(max(minutos - 5, 0), 3)        # minutos 6 a 8
    tramo3 = min(max(minutos - 8, 0), 2)        # minutos 9 a 10
    tramo4 = max(minutos - 10, 0)               # minutos 11 en adelante

    costo1 = tramo1 * 1.00
    costo2 = tramo2 * 0.80
    costo3 = tramo3 * 0.70
    costo4 = tramo4 * 0.50
    subtotal = costo1 + costo2 + costo3 + costo4

    if domingo and nocturno:
        tasa = 0.05
    elif domingo:
        tasa = 0.03
    else:
        tasa = 0.0
    impuesto = subtotal * tasa
    total = subtotal + impuesto

    print("\n--- Detalle ---")
    print(f"Primeros 5 min ({tramo1} x 1.00): S/ {costo1:.2f}")
    print(f"Siguientes 3 min ({tramo2} x 0.80): S/ {costo2:.2f}")
    print(f"Siguientes 2 min ({tramo3} x 0.70): S/ {costo3:.2f}")
    print(f"Desde el min 11 ({tramo4} x 0.50): S/ {costo4:.2f}")
    print(f"Subtotal: S/ {subtotal:.2f}")
    print(f"Impuesto ({tasa * 100:.0f}%): S/ {impuesto:.2f}")
    print(f"TOTAL A PAGAR: S/ {total:.2f}")


if __name__ == "__main__":
    main()
