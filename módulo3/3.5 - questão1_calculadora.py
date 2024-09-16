#  Escreva um programa que solicita 3 entradas:
# o primeiro operando (float), 
# o operador (caracter) 
# e o segundo operando (float).
# Seu programa deve imprimir o resultado da operação solicitada, entre soma (+),subtração (- entre soma (+),), divisão (/), multiplicação (*) ou potência (**). 
# Seu programa também deve imprimiruma mensagem de erro se a operação solicitada não estiver dentre as opções disponíveis.

n1 = float(input())
operador = input()
n2 = float(input())

if operador == "+":
    resultado = n1 + n2
elif operador == "-":
    resultado = n1 - n2
elif operador == "*":
    resultado = n1 * n2
elif operador == "/":
    resultado = n1 / n2
else:
    print("operação inválida")
print(f"{n1}{operador}{n2}={resultado}")