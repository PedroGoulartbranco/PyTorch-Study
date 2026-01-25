#Criar um codigo, que me fale se um numero é grande e positivo 
import math
import random

#Dados = (numero, [positivo?, grande?])

dados = [
    (-5, [0, 0]),
    (-3, [0, 0]),
    (-1, [0, 0]),
    (1, [1, 0]),
    (2, [1, 0]),
    (4, [1, 0]),
    (5, [1, 0]),
    (7, [1, 0]),
    (9, [1, 0]),
    (10, [1, 1]),
    (12, [1, 1])
]

peso_1 = random.uniform(-1, 1)
bias_1 = random.uniform(-1, 1)

peso_2 = random.uniform(-1, 1)
bias_2 = random.uniform(-1, 1)

peso_3_1 = random.uniform(-1, 1) #Peso 1 do terceiro, serve para peso dos positivos
bias_3_1 = random.uniform(-1, 1) #Bias 1 do terceiro, serve para ser o bias dos positivos

peso_3_1 = random.uniform(-1, 1) #Peso 2 do terceiro, serve para peso dos grandes
bias_3_1 = random.uniform(-1, 1) #Bias 2 do terceiro, serve para ser o bias dos grandes

taxa_aprendizado = 0.01

def sigmoid(x):
    return 1 / (1 + math.exp(-max(-500, min(500, x))))


#Verificar se é positivo
for i in range(2500):
    for numero, valores in dados:
        positivo = valores[0]
        chute = numero * peso_1 + bias_1
        probabilidade = sigmoid(chute)

        erro = positivo - probabilidade
        peso_1 += erro * numero * taxa_aprendizado
        bias_1 += erro * taxa_aprendizado

#Verificar se é grande
for i in range(2500):
    for numero, valores in dados:
        grande = valores[1]
        chute = numero * peso_2 + bias_2
        probabilidade = sigmoid(chute)

        erro = grande - probabilidade
        peso_2 += numero * erro * taxa_aprendizado
        bias_2 += erro * taxa_aprendizado

#Verificar se é Grande e Positivo
for i in range(4000):
    for numero, valores in dados:
        positivo = numero * peso_1 + bias_1
        positivo = sigmoid(positivo)

        grande = numero * peso_2 + bias_2
        grande = sigmoid(grande)

        chute = numero * peso_3 + bias_3

