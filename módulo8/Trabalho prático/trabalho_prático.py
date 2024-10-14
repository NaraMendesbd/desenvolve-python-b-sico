import csv

# Estrutura de dados para usuários e produtos
usuarios = []
produtos = []

# Função para carregar usuários do arquivo
def carregar_usuarios(arquivo):
    with open(arquivo, mode='r', newline='', encoding='utf-8') as file:
        leitor = csv.reader(file)
        for linha in leitor:
            usuarios.append({'nome': linha[0], 'senha': linha[1], 'nivel': linha[2]})

# Função para salvar usuários no arquivo
def salvar_usuarios(arquivo):
    with open(arquivo, mode='w', newline='', encoding='utf-8') as file:
        escritor = csv.writer(file)
        for usuario in usuarios:
            escritor.writerow([usuario['nome'], usuario['senha'], usuario['nivel']])

# Função para autenticar o usuário
def autenticar_usuario(nome, senha):
    for usuario in usuarios:
        if usuario['nome'] == nome and usuario['senha'] == senha:
            return usuario
    return None

# Funções CRUD para usuários
def criar_usuario(nome, senha, nivel):
    usuarios.append({'nome': nome, 'senha': senha, 'nivel': nivel})
    salvar_usuarios('usuarios.csv')

def ler_usuarios():
    return usuarios

def atualizar_usuario(nome, novo_nome=None, nova_senha=None, novo_nivel=None):
    for usuario in usuarios:
        if usuario['nome'] == nome:
            if novo_nome:
                usuario['nome'] = novo_nome
            if nova_senha:
                usuario['senha'] = nova_senha
            if novo_nivel:
                usuario['nivel'] = novo_nivel
            salvar_usuarios('usuarios.csv')
            break

def deletar_usuario(nome):
    global usuarios
    usuarios = [usuario for usuario in usuarios if usuario['nome'] != nome]
    salvar_usuarios('usuarios.csv')

# Funções CRUD para produtos
def criar_produto(nome, preco, quantidade):
    produtos.append({'nome': nome, 'preco': preco, 'quantidade': quantidade})

def ler_produtos():
    return produtos

def atualizar_produto(nome, novo_nome=None, novo_preco=None, nova_quantidade=None):
    for produto in produtos:
        if produto['nome'] == nome:
            if novo_nome:
                produto['nome'] = novo_nome
            if novo_preco is not None:
                produto['preco'] = novo_preco
            if nova_quantidade is not None:
                produto['quantidade'] = nova_quantidade
            break

def deletar_produto(nome):
    global produtos
    produtos = [produto for produto in produtos if produto['nome'] != nome]

# Funções adicionais para produtos
def buscar_produto(nome):
    for produto in produtos:
        if produto['nome'] == nome:
            return produto
    return None

def imprimir_produtos_ordenados_por_nome():
    for produto in sorted(produtos, key=lambda x: x['nome']):
        print(produto)

def imprimir_produtos_ordenados_por_preco():
    for produto in sorted(produtos, key=lambda x: x['preco']):
        print(produto)

# Função principal
def main():
    carregar_usuarios('usuarios.csv')
    while True:
        print("\n1. Login")
        print("2. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome: ")
            senha = input("Senha: ")
            usuario = autenticar_usuario(nome, senha)
            if usuario:
                print(f"Bem-vindo, {usuario['nome']} ({usuario['nivel']})!")
                while True:
                    if usuario['nivel'] == 'gerente':
                        print("\n1. Gerenciar Usuários")
                        print("2. Gerenciar Produtos")
                        print("3. Sair")
                        opcao = input("Escolha uma opção: ")
                        # Adicione as funcionalidades para gerente aqui
                    else:
                        print("\n1. Consultar Produtos")
                        print("2. Sair")
                        opcao = input("Escolha uma opção: ")
                        # Adicione as funcionalidades para funcionário/estagiário aqui
            else:
                print("Usuário ou senha inválidos.")
        
        elif opcao == '2':
            print("Saindo...")
            break

if __name__ == "__main__":
    main()