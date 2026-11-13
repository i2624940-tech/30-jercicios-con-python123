"""IDL3 - Ejercicio 1: suma y promedio de pares e impares de 1 a N."""

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


def calcular(n):
    suma_p = suma_i = cant_p = cant_i = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            suma_p += i
            cant_p += 1
        else:
            suma_i += i
            cant_i += 1
    prom_p = suma_p / cant_p if cant_p else 0
    prom_i = suma_i / cant_i if cant_i else 0
    return suma_p, prom_p, suma_i, prom_i


def main():
    n = leer_numero("Valor de N: ", int, 1)
    suma_p, prom_p, suma_i, prom_i = calcular(n)
    print(f"\nPares:   suma = {suma_p}, promedio = {prom_p:.2f}")
    print(f"Impares: suma = {suma_i}, promedio = {prom_i:.2f}")


if __name__ == "__main__":
    main()
