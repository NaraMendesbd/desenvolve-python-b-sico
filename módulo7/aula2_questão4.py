
# código com problema

#  Implemente uma função em Python chamada validador_senha() que verifica se uma senha fornecida atende todos os seguintes critérios:
# 1 - Pelo menos 8 caracteres de comprimento.
# 2 - Contém pelo menos uma letra maiúscula e uma letra minúscula.
# 3 - Contém pelo menos um número.
# 4 - Contém pelo menos um caractere especial (por exemplo, @, #, $).
# # 5 -Complete o seguinte código:
# def validador_senha(senha):
    #### Escreva a função

# Exemplo de uso:
# senha1 = "Senha123@"
# senha2 = "senhafraca"
# senha3 = "Senha_fraca"
# print(validador_senha(senha1))  # Saída esperada: True
# print(validador_senha(senha2))  # Saída esperada: False
# print(validador_senha(senha3))  # Saída esperada: False

import re 

def validador_senha(senha):
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False

# Solicita ao usuário que insira a senha
    senha_usuario = input("Digite sua senha com pelo memos oito caractéres: (digite fim para sair)")
    
    
    # Verifica se contém pelo menos uma letra maiúscula
    if not re.search(r'[A-Z]', senha):
        return False

    # Verifica se contém pelo menos uma letra minúscula
    if not re.search(r'[a-z]', senha):
        return False

    # Verifica se contém pelo menos um número
    if not re.search(r'\d', senha):
        return False

    # Verifica se contém pelo menos um caractere especial (@, #, $, etc.)
    if not re.search(r'[@#$%^&+=!]', senha):
        return False

    # Se todos os critérios forem atendidos, retorna True
    return True



# Exemplos de uso
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1))  # Saída esperada: True
print(validador_senha(senha2))  # Saída esperada: False
print(validador_senha(senha3))  # Saída esperada: False

