# Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. 
# Anagramas são palavras com os mesmos caracteres rearranjados.

# Digite uma frase: Meu amor mora em Roma e me deu um ramo de flores
# Digite a palavra objetivo: amor 
# Anagramas: ["amor", "mora", "ramo", "Roma"]

frase = "Meu amor mora em Roma e me deu um ramo de flores"
objetivo = sorted("amor")

lst_palavras = frase.lower().split(" ")
for palavra in lst_palavras:
    if sorted(palavra) == objetivo:
        print(palavra)