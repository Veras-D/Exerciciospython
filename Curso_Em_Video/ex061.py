print('Progressão aritmética')
num = float(input('Digite A0: '))
R = float(input('Digite a razão: '))
c = 1
while c < 10:
    a = num + (c - 1) * R
    print(a, end=' -> ')
    c += 1
a = num + (c - 1) * R
print(a)
