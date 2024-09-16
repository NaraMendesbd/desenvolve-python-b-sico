produto = 1

while True:
    n = int(input("Digite um número: "))
    if n == 0: break
    if n < 0: continue

    produto *= n
    

print(f"O produto dos positivos é: {produto}")
