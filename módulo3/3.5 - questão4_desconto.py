# Escreva um programa que calcula o desconto com base no valor total da compra e atribui diferentes níveis de desconto.
# Condições:
# Se o valor total da compra for menor que R$ 50, não há desconto.
# Se o valor total da compra for maior ou igual a R$ 50, atribua um desconto de 10%.
# Se o valor total da compra for maior ou igual a R$ 100, atribua um desconto de 20%.

valor_compra = float(input("Digite o valor da compra R$: "))

# 20% de desconto
if valor_compra >= 100.00: 
    desconto = 0.20
# 10% de desconto
elif valor_compra >= 50.00:
    desconto = 0.10 
# Sem desconto
else:
   desconto = 0.00

# Calculo do valor total (a ser pago) e do valor do desconto 
valor_desconto = valor_compra * desconto
valor_total = valor_compra - valor_desconto

# Exibe os resultados
print(f"Valor total da compra: R$ {valor_total:.2f}")
print(f"O valor do desconto é: R$ {valor_desconto:.2f} ({desconto * 100:.0f}%)")
print(f"Valor total a pagar: R$ {valor_total:.2f}")