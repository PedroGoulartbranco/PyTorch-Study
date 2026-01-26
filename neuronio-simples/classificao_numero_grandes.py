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

def sigmoid(x):
    #O uso do max e min é para nao ficar gigante os números, se passar de -500 por exe -1000 fica -500 e se passar de 500 fica 500
    return 1 / (1 + math.exp(-max(-500, min(500, x))))


for i in range(2000):
    for numero, binario in dados:
        chute = pesos * numero + bias
        probabilidade = sigmoid(chute)

        erro = binario - probabilidade

        pesos += erro * numero * taxa_aprendizado
        bias += erro * taxa_aprendizado
    
        if (i % 10 == 0):
            print(f"Número: {numero}\nChute: {probabilidade * 100:.1f}%")

def pequeno_grande(numero):
    formula = pesos * numero + bias
    numero = sigmoid(formula)
    return (numero * 100)

contador = 0

while True:
    contador += 1
    numero = int(input("Digite um número: "))
    print(f"{numero} é grande ? {pequeno_grande(numero):.1f}% de ser grande")
    print("-=" * 20)
    if contador % 5 == 0:
        sair = str(input("Sair ? [S/N] ")).upper()
        if sair == "S":
            break