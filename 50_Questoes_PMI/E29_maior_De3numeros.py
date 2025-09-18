#Crie um programa que determine o maior entre três números
try:
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))
    C = int(input("Digite o valor de C: "))

    if A > B and A > C:
        print(f"O maior valor é A: {A}")
    elif B > A and B > C:
        print(f"O maior valor é B: {B}")
    else:
        print(f"O maior valor é C: {C}")
except ValueError:
    print("Digite apenas números válidos.")
