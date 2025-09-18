#Escreva um programa que calcule a distância entre dois pontos.
import math

try:
    A1 = int(input("Digite o valor de A1: "))
    A2 = int(input("Digite o valor de A2: "))
    B1 = int(input("Digite o valor de B1: "))
    B2 = int(input("Digite o valor de B2: "))

    D = math.sqrt((A1 - A2) ** 2 + (B1 - B2) ** 2)
    print("A distância é", D)
except ValueError:
    print("Digite um valor numérico, por favor.")
