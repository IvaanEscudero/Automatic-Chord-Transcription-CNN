import sys
import numpy as np
import librosa as lb
import matplotlib.pyplot as plt

if __name__ == "__main__":
    filename = "./media/c major.wav"

    try:
        y, sr = lb.load(filename)
        
    except Exception as e:
        print(f"Error al intentar leer el archivo de audio:")
        print(f"{e}")
        sys.exit(1)

    S = np.abs(lb.stft(y))
    fig, ax = plt.subplots()
    img = lb.display.specshow(S, vscale="dBFS",x_axis="time", y_axis="log", ax=ax)
    lb.display.colorbar_db(img, label="dBFS")
    
    plt.show()