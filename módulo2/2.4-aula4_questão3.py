# Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online.
# O preço dos produtos é calculado multiplicando a quantidade pelo preço unitário. 
# Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados 
# e imprima ao final o preço total da compra. Note no exemplo a seguir que:
# Digite o nome do produto 1: calça
#Digite o preço unitário do produto 1: 199.90
#Digite a quantidade do produto 1: 3
#Digite o nome do produto 2: camisa
#Digite o preço unitário do produto 2: 49.95
#Digite a quantidade do produto 2: 10
#Digite o nome do produto 3: cinto
#Digite o preço unitário do produto 3: 25
#Digite a quantidade do produto 3: 3

produto1 = input("Digite o nome do 1º produto: ")
preco1 = float(input(f"Digite o preço unitário de {produto1}: R$ "))
quantidade1 = int(input(f"Digite a quantidade de {produto1}: "))

produto2 = input("Digite o nome do 2º produto: ")
preco2 = float(input(f"Digite o preço unitário de {produto2}: R$ "))
quantidade2 = int(input(f"Digite a quantidade de {produto2}: "))

produto3 = input("Digite o nome do 3º produto: ")
preco3 = float(input(f"Digite o preço unitário de {produto3}: R$ "))
quantidade3 = int(input(f"Digite a quantidade de {produto3}: "))

total1 = preco1 * quantidade1
total2 = preco2 * quantidade2
total3 = preco3 * quantidade3

preco_total = total1 + total2 + total3

print(f"O total da compra foi de: R$ {preco_total}")