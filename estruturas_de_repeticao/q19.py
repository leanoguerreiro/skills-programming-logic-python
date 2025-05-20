for num in range(100, 1000):
    centena = num // 100
    dezena = (num // 10) % 10
    unidade = num % 10
    if num == centena**3 + dezena**3 + unidade**3:
        print(num)