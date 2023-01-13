s = float(input('Qual seu salario? '))
if s > 1250:
    s = s * 1.1
else:
    s = s * 1.15
print(f'Seu novo salario é: {s:.2f}.')
