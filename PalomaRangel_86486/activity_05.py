primeiro_numero = int(input("O programa verificará se as entradas foram feitas de forma crescente.\n"
                            "Digite um número inteiro: "))
segundo_numero = int(input("Digite um segundo número inteiro: "))
terceiro_numero = int(input("Digite um terceiro número inteiro: "))

print(primeiro_numero, "-", segundo_numero, "-", terceiro_numero)

if primeiro_numero < segundo_numero < terceiro_numero:
    print("Os números foram digitados em ordem crescente.")
else:
    print("Os números não foram digitados em ordem crescente.")