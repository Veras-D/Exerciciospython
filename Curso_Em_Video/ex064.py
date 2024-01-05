"""
Soma de elementos a determinar
Date: 01/05/23
Author: Veras
"""
list = [0]
num = -1
while num != 0:
    num = float(input("Digite um numero [Digite 0 para parar]: "))
    if num != 0:
        list.append(num)
    else:
        pass
print(f"A soma dos {len(list)-1} elementos é: {sum(list)}")
