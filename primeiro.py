#Fazer um neuronio aprender y = 2x + 3

#Ideia simples -> chute =  peso . x + bias

import math
import random

dados = [
    (1, 5),
    (2, 7),
    (3, 9),
    (4, 11)
]

peso = random.uniform(-1, 1)
bias = random.uniform(-1, 1)
taxa_aprendizagem = 0.01 #Quanto que vai mudar depois de cada tentativa, quanto menor mais demora mais menos explode ;)

for i in range(1000):
    for x, y in dados:
        chute = peso * x + bias
        
        erro = y - chute

        peso += erro * x * taxa_aprendizagem #Multiplica o X porque na formula o peso é multiplicado pelo X
        bias += erro * taxa_aprendizagem
    if i % 10 == 0:
        print(f"Número: {i}\nPesos: {peso}\nBias: {bias}\nErro: {erro}")
        print(f"Chute: {chute}\nValor Real: {y}")
        print("-=" * 10)

while True:
    numero_pessoa = int(input("Digite o seu X: "))
    print(f"-=" * 20)
    print(f"X: {numero_pessoa}\nResposta: {peso * numero_pessoa + bias}")