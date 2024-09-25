# Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (pelo menos 4 valores), 
# os armazena em uma lista e, usando fatiamento de listas, imprima:
# A lista original
# Os 3 primeiros elementos
# Os 2 últimos elementos
# A lista invertida (do fim para o começo)
# Os elementos de índice par (0, 2, 4 … )
# Os elementos de índice ímpar (1, 3, 5, … )


# Solicita ao usuário uma lista de pelo menos 4 números inteiros
nums = list(map(int, input("Digite pelo menos 4 números inteiros separados por espaço: ").split()))

while len(nums) < 4:
    print("Você deve inserir pelo menos 4 números.")
    nums = list(map(int, input("Digite pelo menos 4 números inteiros separados por espaço: ").split()))

# Lista original
print(f"Lista original: {nums}")

# 3 primeiros números
print(f"Os 3 primeiros números são: {nums[:3]}")

# 2 últimos números
print(f"Os 2 últimos números são: {nums[-2:]}")

# Lista invertida
print(f"A lista invertida é: {nums[::-1]}")

# Números de índice par
print(f"Os números de índice par são: {nums[::2]}")

# Números de índice ímpar
print(f"Os números de índice ímpar são: {nums[1::2]}")