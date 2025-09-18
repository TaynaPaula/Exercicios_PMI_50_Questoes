#Escreva um programa que verifique se um número é par ou ímpar.
try:
    x = int(input("Por favor, digite um número para verificação: "))
    if x % 2 == 0:
        print("%d é par" % x)
    else:
        print("%d é ímpar" % x)
    print("Programa encerrado.")
except:
    print("Valor informado não é válido")