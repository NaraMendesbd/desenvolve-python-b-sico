# Vamos fazer o jogo da forca! Antes de programar crie e salve os seguintes arquivos na mesma pasta onde você vai programar a solução: 
# Crie um arquivo no seu computador chamado "gabarito_forca.txt" com uma lista de 10 palavras de sua escolha 
# (separadas por quebras de linha, "\n"). Essas serão as opções de palavra do jogo.
# Baixe o arquivo "gabarito_enforcado.txt": 
# https://github.com/camilalaranjeira/python-basico-exercicios/blob/main/modulo7/gabarito_enforcado.txt
# Escreva um programa em Python para executar o jogo, de acordo com as definições:
# Abra o arquivo "gabarito_forca.txt" e escolha aleatoriamente uma palavra;
# Com o arquivo "gabarito_enforcado.txt", crie uma lista de strings com os estágios do enforcado;
# No início exiba o número de letras da palavra sorteada como underscores;
# Permita que o jogador insira letras para adivinhar a palavra;
# Em caso de acerto, mostre o progresso do jogador substituindo os underscores correspondentes à letra digitada;
# Em caso de erro, crie a função "imprime_enforcado()" que recebe um inteiro indicando o número de erros do jogador 
# e imprime o enforcado correspondente;
# Limite o número de tentativas para 6 (as partes do enforcado).


import random
def imprime_enforcado(tentativas):
    with open("gabarito_forca.txt", "r") as f:
        enforcado = f.read().splitlines()

    inicio = (6 - tentativas) * 7
    for linha in enforcado[inicio:inicio + 7]:
        print(linha)


def jogo_da_forca():
    # Lendo palavras do arquivo
    with open("gabarito_forca.txt", "r") as fp:
        palavras = fp.read().splitlines()
    
    # Escolhendo uma palavra aleatória
    palavra = random.choice(palavras)
    letras_adivinhadas = []
    tentativas = 6
    acertos = False

    print("Bem-vindo ao jogo da Forca!")
    print("A palavra tem {} letras.".format(len(palavra)))
    
    while not acertos and tentativas > 0:
        # Mostra o progresso
        progresso = ''.join([letra if letra in letras_adivinhadas else '_' for letra in palavra])
        print(progresso)

        # Pede para o jogador inserir uma letra
        tentativa = input("Digite uma letra: ").lower()

        if tentativa in letras_adivinhadas:
            print("Você já tentou essa letra.")
            continue

        letras_adivinhadas.append(tentativa)

        if tentativa in palavra:
            print("Você acertou uma letra!")
        else:
            tentativas -= 1
            print("Letra errada.")
            imprime_enforcado(tentativas)

        # Verifica se a palavra foi adivinhada
        acertos = all(letra in letras_adivinhadas for letra in palavra)

    if acertos:
        print("Parabéns! Você adivinhou a palavra: {}".format(palavra))
    else:
        print("Você perdeu! A palavra era: {}".format(palavra))

# Iniciar o jogo
jogo_da_forca()
