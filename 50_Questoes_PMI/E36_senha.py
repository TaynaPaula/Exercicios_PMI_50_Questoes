#Escreva um programa que verifique se uma senha é válida.
senha_correta = "Coelho"
print("Bem vindo ao sistema de verificação de senha. #Dica: um animal de pelo branco.")
senha_digitada = input("Digite a senha: ")
if senha_digitada == senha_correta:
    print("Acesso permitido. Senha correta! Você vai ganhar ovos de Páscoa esse ano")
else:
    print("Acesso negado. Senha incorreta.")