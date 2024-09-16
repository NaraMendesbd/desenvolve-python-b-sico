#Leitura de dados (entrada)
valor= int(input("Digite o valor: "))

#Processamento
#começar da maior nota (quantas notas?)
notas_100 = valor // 100
#atualizar o valor restante
valor = valor % 100

notas_50 = valor // 50
#atualizar o valor restante
valor = valor % 50

notas_20 = valor // 20
#atualizar o valor restante
valor = valor % 20

notas_10 = valor // 10
#atualizar o valor restante
valor = valor % 10

notas_5 = valor // 5
#atualizar o valor restante
valor = valor % 5

notas_2 = valor //25
#atualizar o valor restante
valor = valor % 2

notas_1 = valor // 1

#Impressão de dados (saída)
print(f"{notas_100} nota(s) de 100")
print(f"{notas_50} nota(s) de 50")
print(f"{notas_20} nota(s) de 20")
print(f"{notas_10} nota(s) de 10")
print(f"{notas_5} nota(s) de 5")
print(f"{notas_2} nota(s) de 2")
print(f"{notas_1} nota(s) de 1")