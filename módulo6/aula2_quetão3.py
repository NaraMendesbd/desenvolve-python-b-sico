# Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. 
# Crie uma terceira lista chamada interseccao contendo apenas os valores que se repetem nas duas listas. Ao final imprima:
# 1 - Ambas as listas
# 2 - A lista intersecção ordenada
# 3 - A quantidade de vezes que cada elemento aparece em cada lista

import random

lista1, lista2 = [], []
for i in range(20):
    lista1.append(random.randint(0, 50))
    lista2.append(random.randint(0, 50))

print(sorted(lista1))
print(sorted(lista2))

inters = []

for elemento in lista1:
    if elemento in lista2 and elemento not in inters:
        inters.append(elemento)
inters.sort()
for i in inters:
    print(f"{i}: ({lista1.count(i)}, {lista2.count(i)})")

