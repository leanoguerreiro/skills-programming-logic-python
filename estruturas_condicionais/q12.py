idade = int(input("Idade: "))

if idade <= 18:
    print("Plano Junior")
elif 19 <= idade <= 40:
    print("Plano adulto")
elif 41 <= idade <= 60:
    print("Plano Senior")
else:
    print("Plano Master com Coparticipação")