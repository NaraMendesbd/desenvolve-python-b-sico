#Ler 3 notas
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))

# Calculo da média
m = (n1 + n2 + n3) / 3

while True:
    if m >= 60:
        print("Aprovado")
    elif m >= 40:
        print("Recuperação")
    else:
        print("Reprovado")