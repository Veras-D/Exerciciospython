import statistics
nomes, nomes_h, idades_homens, idades, idades_m_20, sexos, N = [], [], [], [], [], [], 0
for cont in range(1, 5):
    print('-'*5 + f'{cont}° Pessoa' + '-'*5)
    nome = str(input('Nome: '))
    nomes.append(nome)
    idade = int(input('Idade: '))
    idades.append(idade)
    sexo = str(input('Sexo [M/F]: ')).upper()
    if sexo == 'M':
        sexos.append(1)
        idades_homens.append(idade)
        nomes_h.append(nome)
    elif sexo == 'F':
        sexos.append(0)
        if idade < 20:
            idades_m_20.append(idade)
    else:
        sexos.append(-1)
        N += 1
media = statistics.mean(idades)
idades_homens_ord = sorted(idades_homens)
print(f'A média da idade do grupo é {media}. \nO homem mais velho se chama '
      f'{nomes_h[idades_homens.index(idades_homens_ord[len(idades_homens_ord) - 1])]} e tem '
      f'{idades_homens_ord[len(idades_homens_ord) - 1]}. \nAo todo são {len(idades_m_20)} mulheres '
      f'com menos de 20 anos.')
