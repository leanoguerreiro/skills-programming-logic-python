n = int(input("Digite um valor ímpar para a altura do losango: "))

if n % 2 == 0:
    print("O valor deve ser ímpar!")
else:
    meio = n // 2
    # Parte superior
    for i in range(meio + 1):
        print('\t' * (meio - i) + '\t*' * (2 * i + 1))
    # Parte inferior
    for i in range(meio - 1, -1, -1):
        print('\t' * (meio - i) + '\t*' * (2 * i + 1))