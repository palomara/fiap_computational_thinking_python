nome = input("Insira o nome do aluno: ")
nota_1 = float(input("Insira a primeira nota: "))
nota_2 = float(input("Insira a segunda nota: "))
nota_3 = float(input("Insira a terceira nota: "))
faltas_qtd = int(input("Insira a quantidade de faltas: "))

if faltas_qtd > (25 * 80)/100:
    print("Reprovado por falta.")
else:
    if (nota_1+nota_2+nota_3)/3 >= 7:
        print("Aprovado!")
    else:
        print("Reprovado por média")