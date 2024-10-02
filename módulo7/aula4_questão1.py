# Escreva um script Python que solicita uma frase do usuário e a salve em um arquivo chamado "frase.txt" no mesmo local do seu script. 
# Imprima em seguida o caminho completo do arquivo salvo.
# Ex: 
# Digite uma frase: Bom dia, meu nome é Davi.
# Frase salva em /Users/laranjeira/python-basico/frase.txt

import os

frase = input("Digite uma frase: ")

nome_arquivo = "frase.txt"

# Salva a frase no arquivo
with open(nome_arquivo, 'w') as arquivo:
    arquivo.write(frase)

# Caminho completo do arquivo
caminho_completo = os.path.abspath(nome_arquivo)

# Imprime o caminho completo
print(f"Frase salva em {caminho_completo}")