from numpy import prod
numero = str(8496478565894279643689906468974784684957).replace('0', '')
ult_num = int(numero[-1])
numero = numero[:-1]
difs = []
for i in numero:
    num_temp = abs(int(numero[-1]))
    dif = abs(ult_num - num_temp)
    ult_num = num_temp
    numero = numero[:-1]
    if dif != 0 and abs(dif) != 1:
        difs.append(dif)
    print(dif)
print(difs)
produto = prod(difs)
print(produto)
