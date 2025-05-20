salario_anual = float(input("Digite o salario anual: "))

if salario_anual > 40000.00:
    imposto = salario_anual * 0.275
    print(f"pague R${imposto:.2f}")
elif salario_anual > 28000.00:
    imposto = salario_anual * 0.15
    print(f"pague R${imposto:.2f}")
else:
    print("isento de impostos")