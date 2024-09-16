# Ler 2 números inetiros N e M e e imprimir na tela um campo de batalha naval.
# O tabuleiro deve possuir N linhas e M colunas. # 
# A primeira linha é composta por um espaço em branco e o cabeçalho das colunas, ou seja, valores de 1 a M. 
# # As N linhas seguintes iniciam com o cabeçalho da linha, ou seja, seu número, seguido de M caracteres "/" (barra) indicando uma possível posição jogável.

N = int(input("Digite o valor de N (número de linhas): "))
M = int(input("Digite o valor de M (número de colunas): "))

# Colunas
print("  ", end="") 
for coluna in range(1, M + 1):
    print(coluna, end=" ")
print() 

# Linhas do campo de batalha
for linha in range(1, N + 1):
    # Cabeçalho da linha
    print(linha, end=" ")
    
    # Imprime as colunas com "/"
    for coluna in range(1, M + 1):
        print("/", end=" ")
    