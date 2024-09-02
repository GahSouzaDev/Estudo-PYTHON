# Pede ao usuario para digitar seu nome
nome = str(input('digite seu nome: ')).strip()

# A funcao split() divide a string em uma lista de substrings,
# separadas pelo caractere especificado (no caso, o espaco).
# A lista de substrings esta ordenada pela ordem em que
# elas aparecem na string original.

# A primeira substring da lista e o primeiro nome,
# que pode ser acessado pelo indice [0]
primeiro_nome = nome.split()[0]

# A ultima substring da lista e o ultimo nome,
# que pode ser acessado pelo indice [-1],
# que significa "o ultimo elemento da lista"
ultimo_nome = nome.split()[-1]

# Imprime o resultado com uma string formatada
print(f'seu primeiro nome e {primeiro_nome} e seu ultimo nome e {ultimo_nome}')
