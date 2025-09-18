#Escreva um programa que determine o preço da passagem baseado na idade.
try:
    idade = int(input("Digite a idade do passageiro: "))
    
    if idade < 5:
        preco = 0
    elif idade <= 12:
        preco = 10
    elif idade <= 60:
        preco = 20
    else:
        preco = 15

    print(f"Idade {idade}, o preço da passagem é: R${preco:.2f}")
except ValueError:
    print("Idade inválida.")
