# Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente.
# Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. Adicione o separador "-" na sua impressão.
# Digite o número: 97651234
# Número completo: 99765-1234
# Digite o número: 980876543
# Número completo: 98087-6543

def formata_numero_celular(numero):
    # Verifica se o número tem 8 dígitos 
    if len(numero) == 8:
     # Acrescenta o 9 na frente    
        numero = '9' + numero 
    # Verifica se o número tem 9 dígitos e o primeiro é 9
    elif len(numero) == 9 and numero[0] != '9':
        print("O número deve começar com 9 se tiver 9 dígitos.")
        return

    # Formata o número com o separador '-'
    numero_formatado = numero[:5] + '-' + numero[5:]
    return numero_formatado

# Solicita o número de celular
numero_celular = input("Digite o número: ")

# Formata e imprime o número
numero_formatado = formata_numero_celular(numero_celular)
if numero_formatado:
    print(f"Número completo: {numero_formatado}")