from datetime import date
ano = date.today().year#pega ano atual da maquina
print(f'o ano é {ano}')
print('- - ' * 20)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('É um ano bissexto')
else:
    print('É um ano bissexto')
print('- - ' * 20)
