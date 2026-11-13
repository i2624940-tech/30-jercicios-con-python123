"""IDL1 - Ejercicio 5: ganancia en un año con 2% mensual."""

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
    capital = leer_numero("Capital a invertir (S/): ", float, 0)
    tasa = 0.02  # 2% mensual

    # Interés simple: el interés se calcula siempre sobre el capital inicial
    ganancia_simple = capital * tasa * 12
    # Interés compuesto: los intereses se reinvierten cada mes
    ganancia_compuesta = capital * (1 + tasa) ** 12 - capital

    print(f"\nGanancia en 1 año (interés simple):    S/ {ganancia_simple:.2f}")
    print(f"Ganancia en 1 año (interés compuesto): S/ {ganancia_compuesta:.2f}")


if __name__ == "__main__":
    main()
