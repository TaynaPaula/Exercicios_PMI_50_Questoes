#Escreva um programa que calcule o IMC (Índice de Massa Corporal).
try:
    peso = float(input("Digite o peso (kg): "))
    altura = float(input("Digite a altura (m): "))
    imc = peso / (altura * altura)
    print("Seu IMC é:", round(imc, 2))
except ValueError:
    print("Erro: digite valores numéricos.")
except ZeroDivisionError:
    print("Erro: a altura não pode ser zero!")

