"""
Este programa lê a idade do usuário é prevê se ele deve ou não se alistar
Autor: Veras-D
Data: 21/02/23
"""
import datetime
ano = int(datetime.date.today().year)
print('''Qual seu gênero? 
[1] - Masculino
[2] - Feminino''')
genero = input()
if genero == 1:
    ano_nasc = int(input('Qual seu ano de nascimento? '))
    idade = ano - ano_nasc
    if idade != 0 or idade == 0:
        if idade > 18:
            print(f'Você possui mais de 18 anos seu alistamento foi há {idade - 18} ano(s).')
        elif idade == 18:
            print('Você possui 18 anos e deve comparecer ao quartel IMEDIATAMENTE para se alistar!')
        elif idade < 18:
            print(f'Você ainda não possui 18 anos deve aguardar {18 - idade} ano(s) para sse alistar.')
    else:
        print('Viajante do tempo?')
elif genero == 2:
    print(f'Seu alistamento não é obrigatório, insira {0} caso queira se alistar')
    alist = input()
    if alist == 0:
        ano_nasc = int(input('Qual seu ano de nascimento? '))
        idade = ano - ano_nasc
        if idade != 0 or idade == 0:
            if idade > 18:
                print(f'Você possui mais de 18 anos seu alistamento foi há {idade - 18} ano(s).')
            elif idade == 18:
                print('Você possui 18 anos e deve comparecer ao quartel IMEDIATAMENTE para se alistar!')
            elif idade < 18:
                print(f'Você ainda não possui 18 anos deve aguardar {18 - idade} ano(s) para sse alistar.')
        else:
            print('Viajante do tempo?')
    else:
        print('Certo, tenha um bom dia.')
