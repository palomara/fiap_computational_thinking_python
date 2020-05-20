opcao = int(input("|———- Menu de Opções ——-—|\n1 - Gerar dígitos verificadores\n2 - Verificar dífitos verificadores"
                  "\n3 - Estado de origem\n4 - Sair"))

def gerar_digitos_cpf(numero_cpf):

def verificar_digitos_cpf(numero_cpf):

def estado_origem_cpf(numero_cpf):



while opcao != 4:
    if opcao == 1:
        cpf = input("Digite o número do CPF sem os dígitos verificadores: ")
    elif opcao == 2:
        cpf = input("Digite o número do CPF incluindo os dígitos verificadores: ")
    elif opcao == 3:
        cpf = input("Digite o número do CPF incluindo os dígitos verificados: ")
    elif opcao == 4:
        print("Fechando programa...")
        break
    else:
        print("Opção inválida!")