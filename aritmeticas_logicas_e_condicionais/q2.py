
print("insira apenas numeros inteiros positivos!")

anos_bebendo = int(input("Digite quantos anos voce bebeu: "))
latinhas = int(input("Digite quantos latinhas voce bebeu por dia: "))
preco_latinhas = int(input("Digite o preco de cada latinhas: "))

total_latinhas = anos_bebendo * 360 * latinhas
total_gasto = total_latinhas * preco_latinhas

print(f"Você gastou:")
print(f"R$ {total_gasto} em latinhas de cerveja")