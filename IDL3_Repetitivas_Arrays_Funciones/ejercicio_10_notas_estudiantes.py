"""IDL3 - Ejercicio 10: estadísticas de notas de N estudiantes (5 a 20)."""

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


NOTA_APROBATORIA = 13


def leer_notas(n):
    notas = []
    for i in range(n):
        notas.append(leer_numero(f"Nota del alumno {i + 1} (0-20): ", int, 0, 20))
    return notas


def analizar(notas):
    mayor = max(notas)
    menor = min(notas)
    n = len(notas)
    aprobados = sum(1 for x in notas if x >= NOTA_APROBATORIA)
    return {
        "mayor": mayor,
        "menor": menor,
        "cant_mayor": notas.count(mayor),
        "cant_menor": notas.count(menor),
        "promedio": sum(notas) / n,
        "pares": sum(1 for x in notas if x % 2 == 0),
        "impares": sum(1 for x in notas if x % 2 != 0),
        "aprobados": aprobados,
        "desaprobados": n - aprobados,
        "pct_aprobados": aprobados / n * 100,
        "pct_desaprobados": (n - aprobados) / n * 100,
    }


def main():
    n = leer_numero("Número de estudiantes (5 a 20): ", int, 5, 20)
    notas = leer_notas(n)
    r = analizar(notas)

    print("\n--- RESULTADOS ---")
    print(f"a) Mayor nota:                    {r['mayor']}")
    print(f"b) Menor nota:                    {r['menor']}")
    print(f"c) Alumnos con la mayor nota:     {r['cant_mayor']}")
    print(f"d) Alumnos con la menor nota:     {r['cant_menor']}")
    print(f"e) Promedio del salón:            {r['promedio']:.2f}")
    print(f"f) Notas pares:                   {r['pares']}")
    print(f"g) Notas impares:                 {r['impares']}")
    print(f"h) Aprobados (>= 13):             {r['aprobados']}")
    print(f"i) Desaprobados:                  {r['desaprobados']}")
    print(f"j) % de aprobados:                {r['pct_aprobados']:.2f} %")
    print(f"k) % de desaprobados:             {r['pct_desaprobados']:.2f} %")


if __name__ == "__main__":
    main()
