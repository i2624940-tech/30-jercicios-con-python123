"""IDL1 - Ejercicio 1: velocidad final de un auto (v = v0 + a*t)."""

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
    v0_kmh = 0.0        # velocidad inicial (km/h)
    a = 0.8             # aceleración (m/s²)
    t = 30              # tiempo (s)

    v0 = v0_kmh / 3.6   # km/h -> m/s
    vf = v0 + a * t     # m/s
    vf_kmh = vf * 3.6   # m/s -> km/h

    print(f"Velocidad final: {vf:.2f} m/s")
    print(f"Velocidad final: {vf_kmh:.2f} km/h")


if __name__ == "__main__":
    main()
