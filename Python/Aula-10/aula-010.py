#esse codigo serve para calcular o seno de um angulo
#o math.sin() espera um angulo em radianos como parametro
#mas o usuario vai digitar o angulo em graus
#por isso precisamos converter o angulo de graus para radianos
#com a funcao math.radians() que recebe o angulo em graus como parametro
#e retorna o angulo em radianos

#o resultado do seno sera impresso na tela
#com a funcao print() que vai formatar a string com o valor do seno
#e o valor do angulo digitado pelo usuario
import math
angulo = float(input('Digite o angulo que deseja: '))

seno = math.sin(math.radians(angulo))
print(f'o seno do angulo {angulo} e {seno}')
