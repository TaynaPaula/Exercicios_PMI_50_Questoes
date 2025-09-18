#Escreva um programa que determine o maior e menor entre três números.
try:
    A = int(input("Digite um valor inteiro para A: "))
    B = int(input("Digite um valor inteiro para B: "))
    C = int(input("Digite um valor inteiro para C: "))

    if A <= B and A <= C:
        if B <= C:
            print("Ordem crescente: {}, {}, {}".format(A, B, C))
        else:
            print("Ordem crescente: {}, {}, {}".format(A, C, B))
    elif B <= A and B <= C:
        if A <= C:
            print("Ordem crescente: {}, {}, {}".format(B, A, C))
        else:
            print("Ordem crescente: {}, {}, {}".format(B, C, A))
    else:
        if A <= B:
            print("Ordem crescente: {}, {}, {}".format(C, A, B))
        else:
            print("Ordem crescente: {}, {}, {}".format(C, B, A))
except ValueError:
    print("Valor inválido! Por favor, digite um número inteiro.")
