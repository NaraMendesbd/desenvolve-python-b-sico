# Crie uma lista de listas (uma matriz de 2 dimensões) de tamanho n X n com n dado pelo usuário. 
# Cada elemento da matriz deve ser o produto dos índices da linha pela coluna.

# Exemplo:

# Digite n: 4
# Matriz:
# [[0, 0, 0, 0],
#  [0, 1, 2, 3],
#  [0, 2, 4, 6],
#  [0, 3, 6, 9]]

# Solicita o valor de n ao usuário
n = int(input("Digite o valor de n: "))

# Cria a matriz usando compreensão de listas
matriz = [[i * j for j in range(n)] for i in range(n)]

# Exibe a matriz
print("Matriz:")
for linha in matriz:
    print(linha)