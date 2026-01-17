import torch
import numpy as np
from torch import nn

class LineNetwork(nn.Module): #Importa modelo do torch
    def __init__(self): #Inicialização
        super().__init__()
        self.layers = nn.Sequential( #Faz a conta
            nn.Linear(1, 1)
        )

    #Como a rede computa
    def forward(self, x): #O x é o dado que entra
        return self.layers(x) #O x entra dentro da conta, (x * pesos + bias)
    
from torch.utils.data import Dataset, DataLoader
import torch.distributions.uniform as urand #Criar numeros aleatorios de forma uniforme

class AlgebraDataset(Dataset):
    def __init__(self, f, interval, nsamples):
        X = urand.Uniform(interval[0], interval[1]).sample(nsamples) #Cria numeros aleatorios onde todos 
        #Onde todos tem chance igual de ir, o intervalo a pessoa vai passar, o sample é quantidade desses numeros
        #o nsamples é a pessoa que passa se quer por exemplo 10 dados,
        #Uniform = todos numeros tem chances iguais de cair

        self.data = [(x, f(x)) for x in X] #a pessoa passa a formula que é o f, o x menor é um dos dados acima
        #que fora aleatorizados

    def __len__(self):
        return len(self.data) #Quantidade de dados
    
    def __getitem__(self, indice):
        return self.data[indice] #Retorna dado especifico por indice
    
reta = lambda x: 2*x + 3
intervalo = (-10, 10)
numero_amostras = 1000 
teste_numero_amostras = 100

train_dataset = AlgebraDataset(reta, intervalo, numero_amostras)
teste_train_dataset = AlgebraDataset(reta, intervalo, teste_numero_amostras)

train_dataloader = DataLoader(train_dataset,batch_size= numero_amostras, shuffle=True)
teste_train_dataloader = DataLoader(teste_train_dataset,batch_size= teste_numero_amostras, shuffle=True)

funcao_distancia = nn.MSELoss() #Função de perda, erro quadratico metrico

device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)

model = LineNetwork().to(device)

#SGD = Stochastic  Gradient Descent
# Ajusta os pesos e o bias usando o gradiente
# para fazer o erro diminuir a cada passo
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)
#lr = taxa de aprendizado

def treinar(model,dataloader, funcao_distancia, optmizer):
    model.train()

    for X, y in dataloader:
        X = X.to(device)
        y = y.to(device)