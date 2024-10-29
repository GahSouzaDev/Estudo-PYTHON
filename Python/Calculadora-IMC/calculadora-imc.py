def calcular_imc(peso, altura_cm):
    # Converte a altura de cm para metros
    altura_m = altura_cm / 100
    # Calcula o IMC usando a fórmula IMC = peso / altura²
    return peso / (altura_m ** 2)

def classificar_imc(imc):
    # Classifica o IMC de acordo com as categorias padrão da OMS
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

def main():
    print("Calculadora de IMC")
    
    # Solicita peso e altura do usuário
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura_cm = float(input("Digite sua altura em cm: "))

        # Calcula o IMC e classifica o resultado
        imc = calcular_imc(peso, altura_cm)
        classificacao = classificar_imc(imc)
        
        # Exibe o resultado ao usuário
        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
    except ValueError:
        print("Erro: Certifique-se de que inseriu valores numéricos para peso e altura.")
    
    # Pausa o programa para que o terminal permaneça aberto
    input("Pressione Enter para sair...")

if __name__ == "__main__":
    main()
