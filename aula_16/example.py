def reajuste_salario(valor_sal):
    valor_reajustado = valor_sal * 1.45
    return valor_reajustado

salario = (float(input("Digite seu salário: ")))
reajuste = reajuste_salario(salario)
print("Salário reajustado: ", reajuste)
