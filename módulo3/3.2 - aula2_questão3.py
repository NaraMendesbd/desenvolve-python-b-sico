#idade, partidas jogadas, jogos vencidos
idade = int(input())
partidas_jogadas = int(input())
jogos_vencidos = int(input())
# a: tiver entre 16 e 18 anos
# b: já tiver jogado pelo menos 3 jogos
# c: já ter vencido pelo menos 1 jogo
a = idade >= 16 and idade <= 18
b = partidas_jogadas >= 3
c = jogos_vencidos >= 1
ingresso_permitido = a and b and c
print(a, b, c, ingresso_permitido)