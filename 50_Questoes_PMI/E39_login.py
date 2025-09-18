#Crie um programa que simule um sistema de login.
try:
    senha_correta = "CoelhoP2007"
    usuario_correto = "CoelhoPaulo"="CoelhoPaulo"

    usuario=input("Digite seu nome de usuário: ")
    senha=input("Digite sua senha: ")
    
   
    if usuario==usuario_correto and senha==senha_correta:
        print(f"Bem vindo {usuario_correto}, você está logado no sistema.") 
    else:
        print("Usuário ou senha incorretos. Tente novamente.")  
except ValueError:
    print("Valor informado não é válido")