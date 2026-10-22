import torch
import numpy as np
import sys
import argparse
import librosa as lb
import matplotlib.pyplot as plt

# Simulamos la matriz S que devuelve tu función ExtraerCaracteristicas
S_numpy = np.random.rand(12, 130) 

# 1. Convertir el array de NumPy a un Tensor de PyTorch (y asegurar que sea Float32)
tensor = torch.tensor(S_numpy, dtype=torch.float32)
print(f"Forma original: {tensor.shape}") # Salida: torch.Size([12, 130])

# 2. Añadir la dimensión del Canal de color (Channel)
# unsqueeze(0) añade un '1' en la posición 0 de las dimensiones
tensor_cnn = tensor.unsqueeze(0)
print(f"Forma para la CNN: {tensor_cnn.shape}") # Salida: torch.Size([1, 12, 130])