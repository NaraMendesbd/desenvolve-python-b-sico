# Você está desenvolvendo um programa para determinar o vencedor de um jogo da velha. Escreva uma função avalia_tabuleiro() 
# que recebe uma lista representando o estado atual do tabuleiro e determina se há um vencedor.
# A lista terá 3 sublistas, cada uma representando uma linha do tabuleiro. 
# Cada elemento das sublistas pode ser 'X', 'O' ou vazio (' ').
# O programa deve imprimir o vencedor ('X', 'O'), se houver um, ou "Empate" se não houver vencedor. 
# Um vencedor é determinado se houver três 'X' ou três 'O' em linha (horizontal, vertical ou diagonal).

# Exemplo:
# tabuleiro = [
#   ['X', 'O', 'X'],
#   [' ', 'X', 'O'],
#   ['O', ' ', 'O']
# ]
# O resultado seria "Empate", pois não há um vencedor no exemplo fornecido.

# Exemplo 2:
# tabuleiro = [
#   ['O', 'X', 'O'],
#   ['X', 'O', 'X'],
#   ['X', ' ', 'O']
# ] 
# O resultado seria "O", pois 'O' venceu na diagonal central.

# teste a função nos seguintes tabuleiros

# tabuleiro1 = [
#   ['X', 'O', 'X'],
#   [' ', 'X', 'O'],
#   ['O', ' ', 'X']
#  ]

# tabuleiro2 = [
#  ['X', 'O', 'O'],
#  ['X', 'X', 'O'],
#   ['X', 'O', 'X']
#  ]

# tabuleiro3 = [
#  [' ', ' ', ' '],
#   ['X', ' ', 'O'],
#   ['O', 'X', 'X']
#  ]

# tabuleiro4 = [
#   ['O', 'O', 'O'],
#   ['X', ' ', 'X'],
#  ['O', 'X', 'X']
#  ]

# tabuleiro5 = [
#  ['X', 'X', 'O'],
#   ['X', ' ', 'O'],
#   ['O', 'O', 'X']
#  ]

def avalia_tabuleiro(tabuleiro):    
# Verifica se há vitória nas linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != ' ':
            return linha[0]

# Verifica se há vitória nas colunas
    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] and tabuleiro[0][col] != ' ':
            return tabuleiro[0][col]

# Verifica se há vitória nas diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != ' ':
        return tabuleiro[0][2]

# Verifica se há empate (nenhum espaço vazio)
    for linha in tabuleiro:
        if ' ' in linha:
            return "Empate"

    return "Empate" 

# Testando a função

tabuleiro1 = [
    ['X', 'O', 'X'],
    [' ', 'X', 'O'],
    ['O', ' ', 'X']
]

tabuleiro2 = [
    ['X', 'O', 'O'],
    ['X', 'X', 'O'],
    ['X', 'O', 'X']
]

tabuleiro3 = [
    [' ', ' ', ' '],
    ['X', ' ', 'O'],
    ['O', 'X', 'X']
]

tabuleiro4 = [
    ['O', 'O', 'O'],
    ['X', ' ', 'X'],
    ['O', 'X', 'X']
]

tabuleiro5 = [
    ['X', 'X', 'O'],
    ['X', ' ', 'O'],
    ['O', 'O', 'X']
]

print(f"Resultado Tabuleiro 1: {avalia_tabuleiro(tabuleiro1)}")  
print(f"Resultado Tabuleiro 2: {avalia_tabuleiro(tabuleiro2)}")  
print(f"Resultado Tabuleiro 3: {avalia_tabuleiro(tabuleiro3)}")  
print(f"Resultado Tabuleiro 4: {avalia_tabuleiro(tabuleiro4)}")  
print(f"Resultado Tabuleiro 5: {avalia_tabuleiro(tabuleiro5)}")  