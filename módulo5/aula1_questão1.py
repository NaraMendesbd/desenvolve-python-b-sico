# Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e 
# calcule a diferença absoluta entre esses dois números. Utilize a função nativa abs para garantir que o resultado 
# seja sempre positivo e round para arredondar o resultado para duas casas decimais.
# Exemplo de interação:
# Digite o primeiro número: 3.1415
# Digite o segundo número: 1.4142
# A diferença absoluta entre os números é: 1.73

n1 = float(input("Digite o primeiro número decimal: "))
n2 = float(input("Digite o segundo número decimal: "))

diferenca = abs(n1 - n2)

# Arredondamento da diferença para duas casas decimais
diferenca_arredondada = round(diferenca, 2)

print(f"A diferença absoluta entre os dois números é: {diferenca_arredondada}")