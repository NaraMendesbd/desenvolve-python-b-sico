# Crie a função inverteValor() que recebe um inteiro de qualquer tamanho e retorna esse valor invertido usando apenas 
# operações aritméticas.

def invertevalor(valor):
    valor_invertido = 0
    while valor > 0:
        dígito = valor % 10
        valor_invertido = valor_invertido * 10 + dígito  # Atualiza o valor invertido
        valor = valor // 10
    return valor_invertido

# Crie a função verificaInverso() que recebe o valor original e o valor invertido e retorna verdadeiro se ambos forem 
# igualmente par ou igualmente ímpar. Retorne falso caso contrário.

def verificainverso(valor, valor_invertido):
      return (valor % 2 == valor_invertido % 2)

# No programa principal, peça um valor do usuário e imprima o retorno de ambas as funções.
n = int(input("Digite un número inteiro com 2 ou mais dígitos: "))
n_invertido = invertevalor(n)
print(n_invertido)
print(verificainverso(n, n_invertido))
   