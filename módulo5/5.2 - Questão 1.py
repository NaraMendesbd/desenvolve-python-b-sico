# Sabendo que o código a seguir calcula o fatorial de n, escreva uma função chamada fatorial() que recebe um inteiro n como parâmetro 
# e retorna o resultado do fatorial de n. 
# No programa principal, peça ao usuário o valor de n, chame a sua função e imprima o retorno.


def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat *= i
    return fat

n = int(input())
meu_fatorial = fatorial(n) 
print(f"{n}! é {meu_fatorial}")