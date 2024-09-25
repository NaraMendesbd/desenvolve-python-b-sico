# Crie uma função customizada e aplique a função embutida filter para operar em uma lista de listas contendo os lados de 
# múltiplos triângulos. Construa uma nova lista contendo apenas os triângulos equiláteros, ou seja, com os três lados iguais.

## Crie a função customizada 
# def testa_equilatero(lados): 

### Usando filter, aplique a função customizada aos seguintes triangulos 
# triangulos  = [[2,2,2], [3,4,5], [3,2,2],[4,4,4]]

def testa_equilatero(t):
    if t[0] == t[1] and t [1] == t[2]:
        return True
    return False

triângulos = [[2,2,2], [3,4,5], [3,2,2],[4,4,4]]
equiláteros = list(filter(testa_equilatero, triângulos))
print(equiláteros)