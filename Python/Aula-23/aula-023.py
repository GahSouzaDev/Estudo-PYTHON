#configurando cor do texto

nome = str(input('Qual seu nome?: '))
#\033[ m
#entre o ']' e o 'm' vai o style do texto

#texto normal, cor amarelo e fundo azul
#exemplo: \033[0;33;44m] 
#estilo - texto - fundo

#estilo
#0 non
#1 bold
#4 underline
#7 negative

#texto
#30 branco
#31 vermelho
#32 verde
#33 amarelo
#34 azul
#35 roxo
#36 ciano
#37 cinza

#fundo
#40 branco
#41 vermelho
#42 verde
#43 amarelo
#44 azul
#45 roxo
#46 ciano
#47 cinza

print(f'\033[0+;35;43mOla {nome} seja muito bem vindo\033[m')
