n = int(input("Digite um número: "))
cont = 0
while n > 0:
    
    x = int(input("Digite um número: "))
    
    if x > cont:
       cont = x
    n = n - 1

print("o valor de cont:", cont)