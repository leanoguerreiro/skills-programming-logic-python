TAXA_DOLAR = 5.5
TAXA_EURO = 6.7
TAXA_IENE = 0.05
IOF = 1 + (6.38 / 100)

valor_em_reais = float(input("Valor em reais: "))
valor_com_iof = IOF * valor_em_reais

dolar = valor_com_iof / TAXA_DOLAR
euro = valor_com_iof / TAXA_EURO
iene = valor_com_iof / TAXA_IENE

print(f"\nValor informado: R$ {valor_em_reais:.2f}")
print(f"Valor com IOF: R$ {valor_com_iof:.2f}")
print(f"Em dólar: US$ {dolar:.2f}")
print(f"Em euro: € {euro:.2f}")
print(f"Em iene: ¥ {iene:.2f}")