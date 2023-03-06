import datetime
anos_nasc = int(input('Qual ano de nascimento do nadador? '))
ano = datetime.date.today().year
print(ano)
idade = ano - anos_nasc
if idade <= 9:
    print('Classificação MIRIM')
elif 9 < idade <= 14:
    print('Classificação INFANTIL')
elif 14 < idade <= 19:
    print('Classificação JUNIOR')
elif 19 < idade <= 25:
    print('Classificação SENIOR')
elif idade > 25:
    print('Classificação MASTER')
