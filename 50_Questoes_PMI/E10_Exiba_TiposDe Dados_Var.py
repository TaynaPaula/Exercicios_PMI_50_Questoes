# Crie um programa que exiba os tipos de dados de diferentes variáveis.
texto = "Morango"
b = 8
a = "9"
c = int(input("Digite um número: "))
d = input("Digite seu nome: ")
v = 'outro'
t = '9pula8pula7pula6pula5'
A = True

print(f"v = {v} | id = {id(v)} | tipo = {type(v)}")
print(f"texto = {texto} | tipo = {type(texto)}")
print(f"b = {b} | tipo = {type(b)}")
print(f"a = {a} | tipo = {type(a)}")
print(f"c = {c} | tipo = {type(c)}")
print(f"d = {d} | tipo = {type(d)}")
print(f"f-string 'v = {v}' | tipo = {type(f'v = {v}')}") 
print(f"tamanho de t = {len(t)} | tipo = {type(t)}")
print(f"t fatiado (0:21:5) = {t[0:21:5]} | tipo = {type(t)}")  # de 5 em 5
print(f"t fatiado (::5) = {t[::5]} | tipo = {type(t)}")        # de 5 em 5
print(f"A = {A} | tipo = {type(A)}")
print(f"not A = {not A} | tipo = {type(not A)}")


#ok