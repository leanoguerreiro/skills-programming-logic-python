print(f"informe uma data no formato dd/mm/aaaa")
dia1 = int(input("dia: "))
mes1 = int(input("mês: "))
ano1 = int(input("ano: "))

print(f"informe outra data no formato dd/mm/aaaa")
dia2 = int(input("dia: "))
mes2 = int(input("mês: "))
ano2 = int(input("ano: "))

data_1 = ano1 * 365 + mes1 * 30 + dia1
data_2 = ano2 * 365 + mes2 * 30 + dia2

diferenca = abs(data_1 - data_2)

dias = diferenca


print(f" diferenca de dias entre a data {dia1}/{mes1}/{ano1} e a data {dia2}/{mes2}/{ano2} é de {dias} dias.")
