#Escreva um programa que calcule a hipotenusa de um triângulo retângulo.
a=int(input("Digite o valor do cateto a: "))
b=int(input("Digite o valor do cateto b: "))
hipo=(a**2+b**2)**0.5
print(f"A hipotenusa vai medir {hipo:.2f}")