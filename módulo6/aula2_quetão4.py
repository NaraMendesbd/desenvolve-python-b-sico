# Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. 
# Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. 
# Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.

def combinar_listas_alternadamente(lista1, lista2):
    lista3 = []
    # Elementos das listas intercalados até que a menor lista termine
    for i in range(min(len(lista1), len(lista2))):
        lista3.append(lista1[i])
        lista3.append(lista2[i])
    
    # Adicionando os elementos restantes da maior lista
    if len(lista1) > len(lista2):
        lista3.extend(lista1[len(lista2):])
    elif len(lista2) > len(lista1):
        lista3.extend(lista2[len(lista1):])
    
    return lista3

# Solicitando as duas listas ao usuário
lista1 = list(map(int, input("Digite os elementos da lista1 separados por espaço: ").split()))
lista2 = list(map(int, input("Digite os elementos da lista2 separados por espaço: ").split()))

# Combinando as listas
lista_resultante = combinar_listas_alternadamente(lista1, lista2)

# Imprimindo a lista resultante
print(f"Lista combinada: {lista_resultante}")