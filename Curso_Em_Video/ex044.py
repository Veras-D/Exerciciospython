"""
Programa para definir o valor final de pagamento a uma loja a partir do valor e da quantidade de parcelas
Autor: Veras-D
Data: 08/03/23
"""
valor = float(input('Qual o preço da compra? '))
print('''[ 1 ]   -   Pagamento à vista
[ 2 ]   -   Pagamento à vista no cartão
[ 3 ]   -   Pagamento 2X no cartão
[ 4 ]   -   Pagamento 3X ou mais no cartão''')
escolha = int(input('Escolha uma opção: '))
if escolha == 1:
    n_valor = valor * 0.9
    print(f'''A comprar de {valor:.2f} reais, fica {n_valor:.2f} reais com o desconto do pagamento à vista, obrigado 
pela preferencia.''')
elif escolha == 2:
    n_valor = valor * 0.95
    print(f'''A comprar de {valor:.2f} reais, fica {n_valor:.2f} reais com o desconto do pagamento à vista no cartão, 
obrigado pela preferencia.''')
elif escolha == 3:
    parcela = valor / 2
    print(f'''A comprar de {valor:.2f} reais, foi parcelada em duas vezes no cartão sendo o valor da parcela 
{parcela:.2f} reais, obrigado pela preferencia.''')
elif escolha == 4:
    n_parcelas = int(input('Em quantas vezes deseja parcelar? '))
    if n_parcelas == 1:
        n_valor = valor * 0.95
        print(f'''A comprar de {valor:.2f} reais, fica {n_valor:.2f} reais com o desconto do pagamento à vista no 
cartão, obrigado pela preferencia.''')
    elif n_parcelas == 2:
        parcela = valor / n_parcelas
        print(f'''A comprar de {valor:.2f} reais, foi parcelada em duas vezes no cartão sendo o valor da parcela 
{parcela:.2f} reais, obrigado pela preferencia.''')
    elif n_parcelas > 2:
        n_valor = valor * 1.2
        parcela = n_valor / n_parcelas
        print(f'''A comprar de {valor:.2f} reais, foi parcelada em {n_parcelas} vezes no cartão sendo o valor da parcela 
{parcela:.2f} reais, obrigado pela preferencia.''')
    else:
        print('Opção invalida.')
else:
    print('Opção invalida.')
