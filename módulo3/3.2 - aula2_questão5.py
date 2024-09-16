#gênero, idade, tempo de serviço
genero = input()
idade = int(input())
tempo_de_serviço = int(input())
# A: Para mulheres, ter mais de 60 anos. Para homens, 65.
# B: Ou ter trabalhado pelo menos 30 anos
# C: Ou ter 60 anos  e trabalhado pelo menos 25.
a = (genero == 'fem' and idade >= 60) or \
(genero == 'masc' and idade >= 65)
b = tempo_de_serviço >= 30
c = idade >= 60 and tempo_de_serviço >= 25
pode_aposentar = a or b or c
print(a, b, c, pode_aposentar)