numero = int(input("Digite um número de 0 a 30 ou de 40 a 79: "))

if 0 <= numero <= 30:
    print("O numero ", numero, " está entre 0 e 30.")
elif 40 <= numero <= 79:
    print("O numero ", numero, " está entre 40 e 79.")
else:
    print("O numero está fora dos limites estabelecidos.")