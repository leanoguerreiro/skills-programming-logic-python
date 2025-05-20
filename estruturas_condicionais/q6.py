salario_bruto = float(input("Informe seu salario: "))

prestacao = float(input("Informe o valor da prestacao do emprestimo: "))

if prestacao >= salario_bruto * 0.3 :
    print(f"voce não pode realizar o emprestimo")
else:
    print(f"voce pode realizar o emprestimo!")