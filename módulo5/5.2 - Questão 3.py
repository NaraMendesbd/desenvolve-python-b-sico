# Crie uma função em Python chamada soma_digitos que recebe um número inteiro como parâmetro e retorna a soma dos seus dígitos. 
# Por exemplo, para o número 123, a função deve retornar 6, (1+2+3).
# O desafio aqui é separar os dígitos de um número inteiro usando operações aritméticas. 
# No programa principal solicite ao usuário que insira um número e utilize a função soma_digitos para calcular 
# e exibir a soma dos seus dígitos.

def soma_digitos(n):
    soma = 0
    while n > 0:
        digito = n % 10  # Último dígito do número
        soma += digito  # Adiciona o dígito à soma
        n = n // 10  # Remove o último dígito do número
    return soma

n = int(input("Digite um número inteiro: "))
resultado = soma_digitos(n)
print(f"A soma dos dígitos de {n} é: {resultado}")