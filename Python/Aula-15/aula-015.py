nome = str(input('Digite seu nome: ')).strip()
print(f'ola, {nome} seja muito bem vindo' )
print(f'seu nome maioscula e {nome.upper()} e em minuscula e {nome.lower()}')

print(f'seu nome tem {len(nome)-nome.count(' ')} letras')
print(f'seu primeiro nome tem {nome.find(' ')} letras')
