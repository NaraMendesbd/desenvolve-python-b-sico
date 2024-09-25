# Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada num_elementos. 
# Em seguida gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos, 
# e armazene em uma lista chamada elementos. Em seguida imprima:
# 1 - A lista elementos
# 2 - A soma dos valores da lista
# 3 - A média dos valores da lista

import random

num_elementos = random.randint(5, 20)

elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Imprimir a lista de elementos
print(f"Lista de elementos: {elementos}")

# Soma dos valores da lista
soma = sum(elementos)
print(f"Soma dos valores da lista: {soma}")

# Média dos valores da lista
media = soma / num_elementos
print(f"Média dos valores da lista: {media:.2f}")
