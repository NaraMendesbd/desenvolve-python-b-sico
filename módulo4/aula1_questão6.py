n = int(input("Quantidade de experimentos: "))
cont = 0
soma_sapos, soma_ratos, soma_coelhos = 0, 0, 0

while cont < n:
# número de cobaias
    quantia = int(input())
#tipo de cobaias
    tipo = input()
    if tipo == 'S':
        soma_sapos += quantia
    elif tipo == 'R':
        soma_ratos += quantia
    elif tipo == 'C':
        soma_coelhos += quantia

    cont += 1
print("total de cobaias", soma_sapos + soma_ratos + soma_coelhos)
print("total de sapos", soma_sapos)
print("total de ratos", soma_ratos)
print("total de coelhos", soma_coelhos)
print("percentual sapos", soma_sapos/n)
print("percentual de ratos", soma_ratos/n)
print("percentual de coelhos", soma_coelhos/n)