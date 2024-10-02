# Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" (link a seguir) e salve em seu computador com o nome "estomago.txt". 
# Link: https://aplauso.imprensaoficial.com.br/edicoes/12.0.813.502/12.0.813.502.txt
# Em seguida crie um script em Python que abra o arquivo para leitura e imprima: 
# O texto das primeiras 25 linhas
# O número de linhas do arquivo
# A linha com maior número de caracteres
# O número de menções aos nomes dos personagens "Nonato" e "Íria" 
# (inclua todas as variações de maiúsculas e minúsculas e atenção para não incluir a substring "iria" 
# se ela fizer parte de outras palavras).

import re

# Nome do arquivo
arquivo_roteiro = "estomago.txt"

# Inicializando variáveis
linhas = []
nonato_count = 0
iria_count = 0

# Lê o arquivo e processa as informações
with open(arquivo_roteiro, 'r') as arquivo:
    for linha in arquivo:
        linhas.append(linha.strip())

# Impressão das primeiras 25 linhas
print("Primeiras 25 linhas do roteiro:")
for i in range(min(25, len(linhas))):
    print(linhas[i])

# Número total de linhas do arquivo
numero_de_linhas = len(linhas)
print(f"\nNúmero de linhas do arquivo: {numero_de_linhas}")

# A linha com maior número de caracteres
linha_maior = max(linhas, key=len)
print(f"\nLinha com maior número de caracteres: {linha_maior}")

# Contando menções aos personagens "Nonato" e "Íria"
for linha in linhas:
    nonato_count += len(re.findall(r'\bNonato\b', linha, re.IGNORECASE))
    iria_count += len(re.findall(r'\bÍria\b', linha, re.IGNORECASE))

# Impressão dos resultados
print(f"\nNúmero de menções a 'Nonato': {nonato_count}")
print(f"Número de menções a 'Íria': {iria_count}")