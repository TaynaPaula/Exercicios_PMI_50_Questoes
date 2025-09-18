#Crie um programa que verifique se um número é divisível por 3 e por 5.
try:
    n = int(input("Digite um número: "))

    if n % 3 == 0 and n % 5 == 0:
        print(f"{n} é divisível por 3 e por 5.")
    else:
        print(f"{n} não é divisível por 3 e por 5.")
except ValueError:
    print("Digite apenas números válidos.")
