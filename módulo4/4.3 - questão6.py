maior = float('-inf')
menor = float('inf')

while True:
    n = int(input("Digite um número: "))
    if n == 0: break

    if n > maior:
        maior = n
    if n < menor:
        menor = n

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")