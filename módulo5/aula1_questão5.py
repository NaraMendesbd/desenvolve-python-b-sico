# Você está trabalhando em um sistema de mensagens instantâneas, que deve permitir o uso de emojis nas conversas entre pessoas. Faça:
# No terminal, instale a biblioteca emoji usando o gerenciador de pacotes pip
# $ pip install emoji
# Conheça a função emoji.emojize()
#Seu programa deve apresentar para o usuário a lista de emojis disponíveis com o texto correspondente a cada emoji.
# Em seguida, solicite uma frase codificada ao usuário e apresente ela decodificada com a visualização de emojis (emojizada).
#A seguir um exemplo de interação, com uma lista de emojis sugeridos. 
# Você pode consultar o texto que codifica outros emojis indo nessa página e passando o mouse por cima do emoji desejado. 
# Emojis disponíveis:
# ❤️ - :red_heart:
# 👍 - :thumbs_up:
# 🤔 - :thinking_face:
# 🥳 - :partying_face:
# Digite uma frase e ela será emojizada:
# Olá mundo! :red_heart:
# Frase emojizada:
# Olá mundo! ❤️   

import emoji

lista_emoji = {
    ":grinning_face:": emoji.emojize(":grinning_face:"),  # Rosto sorridente 😀
    ":thumbs_up:": emoji.emojize(":thumbs_up:"),  # Polegar para cima 👍
    ":red_heart:": emoji.emojize(":red_heart:"),  # Coração vermelho ❤️
    ":fire:": emoji.emojize(":fire:"),  # Fogo 🔥
    ":clapping_hands:": emoji.emojize(":clapping_hands:"),  # Mãos batendo palmas 👏
}

print("Lista de Emojis Disponíveis:")
for codigo, emoji_visual in lista_emoji.items():
    print(f"{codigo}: {emoji_visual}")

frase_codificada = input("Digite uma frase codificada com emojis: ")

for codigo, emoji_visual in lista_emoji.items():
    frase_codificada = frase_codificada.replace(codigo, emoji_visual)

print(f"Frase com emojis: {frase_codificada}")


