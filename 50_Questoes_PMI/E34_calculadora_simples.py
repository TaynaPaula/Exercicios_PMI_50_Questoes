#Escreva um programa que simule uma calculadora simples.
try:
    Valor1 = int(input("Digite o primeiro valor: "))
    Valor2 = int(input("Digite o segundo valor: "))

    print("Escolha a operação:")
    print("1 - Divisão (/)")
    print("2 - Multiplicação (*)")
    print("3 - Subtração (-)")
    print("4 - Soma (+)")
    calc = input("Digite o número da operação desejada: ")

    if calc == "1":
        if Valor2 == 0:
            print("Erro: divisão por zero não é permitida!")
        else:
            print(f"A divisão de {Valor1} / {Valor2} é: {Valor1 / Valor2}")
    elif calc == "2":
        print(f"A multiplicação de {Valor1} * {Valor2} é: {Valor1 * Valor2}")
    elif calc == "3":
        print(f"A subtração de {Valor1} - {Valor2} é: {Valor1 - Valor2}")
    elif calc == "4":
        print(f"A soma de {Valor1} + {Valor2} é: {Valor1 + Valor2}")
    else:
        print("Operação inválida!")

except ValueError:
    print("Digite apenas números válidos.")
