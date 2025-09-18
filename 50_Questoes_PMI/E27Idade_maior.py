#Crie um programa que verifique se uma pessoa é maior de idade.

idade=int(input("Por Favor informe a sua Idade: "))
nome=input("Por favor informa o seu nome: ")
if idade>=18:
    print(f"{nome}, você tem {idade} anos,é maior de idade, já pode pagar os boletos.")
else:
     print(f"{nome}, você tem {idade} anos, é menor de idade, continue estudando.")
