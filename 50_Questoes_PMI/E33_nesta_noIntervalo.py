n = 9  
tentativas = 0

while True:
    try:
        palpite = int(input("Digite um número entre 0 e 100: "))
        tentativas += 1

        if palpite < 0 or palpite > 100:
            print("Número fora do intervalo. Tente novamente.")
            continue

        if palpite == n:
            print(f"Você acertou! O número era {n}. Tentativas: {tentativas}")
            break
        elif palpite < n:
            print("O número é maior.")
        else:
            print("O número é menor.")
    except ValueError:
        print("Valor inválido! Por favor, digite um número válido.")
