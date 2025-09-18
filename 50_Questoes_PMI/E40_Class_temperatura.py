try:
    temp = float(input("Digite a sua temperatura em °C: "))

    if temp < 36:
        print("Hipotermia, vá ao médico")
    elif 36 <= temp <= 37.5:
        print("Normal, você está bem ")
    elif 37.6 <= temp <= 39:
        print("Febre, observe se ocorre outros sintomas")
    else:
        print("Febre alta, vá ao médico")

except ValueError:
    print("Por favor, digite apenas números válidos.")
