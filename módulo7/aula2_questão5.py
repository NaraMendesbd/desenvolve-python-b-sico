# De acordo com uma pesquisa do linguista Matt Davis, o cérebro humano consegue ler palavras com as letras embaralhadas, 
# contanto que a primeira e a última letra estejam no lugar correto. 
# Implemente uma função chamada embaralhar_palavras() para ajudar a testar a hipótese do Matt Davis. 
# Sua função vai receber uma frase, embaralhar as letras internas de cada palavra e retornar a frase modificada.
#  Dica: use a biblioteca random.
# Complete o seguinte código:
# def embaralhar_palavras(frase):
    #### Escreva a função
# Exemplo de uso:
# frase = "Python é uma linguagem de programação"
# resultado = embaralhar_palavras(frase)
# print(resultado)
# Possível saída: "Ptohyn é uma lignaugem de prarmoagãço"

import random

def embaralhar_palavras(frase):
# Dividir a frase em palavras
    palavras = frase.split()  
    nova_frase = []

    for palavra in palavras:
# Só embaralha palavras com mais de 3 letras
        if len(palavra) > 3:  
            meio = list(palavra[1:-1])  
            random.shuffle(meio) 
            palavra_embaralhada = palavra[0] + ''.join(meio) + palavra[-1] 
        else:
            palavra_embaralhada = palavra 
        nova_frase.append(palavra_embaralhada)

    return ' '.join(nova_frase)  

# Exemplo de uso
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)