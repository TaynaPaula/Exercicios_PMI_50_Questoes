#Escreva um programa que calcule e exiba a soma de dois números.
#Escreva um programa que calcule e exiba a soma de dois números.
try:
    ValorA=int(input("Digite o valor de A: "))
    ValorB= int(input("Digite o valor de B:  "))
    Soma=ValorA+ValorB
    print("A soma dos Valores é:",Soma)
except ValueError:
     print("Erro: Por favor, insira um número válido.") 
     
   