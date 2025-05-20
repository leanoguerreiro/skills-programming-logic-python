numero = int(input("Digite um numero: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("faixa 1")
elif numero % 2 == 0 and numero % 10 == 0:
    print("faixa 2")
elif 100 <= numero <= 1000:
    print("faixa 3")
else:
    print("numero fora das faixas especificadas")