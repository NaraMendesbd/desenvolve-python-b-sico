# Você está desenvolvendo um programa para auxiliar em cálculos de geometria básica. Crie as seguintes funções:
# A função calcula_perimetro_triangulo() que recebe três inteiros correspondentes aos lados de um triângulo e retorna o 
# perímetro do triângulo, ou seja, a soma dos seus lados.
# A função calcula_perimetro_circulo() que recebe um inteiro referente ao raio do círculo e retorna o perímetro do círculo, 
# dado por 2πr. Use a constante π da biblioteca math.
# A função calcula_perimetro_retangulo() que possui um parâmetro obrigatório lado1 e um opcional lado2, ambos inteiros. 
# Se o valor opcional não for fornecido, significa que se trata de um quadrado. 
# Sua função deve calcular e retornar o perímetro do retângulo, ou seja, a soma de seus lados. 
# Para o quadrado, é dado por 4 X lado 1
# Para o retângulo é dado por 2 X lado 1 + 2 X lado 2
# No programa principal apresente um menu com as opções disponíveis do seu sistema e uma quarta opção Sair. 
# Solicite ao usuário a opção desejada, solicite as entradas correspondentes à opção escolhida, invoque a respective função 
# e apresente o seu retorno. Seu programa deve retornar ao menu até que o usuário escolha a opção Sair

import math

# Perímetro de um triângulo
def calcula_perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

# Perímetro de um círculo
def calcula_perimetro_circulo(raio):
    return 2 * math.pi * raio

# Perímetro de um retângulo (ou quadrado se lado2 não for fornecido)
def calcula_perimetro_retangulo(lado1, lado2=None):
    if lado2 is None:  # Caso seja um quadrado
        return 4 * lado1
    else:  # Caso seja um retângulo
        return 2 * lado1 + 2 * lado2

# Exibir o menu e realizar o cálculo com base na escolha do usuário
def exibir_menu():
    while True:
        print("\nMenu de Cálculos de Perímetro:")
        print("1. Calcular perímetro de um triângulo")
        print("2. Calcular perímetro de um círculo")
        print("3. Calcular perímetro de um retângulo ou quadrado")
        print("4. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            lado1 = int(input("Informe o valor do lado 1 do triângulo: "))
            lado2 = int(input("Informe o valor do lado 2 do triângulo: "))
            lado3 = int(input("Informe o valor do lado 3 do triângulo: "))
            perimetro = calcula_perimetro_triangulo(lado1, lado2, lado3)
            print(f"O perímetro do triângulo é: {perimetro}")

        elif opcao == 2:
            raio = int(input("Informe o valor do raio do círculo: "))
            perimetro = calcula_perimetro_circulo(raio)
            print(f"O perímetro do círculo é: {perimetro:.2f}")

        elif opcao == 3:
            lado1 = int(input("Informe o valor do lado 1: "))
            lado2 = input("Informe o valor do lado 2 (deixe vazio se for um quadrado): ")
            if lado2:
                perimetro = calcula_perimetro_retangulo(lado1, int(lado2))
            else:
                perimetro = calcula_perimetro_retangulo(lado1)
            print(f"O perímetro é: {perimetro}")

        elif opcao == 4:
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Programa principal
exibir_menu()