# Escreva um programa que determine o quadrante de um ponto no plano cartesiano
try:
    x = float(input("Digite a coordenada x: "))
    y = float(input("Digite a coordenada y: "))

    if x == 0 and y == 0:
        print("O ponto está na origem.")
    elif x == 0:
        print("O ponto está no eixo Y.")
    elif y == 0:
        print("O ponto está no eixo X.")
    elif x > 0 and y > 0:
        print("O ponto está no 1º quadrante.")
    elif x < 0 and y > 0:
        print("O ponto está no 2º quadrante.")
    elif x < 0 and y < 0:
        print("O ponto está no 3º quadrante.")
    else:
        print("O ponto está no 4º quadrante.")
except ValueError:
    print("Digite apenas números válidos.")
