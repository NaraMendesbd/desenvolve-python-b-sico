# Escreva uma função em Python chamada soma_quadrados que recebe dois números como parâmetros e retorna a soma dos seus quadrados.
# No programa principal solicite ao usuário que insira dois números e utilize a função para exibir a soma dos quadrados.

def soma_quadrados(n1, n2):
    return n1**2 + n2**2

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

    
resultado = soma_quadrados(n1, n2)
print(f"A soma dos quadrados de {n1} e {n2} é: {resultado}")
