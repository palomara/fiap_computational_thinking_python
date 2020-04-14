numero = int(input("Digite um numero inteiro: "))

if numero % 5 == 0 and numero % 10 == 0:
    print("O numero ", numero, "é multiplo de 5 e 10.")
else:
    print("O numero ", numero, "não é multiplo de 5 e 10.")