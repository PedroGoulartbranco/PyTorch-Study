#Ensinar pra ia oque é um número grande, para minha logica

import math 
import random

dados = [
    (0, 0),
    (1, 0),
    (3, 0),
    (6, 0),
    (8, 0),
    (10, 1),
    (11, 1),
    (13, 1),
    (15, 1)
]

pesos = random.uniform(-1, 1)
bias = random.uniform(-1, 1)
taxa_aprendizado = 0.01

def relu(x):
    return max(0, x)


for i in range(1000):
    for numero, binario in dados:
        chute = pesos * numero + bias
        ativacao = relu(chute)

        erro = binario - ativacao

        pesos += erro * numero * taxa_aprendizado
        bias += erro * taxa_aprendizado
    
    if (i % 10 == 0):
        print(f"Número: {numero}\nChute: {ativacao}")


teste = int(input("Digite um número: "))
print(f"Maior ou menor: {pesos * teste + bias}")