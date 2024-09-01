frase = 'curso em video python'
print(frase[15::3])
print(len(frase))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.split())
print('-'.join(frase))
print(frase.find("python"))#mostra localização de palavras

print('curso' in frase)  # imprime True
print('android' in frase)  # imprime False
print('em' in frase)  # imprime True
print('curso' not in frase)  # imprime False