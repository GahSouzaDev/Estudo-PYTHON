from random import randint
from time import sleep
print('vou pensar em um numero de 0 a 5, tenta acertar')
print('- - '*20)
computador = randint(0,5)#faz o sorteio
#print(f'Pesnei no numero, {computador}')
numero = (int(input('EM que numero eu pensei? ')))#jogador tentar acertar
print('PROCESSANDO...')
sleep(3)#delay em pause - tempo de espera
if numero == computador:
    print('PARABENS, voce acertou')
else:
    print(f'GANHEI, eu pensei o numero {computador}')
print('- - '*20)
