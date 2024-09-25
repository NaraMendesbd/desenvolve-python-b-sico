#  Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. 
# Em seguida imprima na ordem estabelecida: 
# 1 - A lista ordenada, sem modificar a lista original 
# 2 - A lista original 
# 3 - O índice do maior valor da lista
# 4 - O índice do menor valor da lista

import random

aleatório = []
for i in range(20):
    valor = random.randint(-100, 100)
    aleatório.append(valor)

print(sorted(aleatório))
print(aleatório)
print("O índice do maior valor é: ",
      aleatório.index(max(aleatório)))
print("O índice do menor valor é: ",
      aleatório.index(min(aleatório)))