#Escreva um programa que classifique a nota de um aluno.
try:
    B1=float(input("Digite a nota do 1º bimestre: "))
    B2=float(input("Digite a nota do 2º bimestre: "))       
    B3=float(input("Digite a nota do 3º bimestre: "))
    B4=float(input("Digite a nota do 4º bimestre: "))   
    classificacao=(B1+B2+B3+B4)/4
    if classificacao>=6:
     print("APROVADO")       
    elif classificacao>=3 and classificacao<6:
     print("EXAME")
    else:
     print("RETIDO") 
    print("Média Aritmética: ", classificacao)
except ValueError:
    print("Por favor, digite apenas números válidos.")
