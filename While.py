import time
cont = 0
while cont < 10:
    print(cont)
    cont = cont + 1
    time.sleep(1)
    if cont == 6:
        break
print('Acabou a contagem.')
