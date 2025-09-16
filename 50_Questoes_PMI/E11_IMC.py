#Escreva um programa que calcule o IMC (Índice de Massa Corporal).
Peso=float(input("Por Favor, informe o seu peso em quilogramas (kg) "))
Altura=float(input("Por favor, informe a sua altura em metros (m) "))
IMC=Peso/(Altura*Altura)
print(f"O IMC Com Peso: {Peso} e Altura: {Altura} é {IMC:.2f}kg/m²" )

