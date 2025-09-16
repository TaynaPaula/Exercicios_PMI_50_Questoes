#Crie um programa que converta segundos em horas, minutos e segundos.
a=int(input("Digite a quantidade de segundos: "))
hora = a // 3600                
resto = a % 3600              
minutos = resto // 60            
segundos = resto % 60            

print(f"{a} segundos equivalem a {hora}h:{minutos}m:{segundos}s")