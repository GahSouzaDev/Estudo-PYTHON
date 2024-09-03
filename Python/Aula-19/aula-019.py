velocidade = float(input('QUal a velocidade do seu carro? '))
print("- - "*20)
if velocidade > 80:
    print('MULTADO, você ultrapassou o limite de velocidade')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R${multa}')

print('- - '*20)
print('Tenha um bom dia, dirija com segurão!')
print('- - '*20)
