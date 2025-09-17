#Escreva um programa que calcule o perímetro de um círculo.
import math

try:
    raio = float(input("Digite o raio: "))
    perimetro = 2 * math.pi * raio
    print("Perímetro do círculo:", perimetro)
except ValueError:
    print("Erro: valor inválido para raio.")
