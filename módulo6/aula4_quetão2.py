#  Solicite uma frase do usuário e usando compreensão de listas imprima:
# A lista de vogais da frase, ordenada alfabeticamente
# A lista de consoantes da frase
# Exemplo:
# Digite uma frase: Eu gosto de programar em Python
# Vogais: ['a', 'a', 'e', 'e', 'o', 'o', 'o', 'o', 'u']
# Consoantes: ['E', 'g', 's', 't', 'd', 'p', 'r', 'g', 'r', 'm', 'r', 'm', 'P', 'y', 't', 'h', 'n']

# Solicitar uma frase do usuário
frase = input("Digite uma frase: ")

# Definir as vogais
vogais = "aeiouAEIOU"

# Lista de vogais na frase, ordenada alfabeticamente
lista_vogais = sorted([letra for letra in frase if letra in vogais])
print(f"Vogais: {lista_vogais}")

# Lista de consoantes na frase
lista_consoantes = [letra for letra in frase if letra.isalpha() and letra not in vogais]
print(f"Consoantes: {lista_consoantes}")