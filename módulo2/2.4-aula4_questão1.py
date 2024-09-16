#Leitura de dados (entrada)
comprimeto= int(input("Digite o comprimento: "))
largura= int(input("Digite a largura: "))
preço_m2= float(input("Valor do m2: "))

#Processamento
área= comprimeto * largura
preço_total=área * preço_m2

#Impressão de dados (saída)
print(f"O terreno possui {área}m2 e custa R${preço_total:,.2f}")