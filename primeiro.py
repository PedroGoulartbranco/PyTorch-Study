import torch
import numpy as np
from torch import nn

class LineNetwork(nn.Module): #Importa modelo do torch
    def __init__(self): #Inicialização
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(1, 1)
        )

    #Como a rede computa
    def forward(self, x): #O x é o dado que entra
        return self.layers(x) #O x entra dentro da conta, (x * pesos + bias)