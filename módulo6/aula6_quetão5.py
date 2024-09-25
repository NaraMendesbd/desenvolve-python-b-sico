# Escreva um programa para encontrar a diferença entre duas listas, incluindo elementos duplicados.
# Ex:
# Listas originais: 
# [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
# [1, 1, 2, 4, 5, 6]
# Diferença entre as listas:
# [3, 3, 4, 7]

def diferenca_listas(lista1, lista2):
    lista_diferenca = lista1.copy()  
    for item in lista2:
        if item in lista_diferenca:
            lista_diferenca.remove(item)  

    return lista_diferenca

# Listas originais
lista1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
lista2 = [1, 1, 2, 4, 5, 6]

# Calcuoa da diferença
resultado = diferenca_listas(lista1, lista2)

print("Diferença entre as listas:")
print(resultado)