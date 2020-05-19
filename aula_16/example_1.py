def reajuste_salario(salario, reajuste):
    valor_reajustado = salario + (salario * reajuste/100)
    print("Salário reajustado:", valor_reajustado)

sal = float(input("Digite seu salário:"))
perc_reajuste = (int(input("Digite o percentual para reajuste: ")))

reajuste_salario(sal, perc_reajuste)