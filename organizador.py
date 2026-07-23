#!/usr/bin/env python3
from pathlib import Path

def seleccionar_carpeta():
    ruta = input("¿Qué carpeta quieres organizar?")
    carpeta = Path(ruta)

    if carpeta.exists() and carpeta.is_dir():
        print(f"\n✓ Carpeta encontrada : {carpeta}")
    else:
        print("\n✗ La carpeta no existe.")

def main():
    print("=" * 40)
    print("     FILE ORGANIZER v0.2")
    print("=" * 40)
    seleccionar_carpeta()

if __name__ == "__main__":
    main()
