N = str(input('Qual seu nome: ')).strip()
print(f'Muito prazer {N}!')
L = N.split()
print(f'Seu primeiro nome é: {L[0]}.')
NV = len(L) - 1
print(f'Seu ultimo nome é: {L[NV]}.')
# O [-1] pode ser utilizado para se referir ao último objeto de uma lista, assim como [-2] seria a penúltima e assim
# por diante.
