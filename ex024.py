Cidade = str(input('Qual o nome da sua cidade? ')).strip()
p1_Cidade = Cidade.split()
Np1 = str(p1_Cidade[0].capitalize())
santo = bool('Santo' in Np1)
if santo:
    print('O primeiro nome da sua cidade é Santo.')
else:
    print('O primeiro nome da sua cidade não é santo.')
