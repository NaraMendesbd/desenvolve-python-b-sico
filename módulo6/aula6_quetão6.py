# Dada uma lista aleatória, escreva um programa que separa os valores em listas menores de acordo com o tamanho solicitado. 
# Caso não seja possível repartir igualmente a lista original, a última sublista deve conter os elementos remanescentes, 
# como indicado no exemplo a seguir. 
# Note que seu programa deve continuar executando em um laço infinito até que o usuário informe o tamanho 0 na entrada solicitada.

# Lista original:
# [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]

# Tamanho para divisão: 3 
# Subslistas:
# [[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]

# Tamanho para divisão: 4 
# Subslistas: [[12, 45, 23, 67], [78, 90, 45, 32], [100, 76, 38, 62], [73, 29, 83]]

# Tamanho para divisão: 0
# import random
# lista = [random.randint(1,100) for i in range(20)]

import random
lista = [random.randint(1, 100) for i in range(20)]

def dividir_lista(lista, tamanho):
    sublistas = []
    for i in range(0, len(lista), tamanho):
        sublistas.append(lista[i:i + tamanho])  
    return sublistas

# Lista original
lista = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]

while True:
    # Solicita o tamanho para a divisão
    tamanho = int(input("Tamanho para divisão: "))
    
    # Verifica se o usuário deseja sair
    if tamanho == 0:
        print("Programa encerrado.")
        break
    
    if tamanho > 0:        
        sublistas = dividir_lista(lista, tamanho) 
      
        print(f"Sublistas: {sublistas}")
   