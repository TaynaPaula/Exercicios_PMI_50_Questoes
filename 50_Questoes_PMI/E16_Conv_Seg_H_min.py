#Crie um programa que converta segundos em horas, minutos e segundos.
try:
    segundos = int(input("Digite a quantidade de segundos: "))
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    seg_restantes = segundos % 60
    print(f"{horas}h:{minutos}m:{seg_restantes}s")
except ValueError:
    print("Erro: digite um valor inteiro de segundos.")

#ok