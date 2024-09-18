# Escreva um programa em Python que utiliza a biblioteca datetime para exibir a data e hora atuais 
# com a formatação apresentada a seguir:
# Data: 15/03/2023 
# Hora: 14:05

from datetime import datetime

data_hora_atual = datetime.now()

dia = f"{data_hora_atual.day:02d}"
mes = f"{data_hora_atual.month:02d}"
ano = data_hora_atual.year
hora = f"{data_hora_atual.hour:02d}"
minuto = f"{data_hora_atual.minute:02d}"

print(f"{dia}/{mes}/{ano}")
print(f"{hora}:{minuto}")
