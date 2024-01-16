soma = 0
cont = 0
while True:
    num = float(input("Digite um numero [Digite 0 para parar]: "))
    if num != 0:
        soma += num
        cont += 1
    else:
        break
print(f"A soma dos {cont} elementos é: {soma}")
