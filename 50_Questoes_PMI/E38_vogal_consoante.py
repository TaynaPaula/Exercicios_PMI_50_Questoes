#Escreva um programa que verifique se um caractere é vogal ou consoante.
try:
    Letra = input("Digite uma letra: ").strip() 

    if len(Letra) != 1 or not Letra.isalpha():
        print("Valor inválido! Digite apenas uma letra.")
    else:
       if Letra.lower() in "aeiou":
        print(f"A letra {Letra} é uma vogal")
       else:
         print(f"A letra {Letra} é uma consoante")
except:
    print("Valor informado não é válido, digite apenas letras.")
