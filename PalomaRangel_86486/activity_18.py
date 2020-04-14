opcao = int(input("\tMenu de Opções\n1. Somar dois números\n2. Raiz quadrada de um número\nDigite a opção desejada: "))

if opcao == 1:
    num_1 = int(input("Insira o primeiro número: "))
    num_2 = int(input("Insira o segundo número: "))
    soma = num_1 + num_2
    print("A soma de ", num_1, " com ", num_2, " é: ", soma)
elif opcao == 2:
    numero = float(input("Digite um número: "))
    raiz = numero ** 0.5
    print("A raiz quadrada de ", numero," é", raiz)
else:
    print("Opção inexistente!")