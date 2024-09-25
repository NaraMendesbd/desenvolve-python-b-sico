# Crie uma função chamada ordena_por_comprimento que aceite uma lista de strings e a ordene com base no comprimento das strings, 
# do menor para o maior. Utilize a função sorte e uma expressão lambda.

# crie a função ordena_por_comprimento e retorne a lista resultado
## aplique sua função à seguinte lista e imprima o resultado
# nomes = ["Joao", "Maria", "Jose", "Gabriela", "Sol", "Luna", "Bento", "Enzo", "Fernanda"]

#  Função que ordena a lista de strings pelo comprimento
def ordena_por_comprimento(lista):
    return sorted(lista, key=lambda x: len(x))

# Lista de nomes fornecida
nomes = ["Joao", "Maria", "Jose", "Gabriela", "Sol", "Luna", "Bento", "Enzo", "Fernanda"]

resultado = ordena_por_comprimento(nomes)
print(resultado)