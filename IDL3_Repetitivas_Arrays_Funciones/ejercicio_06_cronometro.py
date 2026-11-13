"""IDL3 - Ejercicio 6: cronómetro hh:mm:ss (referencial)."""
import time

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


def formatear(segundos):
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = segundos % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def main():
    limite = leer_numero("¿Hasta cuántos segundos quieres contar? ", int, 1)
    pausa = leer_numero("Pausa entre segundos (1 = tiempo real; 0.01 = demo rápida): ",
                        float, 0)
    print("Presiona Ctrl+C para detener.\n")
    try:
        for seg in range(limite + 1):
            print(f"\r{formatear(seg)}", end="", flush=True)
            time.sleep(pausa)
    except KeyboardInterrupt:
        pass
    print("\nCronómetro detenido.")


if __name__ == "__main__":
    main()
