import os
import torch
import librosa as lb
from torch.utils.data import Dataset, DataLoader

class AcordesDataset(Dataset):
    def __init__(self, carpeta_audios, max_frames=130):
        self.carpeta = carpeta_audios
        self.max_frames = max_frames

        # .wav
        self.archivos = [f for f in os.listdir(carpeta_audios) if f.endswith('.wav')]
        
    def __len__(self):
        return len(self.archivos)
    
    def __getitem__(self, idx):
        ruta_completa = os.path.join(self.carpeta, self.archivos[idx])
        
        
        y, sr = lb.load(ruta_completa)
        S = lb.feature.chroma_cqt(y=y, sr=sr)
        
        # Estandarizar el ancho
        S_fijo = lb.util.fix_length(S, size=self.max_frames, axis=1)
        
        # 0 = Do Mayor, 1 = Sol Mayor
        etiqueta = 0 if "c major" in self.archivos[idx].lower() else 1
        
        # Convertir a Tensor de PyTorch 
        tensor_S = torch.tensor(S_fijo, dtype=torch.float32).unsqueeze(0)
        tensor_etiqueta = torch.tensor(etiqueta, dtype=torch.long)
        
        return tensor_S, tensor_etiqueta

if __name__ == "__main__":
    
    # Instanciar dataset
    dataset = AcordesDataset(carpeta_audios="./media/", max_frames=130)
    

    if len(dataset) > 0:
        tensor_audio, etiqueta = dataset[0]
        print(f"Archivo procesado: {dataset.archivos[0]}")
        print(f"Forma del tensor: {tensor_audio.shape}")
        print(f"Res: {etiqueta} (0=Do, 1=Sol)")
    else:
        print("No se encontraron archivos .wav en la carpeta.")