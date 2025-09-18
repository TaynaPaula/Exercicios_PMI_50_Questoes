#Crie um programa que calcule o resto da divisão.
try:
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))
    Resto = A % B
    print(f"O resto da divisão de {A} / {B} é: {Resto}")
except ValueError:
    print("Digite apenas números válidos.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
