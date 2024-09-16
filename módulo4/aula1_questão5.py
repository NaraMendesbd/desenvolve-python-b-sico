# Um instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes. 
# # Escreva um programa que leia um inteiro N com a quantidade de respondentes e em seguida leia as N idades de cada respondente.
#  Ao final, imprima a média das idades.
# respondentes = r
r = int(input())
soma = 0
cont = 0
while cont < r:
    cont += 1
    idade = int(input())
    soma += idade
print(soma)
print(f"A média de idade dos respondentes é: {soma/r} anos")