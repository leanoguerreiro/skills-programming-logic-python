import math

int1 = int(input("digite um numero inteiro:"))

int2 = int(input("digite mais um numero inteiro:"))

float1 = float(input("digite um numero real:"))

produto = (int1 * 2) * (int2 / 2)

soma = (int1 * 3) + float1

cubo = float1 ** 3

subtracao = abs(int1 - int2)

naoSeiComoDefinirIsso = (int2 ** 2) + math.log(float1, int1)

print(f"""
    produto: {produto:.2f}
    soma: {soma:.2f}
    cubo: {cubo:.2f}
    subtracao: {subtracao:.2f}
    conta: {naoSeiComoDefinirIsso:.2f}
""")