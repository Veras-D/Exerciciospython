soma = 0
contador = 0
for cont in range(3, 500, 3):
    if cont % 2 == 1:
        contador += 1
        soma = soma + cont
print(f'Os {contador} números somados são iguais a {soma}.')
