#Crie um programa que verifique se uma data é válida (formato simples).
ano = int(input("Digite o ano: "))
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))

if (dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 0
    or (mes == 2 and dia > 28)
    or (mes in [4, 6, 9, 11] and dia == 31)):
    print("Data não válida")
else:
    print("Data válida")
