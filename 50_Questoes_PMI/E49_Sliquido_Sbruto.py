#Crie um programa que calcule o salário líquido com base no salário bruto.
try:
    H=float(input("Digite a quantidade de horas trabalhadas: "))
    ValorH=float(input("Digite o valor por hora trabalhada: ")) 
    Desc=float(input("Digite o percentual de desconto (sem o %): "))
    SalarioBruto=H*ValorH
    Desconto=(Desc/100)*SalarioBruto    
    SalarioLiquido=SalarioBruto-Desconto
    print("Salário Bruto: R$ {:.2f}".format(SalarioBruto))
    print("Desconto: R$ {:.2f}".format(Desconto))   
    print("Salário Líquido: R$ {:.2f}".format(SalarioLiquido))
except ValueError:
    print("Valor inválido! Por favor, digite um número válido.")
