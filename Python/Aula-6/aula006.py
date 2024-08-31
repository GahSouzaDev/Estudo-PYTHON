n = int(input("Digite um número: "))
v = int(input("Valor limite da tabuada: "))

for x in range(v+1):
    print(f"{n} x {x} = {n * x}")
#o for ignora a ultima sequencia, tendo que colocar sempre o +1 para ober o valor desejado
