import sys
import argparse
import numpy as np
import librosa as lb
import matplotlib.pyplot as plt

def ExtraerCaracteristicas(ruta):
    try:
        y, sr = lb.load(ruta)
    except Exception as e:
        print(f"Error al intentar leer el archivo de audio '{ruta}':\n{e}")
        sys.exit(1)
    
    # Cromagrama
    S = lb.feature.chroma_cqt(y=y, sr=sr)
    return S

def MostrarCromagrama(S, titulo="Cromagrama"):
    fig, ax = plt.subplots(figsize=(10, 4))
    img = lb.display.specshow(S, x_axis="time", y_axis="chroma", ax=ax, cmap='coolwarm')
    fig.colorbar(img, ax=ax)
    plt.title(titulo)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    
    
    parser = argparse.ArgumentParser(description="Extrae y visualiza el cromagrama de un archivo de audio.")
    parser.add_argument("ruta", type=str, help="Ruta al archivo .wav")
    args = parser.parse_args()
    
    # Extraer Cronograma
    matriz_caracteristicas = ExtraerCaracteristicas(args.ruta)
    print(f"Forma de la matriz: {matriz_caracteristicas.shape}")
    
    # Mostrar Cronograma
    MostrarCromagrama(matriz_caracteristicas, titulo=f"Cromagrama de: {args.ruta}")



    