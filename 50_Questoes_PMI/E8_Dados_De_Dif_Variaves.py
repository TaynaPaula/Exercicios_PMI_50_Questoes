#Crie um programa que calcule a média de três notas.
try:
    n1 = float(input("Digite a 1ª nota: "))
    n2 = float(input("Digite a 2ª nota: "))
    n3 = float(input("Digite a 3ª nota: "))
    media = (n1 + n2 + n3) / 3
    print("Média:", media)
except ValueError:
    print("Erro: digite apenas números nas notas.")

#ok