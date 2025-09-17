#Crie um programa que converta temperatura de Celsius para Fahrenheit.
try:
    temperatura= float(input("Digite a temperatura "))
    F=(((9*temperatura)+160)/5)
    print(f"A temperatura {temperatura}°C em Fahrenheit é: {F:.2f}°F")
except ValueError:
    print("Erro: Por favor, insira um número válido.")  

