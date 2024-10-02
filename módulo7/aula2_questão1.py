# Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. 
# Dica: usando listas você não precisa fazer um "if" para cada mês.
# Ex:
# Digite uma data de nascimento: 29/10/1973
# Você nasceu em  29 de Outubro de 1973.

def data_nascimento_extenso(data_nascimento):   
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    dia, mes, ano = data_nascimento.split('/')

    # Converte o mês de string para inteiro e obtém o nome do mês correspondente
    mes_extenso = meses[int(mes) - 1]

    # Imprime a data com o mês por extenso
    print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")

# Solicita a data de nascimento do usuário
data = input("Digite sua data de nascimento (dd/mm/aaaa): ")
data_nascimento_extenso(data)