print('Progressão aritmética indeterminada')
num = float(input('Digite A0: '))
R = float(input('Digite a razão: '))
c = 1
n = 1
t = 0
stop = 1
quant = int(input('Quantos termos você precisa: '))
if quant == 0:
    stop = 0
    print('Programa finalizado')
while stop != 0:
    if c <= quant:
        a = num + (n - 1) * R
        print(a, end=' -> ')
        c += 1
        n += 1
        t += 1
    elif c > quant:
        print('PAUSA')
        c = 1
        quant = int(input('Quantos termos você precisa: '))
        if quant == 0:
            stop = 0
print(f'A progressão foi finalizada com {t} termos.')
