inicio = int(input("insira um numero: "))
fim = int(input("insira outro numero: "))

for i in range(inicio, fim +1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)