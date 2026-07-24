#!/usr/bin/env python3
from pathlib import Path
from core.analizador import analizar_carpeta


def seleccionar_carpeta():
    ruta = input("¿Qué carpeta quieres organizar? ")
    carpeta = Path(ruta)

    if carpeta.exists() and carpeta.is_dir():
        datos = analizar_carpeta(ruta)

        print("\n--------------------------------------")
        print(f"Ruta................ {datos['ruta']}")
        print(f"Archivos............ {datos['archivos']}")
        print(f"Subcarpetas......... {datos['carpetas']}")

        print("\nTipos de archivo encontrados:")

        for extension, cantidad in sorted(datos["extensiones"].items()):
            print(f"{extension:<15} {cantidad}")

        print("--------------------------------------")

    else:
        print("\n✗ La carpeta no existe.")


def main():
    print("=" * 40)
    print("      FILE ORGANIZER v0.5")
    print("=" * 40)

    seleccionar_carpeta()


if __name__ == "__main__":
    main()