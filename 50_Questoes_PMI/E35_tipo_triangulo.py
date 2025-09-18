# Crie um programa que determine o tipo de triângulo
try:
    Angulo1 = int(input("Digite o valor do ângulo 1: "))
    Angulo2 = int(input("Digite o valor do ângulo 2: "))
    Angulo3 = int(input("Digite o valor do ângulo 3: "))

    SomaAngulos = Angulo1 + Angulo2 + Angulo3

    if SomaAngulos == 180 and Angulo1 > 0 and Angulo2 > 0 and Angulo3 > 0:
        if Angulo1 == 90 or Angulo2 == 90 or Angulo3 == 90:
            print("Triângulo Retângulo: pois possui um ângulo reto (90 graus)")
        elif Angulo1 < 90 and Angulo2 < 90 and Angulo3 < 90:
            print("Triângulo Acutângulo: pois todos os ângulos são agudos (menores que 90 graus)")
        else:
            print("Triângulo Obtusângulo: pois possui um ângulo obtuso (maior que 90 graus)")
    else:
        print("Os ângulos informados não formam um triângulo válido")

except ValueError:
    print("Valor do ângulo informado não é válido")

