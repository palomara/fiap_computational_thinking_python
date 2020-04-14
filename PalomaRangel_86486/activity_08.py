primeiro_numero = int(input("Esse programa verificará se a soma dos números digitados é maior que 10.\n"
                            "Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

soma = primeiro_numero + segundo_numero

if soma > 10:
    print("Número maior que 10")
elif soma <= 10:
    print("Número menor ou igual a 10")