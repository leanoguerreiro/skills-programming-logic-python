from datetime import datetime

dia = int(input("Digite o dia do seu nascimento: "))
mes = int(input("Digite o mês do seu nascimento: "))
ano = int(input("Digite o ano do seu nascimento: "))

data_nascimento = datetime(ano, mes, dia)
data_atual = datetime.now()


diferenca = data_atual - data_nascimento
dias = diferenca.days

anos = dias // 365
meses = (dias % 365) // 30
dias_restantes = (dias % 365) % 30

minutos = diferenca.total_seconds() // 60
segundos = diferenca.total_seconds()

print(f"Você tem aproximadamente:")
print(f"{anos} anos, {meses} meses e {dias_restantes} dias de vida.")
print(f"{int(minutos)} minutos de vida.")
print(f"{int(segundos)} segundos de vida.")