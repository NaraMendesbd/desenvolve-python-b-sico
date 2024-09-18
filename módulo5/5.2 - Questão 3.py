# Crie uma função em Python chamada soma_digitos que recebe um número inteiro como parâmetro e retorna a soma dos seus dígitos. 
# Por exemplo, para o número 123, a função deve retornar 6, (1+2+3).
# O desafio aqui é separar os dígitos de um número inteiro usando operações aritméticas. 
# No programa principal solicite ao usuário que insira um número e utilize a função soma_digitos para calcular 
# e exibir a soma dos seus dígitos.

def soma_digitos(n):
    soma = 0

while (n > 0):

    resto = n % 10
    n = (n - resto)/10
    soma = soma + resto


print("A soma dos números é: ", n)



