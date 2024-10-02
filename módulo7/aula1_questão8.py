# Desenvolva um validador de CPF. Solicite do usuário um CPF na forma XXX.XXX.XXX-XX (lido como string) e imprima "Válido" ou "Inválido". 
# O primeiro passo é calcular o primeiro dígito verificador. Separamos os primeiros 9 dígitos do CPF (ex: 111.444.777) e
# multiplicamos cada um dos números, da direita para a esquerda por números crescentes a partir do número 2, como no exemplo abaixo:
# CPF 1 1 1 4 4 4 7 7 7
# Multiplicador 10 9 8 7 6 5 4 3 2 
# Resultado 10 9 8 28 24 20 28 21 14
# Em seguida somamos o resultado: 10+9+8+28+24+20+28+21+14 = 162
# Pegamos o resultado e dividimos por 11:  162 / 11 = 14 com resto 8
# Se o resto da divisão for menor que 2, então o dígito é igual a 0 (Zero).
# Se o resto da divisão for maior ou igual a 2, então o dígito verificador é igual a 11 menos o resto da divisão (11 - resto).
# 11-6 = 5, logo 5 é o nosso segundo dígito verificador e o CPF completo é:
#                               111.444.777-35
# O CPF de entrada deve ser considerado válido se os dígitos fornecidos pelo usuário forem os mesmos dígitos calculados
# através do processo acima. 
# Exemplos válidos
# 545.315.761-52
# 473.063.662-70
# 775.682.566-77
# Exemplos inválidos
# 545.315.761-12
# 473.063.662-98
# 775.682.566-13

def calcular_digito(cpf, multiplicadores):
    soma = sum(int(cpf[i]) * multiplicadores[i] for i in range(len(multiplicadores)))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

def validar_cpf(cpf):
    # Remove os caracteres especiais do CPF
    cpf = cpf.replace('.', '').replace('-', '')

    # Verifica se o CPF tem exatamente 11 dígitos
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    # Calcula o primeiro dígito verificador
    multiplicadores_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    digito1 = calcular_digito(cpf[:9], multiplicadores_1)

    # Calcula o segundo dígito verificador
    multiplicadores_2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    digito2 = calcular_digito(cpf[:10], multiplicadores_2)

    # Verifica se os dígitos calculados correspondem aos fornecidos
    return cpf[-2:] == f"{digito1}{digito2}"

# Solicita o CPF do usuário
cpf_input = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")

# Valida o CPF e imprime o resultado
if validar_cpf(cpf_input):
    print("Válido")
else:
    print("Inválido")


