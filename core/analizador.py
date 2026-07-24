from pathlib import Path

def analizar_carpeta(ruta):
    carpeta = Path(ruta)

    archivos = 0
    carpetas = 0

    for elemento in carpeta.iterdir():
        if elemento.is_file():
            archivos += 1
        elif elemento.is_dir():
            carpetas += 1

    return {
        "ruta": carpeta.resolve(),
        "archivos": archivos,
        "carpetas": carpetas
    }