try:
    Lado1 = int(input("Digite o lado1 do triângulo: "))
    Lado2 = int(input("Digite o lado2 do triângulo: "))
    Lado3 = int(input("Digite o lado3 do triângulo: "))

    # Verifica se forma triângulo válido
    if (Lado1 + Lado2 > Lado3) and (Lado2 + Lado3 > Lado1) and (Lado1 + Lado3 > Lado2):
        if Lado1 == Lado2 == Lado3:
            print("Triângulo Equilátero: pois todos os lados são iguais")
        elif Lado1 != Lado2 and Lado2 != Lado3 and Lado1 != Lado3:
            print("Triângulo Escaleno: pois todos os lados são diferentes")
        else:
            print("Triângulo Isósceles: pois dois lados são iguais")
    else:
        print("Os lados informados não formam um triângulo válido")
except ValueError:
    print("Valor informado não é válido")
