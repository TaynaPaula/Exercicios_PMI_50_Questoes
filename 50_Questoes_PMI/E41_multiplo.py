# Crie um programa que verifique se um número é múltiplo de outro.
try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    if num2 == 0:
        print("O segundo número não pode ser zero.")
    elif num1 % num2 == 0:
        print(f"{num1} é múltiplo de {num2}")
    else:
        print(f"{num1} não é múltiplo de {num2}")       
except ValueError:
    print("Valor informado não é válido")