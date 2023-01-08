frase = str(input('Digite uma frase: ')).strip().upper()
frase1 = frase.replace(' ', '')
L = str(input('Qual letras deseja analisar? ')).strip().upper()
Li = frase1.find(L) + 1
Lf = frase1.rfind(L) + 1
N = frase1.count(L)
if Li == 0:
    print(f'Não há letras "{L}" na frase.')
elif Li == Lf:
    print(f'O numero de letras "{L}" na frase é: {N}.')
    print(f'A letra "{L}" apareceu na posição: {Li}.')
else:
    print(f'O numero de letras "{L}" na frase é: {N}.')
    print(f'A primeira letra "{L}" apareceu na posição: {Li}.')
    print(f'A ultima letra "{L}" apareceu na posição: {Lf}.')
