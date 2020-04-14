lado_a = float(input("\tTIPO DE TRIÂNGULO\nInsira valor do lado A: "))
lado_b = float(input("Insira valor do labo B: "))
lado_c = float(input("Insira valor do lado C: "))

if lado_a <= 0 or lado_b <=0 or lado_c <=0:
    print("Valores nulos ou negativos.")

if lado_a >= lado_b + lado_c or lado_b >= lado_c + lado_a or lado_c >= lado_a + lado_b:
    print("Valores não formam um triângulo")
else:
    if lado_a == lado_b and lado_b == lado_c:
        print("Triangulo equilátero")
    elif lado_a == lado_b or lado_b == lado_c or lado_c == lado_a:
        print("Triangulo isósceles")
    else:
        print("Triangulo escaleno.")