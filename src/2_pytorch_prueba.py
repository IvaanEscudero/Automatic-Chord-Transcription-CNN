import torch
import librosa as lb

if __name__ == "__main__":
    
    y, sr = lb.load("./media/c major.wav")
    S_numpy = lb.feature.chroma_cqt(y=y, sr=sr)

    
    tensor = torch.tensor(S_numpy, dtype=torch.float32)
    tensor_cnn = tensor.unsqueeze(0)

    print(f"Tensor listo para PyTorch: {tensor_cnn.shape}")