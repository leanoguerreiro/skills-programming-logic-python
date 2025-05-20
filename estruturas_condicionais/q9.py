a = float(input("Insira o valor do lado 1: "))

b = float(input("Insira o valor do lado 2: "))
c = float(input("Insira o valor do lado 3: "))

if a < b + c and b < a + c and c < a + b:

    if a == b == c:
        print("Triângulo equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")


    if a >= b and a >= c:
        maior = a
        lado1 = b
        lado2 = c
    elif b >= a and b >= c:
        maior = b
        lado1 = c
        lado2 = a
    else:
        maior = c
        lado1 = a
        lado2 = b

    if (maior **2) == (lado1**2)+(lado2**2):
        print("triangulo retangulo")
    elif (maior **2) > (lado1**2)+(lado2**2):
        print("triangulo obtusandulo")
    else:
        print("triangulo acutangulo")
else:
    print("Os lados informado não formam um triangulo")
