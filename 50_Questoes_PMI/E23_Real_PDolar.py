#Escreva um programa que converta uma quantia em reais para dólares.
try:
    TaxaCambio = float(input("Por favor, informe a taxa de câmbio: "))
    ValorReal = float(input("Por favor, informe o valor para conversão: "))
    Conversao = ValorReal / TaxaCambio
    print(f"O valor R$ {ValorReal:.2f}, com câmbio de {TaxaCambio:.2f}, fica: {Conversao:.2f}.")
except ValueError:
    print("Digite valores válidos, por favor.")
except ZeroDivisionError:
    print("O número informado não pode ser zero.")
