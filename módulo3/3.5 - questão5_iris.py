# Você está projetando um sistema de autenticação baseado na análise da íris (parte colorida do olho). Ao acionado, o sistema coleta e retorna 3 valores inteiros referentes a atributos da íris visível. 
# # Mas o sistema não é perfeito, tendo uma margem de erro do sensor de +/- 5.
# O código abaixo tem os atributos dos 4 usuários cadastrados no sistema. 
# # Você deve completar om código, pedindo ao usuário para inserir uma nova leitura de padrão de íris. 
# # O programa deve comparar o padrão inserido com os padrões cadastrados no banco de dados. 
# # Se o padrão estiver dentro da tolerância estabelecida, o usuário é autenticado com sucesso. 
# Caso contrário, a autenticação falha.
## Não altere os atributos definidos a seguir
# iris1_a1, iris1_a2, iris1_a3 = 123, 456, 789
# iris2_a1, iris2_a2, iris2_a3 = 987, 654, 321
# iris3_a1, iris3_a2, iris3_a3 = 111, 222, 333
# iris4_a1, iris4_a2, iris4_a3 = 444, 555, 666
# Padrões cadastrados
iris1 = (123, 456, 789)
iris2 = (987, 654, 321)
iris3 = (111, 222, 333)
iris4 = (444, 555, 666)

# Margem de erro do sensor
margem_erro = 5

# Função para autenticar a íris
def autenticar_iris(iris_cadastrada, iris_lida):
    # Comparação de cada atributo da íris com a margem de erro
    for a_cadastrado, a_lido in zip(iris_cadastrada, iris_lida):
        if abs(a_cadastrado - a_lido) > margem_erro:
            return False
    return True

# Solicita nova leitura do padrão de íris
a1 = int(input("Digite o primeiro valor da leitura da íris: "))
a2 = int(input("Digite o segundo valor da leitura da íris: "))
a3 = int(input("Digite o terceiro valor da leitura da íris: "))
iris_lida = (a1, a2, a3)

# Verifica se a leitura da íris corresponde a algum usuário cadastrado
if autenticar_iris(iris1, iris_lida):
    print("Autenticação bem-sucedida: Usuário 1 autenticado.")
elif autenticar_iris(iris2, iris_lida):
    print("Autenticação bem-sucedida: Usuário 2 autenticado.")
elif autenticar_iris(iris3, iris_lida):
    print("Autenticação bem-sucedida: Usuário 3 autenticado.")
elif autenticar_iris(iris4, iris_lida):
    print("Autenticação bem-sucedida: Usuário 4 autenticado.")
else:
    print("Autenticação falhou: Nenhum usuário correspondente.")