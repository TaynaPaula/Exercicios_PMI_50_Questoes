n = 9
while True:
    try:
        palpite = int(input("Digite um número entre 0 e 100: "))
        if palpite < 0 or palpite > 10:
            print("Número fora do intervalo. Tente novamente.")
            continue

        if palpite == n:
            print("Você acertou!")
            
            break
        elif palpite < n:
            print("O número é maior")
        else:
            print("O número é menor")
    except ValueError:
        print("Valor inválido! Por favor, digite um número válido.")
