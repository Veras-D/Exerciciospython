Num = int(input('Digite um numero: '))
fat = Num
cont = 1
while (Num - cont) > 1:
    fat = fat * (Num - cont)
    cont += 1
print(f'O fatorial é {fat}')
