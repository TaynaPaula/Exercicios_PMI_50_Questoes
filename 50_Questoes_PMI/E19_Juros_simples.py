#Escreva um programa que calcule juros simples.
try:
    C = float(input("Informe o valor inicial (capital): "))
    I = float(input("Informe a taxa de juros ao mês (em decimal, por exemplo 0.05 para 5%): "))
    T = float(input("Informe o tempo de operação (em meses): "))
    Valorfinal = C + (C * I * T)
    print(f"O valor final após {T} meses será: R$ {Valorfinal:.2f}")
except ValueError:
    print("Por favor, digite apenas números válidos.")
