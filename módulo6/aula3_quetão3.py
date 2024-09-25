# Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. 
# Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del. 
# Você deve imprimir a lista antes e depois da deleção.

# Original: [9, 2, -1, 4, -2, -3, 5, 6, -7, -4, -1, 6, 8, -3, -6]
# Editada:  [9, 2, -1, 4, -2, -3, 5, 6, 6, 8, -3, -6]

elementos = [9, 2, -1, 4, -2, -3, 5, 6, -7, -4, -1, 6, 8, -3, -6]

início_fatia_maior, tam_fatia_maior = 0, 0
início_fatia_atual, tam_fatia_atual = 0, 0

for i in range(len(elementos)):
    print('Início do laço', i, elementos[i])
    if elementos[i] <0:
        tam_fatia_atual += 1
        if tam_fatia_atual == 1:
            print('Início nova fatia', tam_fatia_atual)
            início_fatia_atual = i
    
    else:
        if tam_fatia_atual > tam_fatia_maior:
            print('Maior fatia até agora', tam_fatia_atual)
            tam_fatia_maior = tam_fatia_maior
            início_fatia_maior = início_fatia_atual
        tam_fatia_atual = 0

    print(início_fatia_maior, tam_fatia_maior)
    del elementos[início_fatia_maior: início_fatia_maior+tam_fatia_maior]
    print(elementos)
   

