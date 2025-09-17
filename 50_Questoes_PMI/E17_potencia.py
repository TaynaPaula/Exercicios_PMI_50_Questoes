#Escreva um programa que calcule a potência de um número.
try:
    base = int(input("Informe a base: "))
    expoente = int(input("Informe o expoente: "))
    potencia = base ** expoente
    print(f"{base} elevado a {expoente} é {potencia}")
except ValueError:
    print("Erro: Por favor, insira apenas números válidos.")
