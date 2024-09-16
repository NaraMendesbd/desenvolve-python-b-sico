n = int(input("Número de jogos: "))

soma_vitórias, soma_empates, soma_derrotas = 0, 0,0

for jogo in range(n):
    gols_galo = int(input(f"digite os gol do galo no jogo {jogo}: "))
    gols_op = int(input(f"digite os gol do oponente no jogo {jogo}: "))

    if gols_galo > gols_op:
        soma_vitórias += 1
    elif gols_galo < gols_op:
        soma_derrotas += 1
    else:
        soma_empates += 1
    

    print("Total de vitórias", soma_vitórias)
    print("Total de empates", soma_empates)
    print("Total de derrotas", soma_derrotas)
    print("Pontuação", 3*soma_vitórias+soma_empates)