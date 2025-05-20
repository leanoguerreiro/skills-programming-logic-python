pi_aprox = 0
sinal = 1

for i in range(1, 40, 2):
    pi_aprox += sinal * (1 / i)
    sinal *= -1

pi_aprox *= 4
print(f"Aproximação de pi com 20 termos: {pi_aprox}")