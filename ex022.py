nome = str(input('qual seu nome? ')).strip()
print(f'SEU NOME É: {nome.upper()}.')
print(f'seu nome é: {nome.lower()}.')
new_nome = nome.split()
new_nome2 = ''.join(new_nome)
print(f'Seu nome tem {len(new_nome2)} letras.')
print(f'Seu primeiro nome tem {len(new_nome[0])} letras.')
