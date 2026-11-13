"""IDL3 - Ejercicio 8: estadísticas de los asistentes a una fiesta."""

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
    total = hombres = mujeres = 0
    suma_h = suma_m = 0
    menor = mayor = None

    while True:
        sexo = ""
        while sexo not in ("H", "M"):
            sexo = input("Sexo (H = hombre, M = mujer): ").strip().upper()
        edad = leer_numero("Edad: ", int, 0, 120)

        total += 1
        if sexo == "H":
            hombres += 1
            suma_h += edad
        else:
            mujeres += 1
            suma_m += edad

        if menor is None or edad < menor:
            menor = edad
        if mayor is None or edad > mayor:
            mayor = edad

        if input("¿Registrar a otra persona? (s/n): ").strip().lower() != "s":
            break
        print()

    print(f"\nAsistentes: {total}")
    print(f"Hombres: {hombres} | Mujeres: {mujeres}")
    print(f"Promedio de edad de hombres: {suma_h / hombres:.2f}" if hombres
          else "Promedio de edad de hombres: no hubo hombres")
    print(f"Promedio de edad de mujeres: {suma_m / mujeres:.2f}" if mujeres
          else "Promedio de edad de mujeres: no hubo mujeres")
    print(f"Menor edad: {menor} años")
    print(f"Mayor edad: {mayor} años")


if __name__ == "__main__":
    main()
