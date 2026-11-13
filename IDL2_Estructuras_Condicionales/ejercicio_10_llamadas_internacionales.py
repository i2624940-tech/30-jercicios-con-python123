"""IDL2 - Ejercicio 10: costo de llamadas internacionales según zona."""

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
    zonas = {
        10: ("América del Norte", 2.2),
        12: ("América del Centro", 2.5),
        20: ("América del Sur", 1.2),
        22: ("Asia", 3.5),
        30: ("Europa", 3.0),
        32: ("África", 3.24),
    }

    print("Códigos disponibles:")
    for codigo, (nombre, costo) in zonas.items():
        print(f"  {codigo} - {nombre} (S/ {costo} por minuto)")

    codigo = leer_numero("\nClave de la zona: ", int)
    if codigo not in zonas:
        print("Clave de zona no válida.")
        return

    minutos = leer_numero("Minutos hablados: ", float, 0)
    nombre, costo = zonas[codigo]
    total = minutos * costo

    print(f"\nZona: {nombre}")
    print(f"Costo total de la llamada: S/ {total:.2f}")


if __name__ == "__main__":
    main()
