# Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5.
print("Dê uma nota ao filme")
n = int(input())
if n == 5:
    print("Excelente!")
if n == 4:
    print("Muito Bom!")
if n == 3:
    print("Bom!")
if n == 2:
    print("Regular!")
if n == 1:
    print("Ruim!")