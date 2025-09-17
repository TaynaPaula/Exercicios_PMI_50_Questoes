#Escreva um programa que calcule o quadrado de um número.
try:
    A=int(input("Infome um valor para calcular "))
    Quadrado=A**2
    print(f"O quadrado do número {A} é {Quadrado}")
except ValueError:
    print("Erro: Por favor, insira um número válido.")

#ok