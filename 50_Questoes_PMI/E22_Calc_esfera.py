#Crie um programa que calcule o volume de uma esfera.
try:
    R = float(input("Digite o raio: "))
    V = (4 * 3.1415 * (R ** 3)) / 3
    print(f"O volume da esfera com raio {R} é: {V:.2f}")
except ValueError:
    print("O valor do raio é inválido. Por favor, digite apenas números.")
