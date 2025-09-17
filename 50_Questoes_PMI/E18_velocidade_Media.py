#Crie um programa que calcule a velocidade média.
#Vm = D / T (velocidade média = distância / tempo)
try:    
    D = float(input("Digite a distância em km: "))
    T = float(input("Digite o tempo em horas: "))
    Vm = D / T
    print(f"A velocidade média é: {Vm:.2f} km/h")   
except ValueError:
    print("Erro: Por favor, insira um número válido.")
except ZeroDivisionError:
    print("Erro: O tempo não pode ser zero.")