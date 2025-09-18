# Escreva um programa que verifique se um número é positivo, negativo ou zero.
try:
    num = float(input("Digite um valor: "))
    if num > 0:
        print(f"O número {num} é positivo")
    elif num < 0:
        print(f"O número {num} é negativo")
    else:
        print("O número é zero")
except ValueError:
    print("Valor informado não é válido")
