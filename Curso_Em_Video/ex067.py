"""
Tabuada v3
Author: Veras-D
Date: 16/01/24
"""
while True:
    num = int(input("Qual tabuada você deseja ver? [Digite 0 para encenrrar o programa] "))
    if num == 0:
        break
    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")
