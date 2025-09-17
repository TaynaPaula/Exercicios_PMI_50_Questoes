#Escreva um programa que calcule a área de um triângulo.
try:
    base= int(input("Digite a base do triângulo "))
    altura=(int(input("Digite a altura de um triângulo")))
    area=((base*altura)/2)
    print("Area é: ", area)
except ValueError:
    print("Erro: Por favor, insira um número válido.")


#ok