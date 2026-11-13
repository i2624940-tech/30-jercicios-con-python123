"""IDL2 - Ejercicio 3: ¿debe tributar? (mayor de 18 años e ingresos >= S/ 3000)."""

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
    edad = leer_numero("Edad: ", int, 0)
    ingresos = leer_numero("Ingresos mensuales (S/): ", float, 0)

    if edad > 18 and ingresos >= 3000:
        monto = ingresos * 0.05
        print("El usuario SÍ debe tributar.")
        print(f"Monto a tributar (5%): S/ {monto:.2f}")
    else:
        print("El usuario NO debe tributar.")


if __name__ == "__main__":
    main()
