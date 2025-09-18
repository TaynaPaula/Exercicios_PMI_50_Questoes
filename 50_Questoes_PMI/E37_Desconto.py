#Crie um programa que determine o desconto baseado no valor da compra.
try:
    valor_compra = float(input("Digite o valor da compra: R$ "))

    if valor_compra > 100:
        desconto = valor_compra * 0.10
        valor_final = valor_compra - desconto
        print(f"O valor da compra é R${valor_compra:.2f}, você ganhou um desconto de R${desconto:.2f}, o valor final a pagar é R${valor_final:.2f}")
    else:
        print(f"O valor da compra é R${valor_compra:.2f}, você não ganhou desconto, o valor final a pagar é R${valor_compra:.2f}")

except ValueError:
    print("Valor informado inválido! Digite apenas números.")
