# Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo 
# (ou seja, lida da mesma forma de trás para frente). 
# Ignore espaços em branco ou sinais de pontuação, e considere maiúsculas e minúsculas da mesma forma. 
# Seu programa deve continuar rodando até que o usuário digite "Fim".Ex:
# Digite uma frase (digite "fim" para encerrar): Radar
# "Radar" é palíndromo
# Digite uma frase (digite "fim" para encerrar): Bom dia!
# "Bom dia!" não é palíndromo
# Digite uma frase (digite "fim" para encerrar): Ame o poema
# "Ame o poema" é palíndromo
# Digite uma frase (digite "fim" para encerrar): A Daniela ama a lei? Nada!
# "A Daniela ama a lei? Nada!" é palíndromo
# Digite uma frase (digite "fim" para encerrar): fim

import string

def eh_palindromo(frase):
   
    frase_limpa = ''.join([c.lower() for c in frase if c.isalnum()])
    
    # Verifica se a frase limpa é igual à sua reversa
    return frase_limpa == frase_limpa[::-1]

# Loop principal do programa
while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    
    # Condição de saída
    if frase.lower() == "fim":
        print("Programa encerrado.")
        break
    
    # Verifica se a frase é palíndromo
    if eh_palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')