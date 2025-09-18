#Crie um programa que verifique se um ano é bissexto.
try:
    ano = int(input("Informe o ano para verificação: "))

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano {ano} é bissexto")
    else:
        print(f"O ano {ano} não é bissexto")
except ValueError:
    print("Digite um valor numérico válido.")