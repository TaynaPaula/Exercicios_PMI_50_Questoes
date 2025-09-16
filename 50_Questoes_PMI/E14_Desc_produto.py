#Crie um programa que calcule o desconto de um produto.
ValorProduto=float(input("Informe o valor do produto "))
Desc=float(input("Digite o percentual de desconto (sem o %): "))
ProdutoFinal=ValorProduto-(ValorProduto*(Desc/100))
print(f"O valor final do produto com desconto é: R$ {ProdutoFinal:.3f}")

#ok