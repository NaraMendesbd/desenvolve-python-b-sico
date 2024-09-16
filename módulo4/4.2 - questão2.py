numero = int(input("Digite um número inteiro positivo: "))

soma = 0

for i in range(1, numero + 1):
    soma += i

print(f"A soma dos números de 1 até {numero} é: {soma}")