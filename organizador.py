def seleccionar_carpeta():
    ruta: str = input("¿Qué carpeta quieres organizar?")
    print(f"La carpeta elegida es: {ruta}")
def main():
    print("=" * 40)
    print("     FILE ORGANIZER v0.2")
    print("=" * 40)
    seleccionar_carpeta()
if __name__ == "__main__":
    main()
