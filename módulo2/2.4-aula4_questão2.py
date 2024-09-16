#Leitura de dados (entrada)
fahrenheit= int(input("Digite a temperatura fahrenheit: "))

#Processamento
celsius= (fahrenheit - 32) * 5/9

#Impressão de dados (saída)
print(f"{fahrenheit} graus fahrenheit são {int(celsius)} graus celsius")