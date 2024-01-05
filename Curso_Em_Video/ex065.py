"""
Media de elementos a determinar
Date: 01/05/23
Author: Veras
"""
list = []
flag = str("s")
while flag.upper() != "N":
    num = float(input("Digite um numero: "))
    list.append(num)
    flag = str(input("Deseja continuar [S/N]: "))
print(f"A media dos {len(list)-1} elementos é: {sum(list)/(len(list)-1)}")
print(f"O maior elemento é: {max(list)}")
print(f"O menor elemento é: {min(list)}")
