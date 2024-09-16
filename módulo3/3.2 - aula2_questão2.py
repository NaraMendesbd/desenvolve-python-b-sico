idade_juliana = int(input())
print(idade_juliana >= 18)
idade_cris = int(input())
print(idade_cris >= 18)
# true se pelo menos um dos sois for maior de idade
# false em qualquer ouro caso
# <exp1> = juliana é maior de idade
# <exp2> = cris é maior de idade
# <exp1> or <exp2> 
liberado = idade_juliana >= 18 or idade_cris>=18
print(liberado)
