# Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".
# Ex:
# Digite uma frase: O rato roeu a roupa do rei
# Frase modificada: * r*t* r*** * r**p* d* r**

def substituir_vogais(frase):
    vogais = "aeiouAEIOU"  
    frase_modificada = ""
  
    for letra in frase:
        if letra in vogais:
        # Substitui vogal por "*"
            frase_modificada += "*"  
        else:
            frase_modificada += letra 

    return frase_modificada

# Solicita a frase do usuário
frase = input("Digite uma frase: ")

frase_modificada = substituir_vogais(frase)
print("Frase modificada:", frase_modificada)