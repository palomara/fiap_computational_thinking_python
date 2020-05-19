janela = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
corredor = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
opcao = 0

while opcao != 4:
    print('1 - Vender passagem\n2 - Cancelar compra\n3 - Mostrar mapa de ocupação\n4 - Sair')
    opcao = int(input('Digite o número da opção: '))
    if opcao == 1:
        if 0 not in janela and 0 not in corredor:
            print('Ônibus lotado. Opção inválida!')
        else:
            tipo_poltrona = int(input("Selecione o tipo de poltrona:\n1- Janela\n2 - Corredor\n "))
            if tipo_poltrona == 1:
                print(janela)
                poltrona = int(input('Informe o número da poltrona: '))
                if janela[poltrona - 1] == 0:
                    janela[poltrona - 1] = 1
                    print('Venda realizada com sucesso! ')
                else:
                    print('Poltrona ocupada. Venda não realizada!')
            elif tipo_poltrona == 2:
                print(corredor)
                poltrona = int(input("Informe o número da poltrona: "))
                if corredor[poltrona - 1] == 0:
                    corredor[poltrona - 1] = 1
                    print('Venda realizada com sucesso! ')
                    print(corredor)
                else:
                    print('Poltrona ocupada. Venda não realizada!')
            else:
                print('Opção inválida')
            if 0 not in janela and 0 not in corredor:
                print('Ônibus lotado. Opção inválida!')
    elif opcao == 2:
        if 1 not in janela and 1 not in corredor:
            print('Todas as poltronas estão livres. Opção inválida!')
        else:
            cancelamento = int(input('Informe o número da poltrona: '))
            tipo_cancelamento = int(input('Selecione o tipo de poltrona:\n1- Janela\n2 - Corredor\n'))
            if tipo_cancelamento == 1:
                if janela[poltrona - 1] == 1:
                    print('Compra cancelada com sucesso! ')
                else:
                    print('Poltrona livre. Compra não cancelada! ')
            if tipo_cancelamento == 2:
                if corredor[poltrona - 1] == 1:
                    print('Compra cancelada com sucesso! ')
                else:
                    print('Poltrona livre. Compra não cancelada! ')
    elif opcao == 3:
            print("******** Janela ********")
            for i in range(24):
                poltrona = janela[i]
                if poltrona == 0:
                    print(f'{i + 1} - Livre')
                else:
                    print(f'{i + 1} - Ocupada')
            print("******** Corredor ********")
            for i in range(24):
                poltrona = corredor[i]
                if poltrona == 0:
                    print(f"{i + 1} - Livre")
                else:
                    print(f'{i + 1} - Ocupada')
    elif opcao == 4:
        print('Execução finalizada !!!')
        break
    else:
        print('Opção inválida!!')