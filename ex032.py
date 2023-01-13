import datetime
ano = int(input('Qual ano quer analisar (Digite "0" para analisar o ano atual)? '))
if ano == 0:
    AnoAt = str(datetime.date.today())
    a = int(AnoAt[0:4])
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        print(f'O ano {a} é bissexto.')
    else:
        print(f'O ano {a} não é bissexto.')
elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')
# print(datetime.date.today().year)
