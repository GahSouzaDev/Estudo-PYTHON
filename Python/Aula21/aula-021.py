ano = int(input('Em que ano vc nasceu? '))
print('- - ' * 20)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('vc nasceu em um ano bissexto')
else:
    print('vc nao nasceu em um ano bissexto')
print('- - ' * 20)