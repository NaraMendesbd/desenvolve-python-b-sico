# Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", 
# removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha. 
# Ao final, imprima o conteúdo do arquivo "palavras.txt". 
# Ex: 
# Bom 
# dia 
# meu 
# nome 
# é 
# Davi

import re

# Nome dos arquivos
arquivo_frase = "frase.txt"
arquivo_palavras = "palavras.txt"

# Lê a frase do arquivo
with open(arquivo_frase, 'r') as fp:
    conteudo = fp.read()

# Remover espaços em branco e caracteres não alfabéticos
    palavras = re.findall(r'\b\w+\b', conteudo)

# Salvando em um novo arquivo
with open(arquivo_palavras, 'w', encoding='utf-8') as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + '\n')

# Imprime o conteúdo do arquivo "palavras.txt"
print("Conteúdo do arquivo 'palavras.txt':")
with open(arquivo_palavras, 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)