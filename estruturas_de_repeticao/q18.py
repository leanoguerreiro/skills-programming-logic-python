num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

maior = max(num1, num2)

mmc = maior

while True:
    if mmc % num1 == 0 and mmc % num2 == 0:
        print(f"o MMC de {num1} e {num2} é {mmc}")
        break
    mmc = mmc + 1