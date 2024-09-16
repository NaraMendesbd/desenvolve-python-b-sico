# Escreva um programa que leia os comprimentos dos 3 lados de um triângulo e diga se o triângulo é equilátero, isóceles ou escaleno.
# Regras:
# A: Isóceles: Quaisquer dois lados com o mesmo comprimento
# B:Equilátero: Os três lados tem o mesmo comprimento
# C: Escaleno: Três lados de comprimento diferente

print("Qual o triângulo")
l1 = int(input('lado 1:  '))
l2 = int(input('lado 2:  '))
l3 = int(input('lado 3:  '))
if  l1 == l2 and l2 ==l3:
    print("Equilátero")
if l1 == l2 or l1 == l3 or l2 ==l3:
    print("Isóceles")
if l1 != l2 and l2 != l3 and l1 != l3:
    print("Escaleno")