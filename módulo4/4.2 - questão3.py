#"Digite dez números inteiros positivos
soma = 0
for n in range(1, 11):
    número =int(input(f"Digite o {n}º número inteiro positivo: "))
    soma += número
   
média = soma/10
print(f"A média dos númeross digitados é: {média:.2f}")