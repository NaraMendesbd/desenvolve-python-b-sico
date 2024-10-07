# A extensão ".csv" significa "comma-separated values" ou "valores separados por vírgula". 
# É a extensão utilizada por sistemas de gerência de tabelas como o Microsoft Excel ou Google Sheets. 
# Nesse exercício vamos criar uma planilha com dados sobre livros que você já leu ou gostaria de ler. Siga as instruções.
# Selecione pelo menos 10 livros que você leu ou gostaria de ler. Você deve reunir as seguintes informações: título, autor, 
# ano de publicação e número de páginas.
# No Python, crie um arquivo chamado "meus_livros.csv", aberto para escrita.
# Na primeira linha escreva os títulos da planilha separados por vírgula (sem espaço em branco). Os títulos são: 
# "Título", "Autor", "Ano de publicação" e "Número de páginas". Lembre de finalizar a linha com uma quebra de linha.
# A partir da segunda linha escreva as informações de cada livro que você levantou, 
# separando cada informação por uma vírgula (sem espaço em branco). 
# Lembre de finalizar cada linha com uma quebra de linha.
# Feche o arquivo para salvá-lo e abra com a ferramenta de planilhas de sua escolha. 
# Como você já tem conta no Google, sugiro abrir com o Google Sheets.
# Seu arquivo deve ser aberto como uma planilha parecida com a imagem anexada neste exercício.

livros = [
["O Senhor dos Anéis - O Retorno do Rei", "J.R.R. Tolkien", 2002, 441],
["O Senhor dos Anéis - A Sociedade do Anel", "J.R.R. Tolkien", 2002, 441],  
["O Senhor dos Anéis - As Duas Torres", "J.R.R. Tolkien", 2002, 473],  
["A Bicicleta Azul - Volume 1", "Régine Deforges", 1985, 403],  
["A Bicicleta Azul - Volume 2", "Régine Deforges", 1985, 291],  
["A Bicicleta Azul - Volume 3", "Régine Deforges", 1985, 378],  
["A Bicicleta Azul -Tango Negro", "Régine Deforges", 1995, 316],  
["O Incêdio de Rróia", "Marion Zimmer Bradley", 1988, 545],  
["Ivanhoé", "Walter Scott", 2003, 478], 
["Os Três Mosqueteiros", "Alexandre Dumas", 1844, 688], 
]

with open("meus_livros.csv", "w") as arquivo:
   
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    
    # Escrever as informações de cada livro
    for livro in livros:
        linha = ",".join(map(str, livro)) + "\n"
        arquivo.write(linha)

print("Arquivo 'meus_livros.csv' criado com sucesso.")