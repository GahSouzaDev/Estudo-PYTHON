from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h1 = hypot(co, ca)
#metodo para calculo de ipotenusa

print (f'A soma dos quadrados de {co} e {ca} e {h1}')
