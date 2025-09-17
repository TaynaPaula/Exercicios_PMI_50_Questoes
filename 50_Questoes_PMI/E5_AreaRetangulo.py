#Escreva um programa que calcule a área de um retângulo.
try:
   C=10
   H=6
   Area=C*H
   print(f"A área de um retângulo de base {C} e altura {H} é: {Area}")
except ValueError:
    print("Erro: Por favor, insira um número válido.")