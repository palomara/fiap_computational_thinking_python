primeiro_numero = int(input("Esse programa irá exibir três números *inteiros* em ordem crescente.\n"
                            "Insira o primeiro número: "))
segundo_numero = int(input("Segundo número: "))
terceiro_numero = int(input("Terceiro número: "))

print(primeiro_numero, "-", segundo_numero, "-", terceiro_numero)

if primeiro_numero < segundo_numero < terceiro_numero:
    print("Ordem crescente: ", primeiro_numero, "-", segundo_numero, "-", terceiro_numero)
elif primeiro_numero < terceiro_numero < segundo_numero:
    print("Ordem crescente: ", primeiro_numero, "-", terceiro_numero, "-", segundo_numero)
elif segundo_numero < primeiro_numero < terceiro_numero:
    print("Ordem crescente: ", segundo_numero, "-", primeiro_numero, "-", terceiro_numero)
elif segundo_numero < terceiro_numero < primeiro_numero:
    print("Ordem crescente: ", segundo_numero, "-", terceiro_numero, "-", primeiro_numero)
elif terceiro_numero < segundo_numero < primeiro_numero:
    print("Ordem crescente: ", terceiro_numero, "-", segundo_numero, "-", primeiro_numero)
elif terceiro_numero < primeiro_numero < segundo_numero:
    print("Ordem crescente: ", terceiro_numero, "-", primeiro_numero, "-", segundo_numero)
elif primeiro_numero == segundo_numero and segundo_numero == terceiro_numero:
    print("Os três números digitados são iguais.")