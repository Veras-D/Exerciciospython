valor = float(input('Qual valor do empréstimo? '))
salario = float(input('Qual o valor do seu salário? '))
parcelas = int(input('Em quantos anos voce planeja pagar o empréstimo? ')) * 12
if parcelas <= 12:
    taxa = 1.1
elif 12 < parcelas <= 60:
    taxa = 1.2
elif 60 < parcelas <= 240:
    taxa = 1.3
prestacao = valor * taxa / parcelas
if prestacao > 0.3 * salario:
    print('Infelizmente seu empréstimo não foi aprovado.')
elif parcelas > 240:
    print('Infelizmente seu empréstimo não foi aprovado.')
else:
    print(f'''Parabens seu empréstimo foi aprovado, voce devera pagar a partir do próximo mes a quantia de 
{prestacao:.2f} reais ao banco.''')
