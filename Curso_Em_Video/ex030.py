num = int(input('Digite um numero: '))
print(num % 2)
if (num % 2) == 0:
    print(f'{num} é um número par.')
elif num % 2 == 1:
    print(f'{num} é um número impar.')