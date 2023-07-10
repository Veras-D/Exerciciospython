import time
# estrutura de repetição for
for cont in range(0, 6):
    print('oi')
print('fim')
for cont in range(1, 6):
    print(cont)
print('-' * 20)
for cont in range(5, 0, -1):
    print(cont)
    time.sleep(1)
num = int(input('numero: '))
for cont in range(1, num):
    print(cont)
for cont in range(num, 0):
    print(cont)
i = int(input('inicio: '))
f = int(input('final: ')) + 1
inter = int(input('intervalo: '))
for cont in range(i, f, inter):
    print(cont)
s = 0
for cont in range(0, 4):
    n = int(input('numero: '))
    s = s + n
    # ou
    # s += n
print(s)