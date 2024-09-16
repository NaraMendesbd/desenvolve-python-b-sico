#  Escreva um código que solicita ao usuário para inserir um ano e imprime "Bissexto" se:
#A: divisível por 4 e não for divisível por 100
#B: se for divisível por 400
#C: Caso contrário imprimir  "Não Bissexto".

ano = int(input())
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("Bissexto")
else:
    print("Não Bissexto")