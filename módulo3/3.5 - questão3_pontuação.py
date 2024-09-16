# Escreva um programa em Python que avalia a pontuação do jogador em uma missão e atribui uma classificação com base nas seguintes condições:
# Se a pontuação for menor que 70, atribua a classificação "Insatisfatório".
# Se a pontuação for maior ou igual a 70, atribua a classificação "Regular".
# Se a pontuação for maior ou igual a 80, atribua a classificação "Bom".
# Se a pontuação for maior ou igual a 90, atribua a classificação "Excelente".

pontuação = float(input("Digite a pontuação: "))
if pontuação < 70:
    classificação = "Insatisfatório"
elif pontuação >= 70 and pontuação <= 79:
    classificação = "Regular"
elif pontuação >= 80 and pontuação <= 89:
    classificação = "Bom"
elif pontuação >= 90:
    classificação = "Excelente" 
print(f"A pontuação foi {pontuação} e sua classificação foi {classificação}")

