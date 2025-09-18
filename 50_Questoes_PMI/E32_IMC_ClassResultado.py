# Escreva um programa que calcule o IMC e classifique o resultado.

try:
    peso = float(input("Digite o peso (kg): "))
    altura = float(input("Digite a altura (m): "))

    if altura == 0:
        raise ZeroDivisionError("A altura não pode ser zero.")

    imc = peso / (altura ** 2)
    print(f"Seu IMC é: {imc:.2f}")

    if imc < 18.5:
        print("Classificação: Abaixo do peso")
    elif 18.5 <= imc <= 24.9:
        print("Classificação: Peso normal")
    elif 25 <= imc <= 29.9:
        print("Classificação: Sobrepeso")
    elif 30 <= imc <= 34.9:
        print("Classificação: Obesidade grau I")
    elif 35 <= imc <= 39.9:
        print("Classificação: Obesidade grau II")
    else:
        print("Classificação: Obesidade grau III")

except ValueError:
    print("Erro: digite valores numéricos válidos.")
except ZeroDivisionError as e:
    print(f"Erro: {e}")

