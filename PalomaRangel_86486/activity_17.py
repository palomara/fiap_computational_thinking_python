valor_produto = float(input("Insira o valor do produto: "))

print("Valor do Produto: {:.2f}".format(valor_produto))

if valor_produto < 20.00:
    valor_venda = valor_produto + (valor_produto * 45)/100
    print("Valor de Venda: {:.2f}".format(valor_venda))
else:
    valor_venda = valor_produto + (valor_produto * 30) / 100
    print("Valor de Venda: {:.2f}".format(valor_venda))