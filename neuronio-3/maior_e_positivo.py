#Criar um codigo, que me fale se um numero é grande e positivo 
import math
import random

#Dados = (numero, [positivo?, grande?])

dados = [
    (-5, [0, 0], 0),
    (-3, [0, 0], 0),
    (-1, [0, 0], 0),
    (1, [1, 0], 0),
    (2, [1, 0], 0),
    (4, [1, 0], 0),
    (5, [1, 0], 0),
    (7, [1, 0], 0),
    (9, [1, 0], 0),
    (10, [1, 1], 1),
    (12, [1, 1], 1),
    (15, [1, 1], 1)
]

peso_1 = random.uniform(-1, 1)
bias_1 = random.uniform(-1, 1)

peso_2 = random.uniform(-1, 1)
bias_2 = random.uniform(-1, 1)

peso_3_1 = random.uniform(-1, 1) #Peso 1 do terceiro, serve para peso dos positivos
peso_3_2 = random.uniform(-1, 1) #Peso 2 do terceiro, serve para peso dos grandes
bias_3 = random.uniform(-1, 1)


taxa_aprendizado = 0.01

def sigmoid(x):
    return 1 / (1 + math.exp(-max(-500, min(500, x))))


#Verificar se é positivo
for i in range(2500):
    for numero, valores, resultado in dados:
        positivo = valores[0]
        chute = numero * peso_1 + bias_1
        probabilidade = sigmoid(chute)

        erro = positivo - probabilidade
        peso_1 += erro * numero * taxa_aprendizado
        bias_1 += erro * taxa_aprendizado

#Verificar se é grande
for i in range(2500):
    for numero, valores, resultado in dados:
        grande = valores[1]
        chute = numero * peso_2 + bias_2
        probabilidade = sigmoid(chute)

        erro = grande - probabilidade
        peso_2 += numero * erro * taxa_aprendizado
        bias_2 += erro * taxa_aprendizado

#Verificar se é Grande e Positivo
for i in range(4000):
    for numero, valores, resultado in dados:
        positivo = numero * peso_1 + bias_1
        positivo = sigmoid(positivo)

        grande = numero * peso_2 + bias_2
        grande = sigmoid(grande)

        chute = (positivo * peso_3_1) + (grande * peso_3_2) + bias_3
        probabilidade = sigmoid(chute)

        erro = resultado - probabilidade
        
        peso_3_1 += erro * positivo * taxa_aprendizado
        peso_3_2 += erro * grande * taxa_aprendizado
        bias_3 += erro * taxa_aprendizado


def verificar_grande_pequeno(n):
    positivo = n * peso_1 + bias_1
    positivo = sigmoid(positivo)

    grande = n * peso_2 + bias_2
    grande = sigmoid(grande)
    chute = (positivo * peso_3_1) + (grande * peso_3_2) + bias_3
    probabilidade = sigmoid(chute)

    return probabilidade

while True:
    numero = int(input("Digite um número: "))
    chance_grande_postivo = verificar_grande_pequeno(numero)
    if chance_grande_postivo >= 0.5:
        resultado = 1
    else:
        resultado = 0
    print(f"O número {numero} é positivo e grande? {resultado}\nChance de ser: {chance_grande_postivo * 100:.2f}%")
