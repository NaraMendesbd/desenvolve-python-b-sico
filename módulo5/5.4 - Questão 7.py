#Escreva um programa que pergunte ao usuário qual operação ele deseja: maior ou menor. 
# Em seguida leia uma quantidade indefinida de valores do usuário, até que o usuário digite o valor zero. 
# Apresente ao final o maior ou menor dos valores digitados de acordo com a escolha do usuário.

# Sua solução deve incluir pelo menos uma função lambda

op = int(input("(1) maior ou (2) menor?"))
if op == 1:
    result = float("-inf")
    op_function = lambda a, b: a > b

else:
    result = float("inf")
    op_function = lambda a, b: a < b

while True:
    x = int(input())
    if x == 0:break

    if op_function (x, result):
        result = x

    print(result)