Nome = str(input('Qual seu nome? ')).strip()
N_Nome = (Nome.title().split())
N_N_Nome = bool('Silva' in N_Nome)
if N_N_Nome:
    print('Seu nome tem Silva.')
else:
    print('Seu nome não tem Silva')
