#Escreva um programa que calcule a idade em dias.
#idade = (anos × 365) + (meses × 31) + dias 
ano=int(input("Digite o ano do seu nascimento: "))
mes=int(input("Digite ome que você nasceu: "))
dia=int(input("Digite o dia que você nasceu: "))

anoatual=int(input("Digite o ano atual: "))
mesAtual=int(input("Digite o mês atual: "))
diaAtual=int(input("Digite o dia atual: "))

meses=mesAtual-mes
anos=anoatual-ano
dias=diaAtual-dia

idade=(anos*365)+(meses*31)+dias

print(f"Sua idade em dias é: {idade} dias")