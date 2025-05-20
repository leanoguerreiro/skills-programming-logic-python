minutos = int(input("Digite os minutos da ligacao: "))

tipo_ligacao = (input("Digite o tipo de ligacao: "))


if tipo_ligacao == "local":
    if minutos > 3:
        taxa = 0.5 + (minutos - 3) * 0.1
    else:
        taxa = 0.5
elif tipo_ligacao == "nacional":
    if minutos > 3:
        taxa = 1 + (minutos - 3) * 0.25
    else:
        taxa = 1
elif tipo_ligacao == "internacional":
    if minutos > 3:
        taxa = 2 + (minutos - 3) * 0.60
    else:
        taxa = 2
else:
    print("Tipo de ligação inválido.")
    taxa = None

if taxa is not None:
    print(f"Total: R$ {taxa:.2f}")