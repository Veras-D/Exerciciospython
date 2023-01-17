# cores no terminal
print('\033[0;33;44mTEXTO\033[m')
print('\033[31;40mOlá mundo\033[m')
print('\033[30;43mTESTE\033[m')
print('\033[1;30;47mEXEMPLO\033[m')
print('\033[7;37mLETRA\033[m')
a = 5
b = 3
print(f'Os valores são: \033[31m{a}\033[m e \033[33m{b}\033[m!!!')
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azulesc': '\033[34m',
         'magenta': '\033[35m',
         'azulcla': '\033[36m',
         'cinza': '\033[37m'}
print(f'Os valores são: {(cores["vermelho"])}{a}{(cores["limpa"])} e {(cores["azulesc"])}{b}{(cores["limpa"])}!!!')
nome = 'Danilo'
print(f'Meu nome é {(cores["magenta"])}{nome}{(cores["limpa"])}.')
# estilos
# 0 - nada
# 1 - negrito
# 4 - sublinhado
# 7 - invertido
#
# cores
# 30 - Branco
# 31 - Vermelho
# 32 - Verde
# 33 - Amarelo
# 34 - Azul escuro
# 35 - Magenta
# 36 - Azul claro
# 37 - Cinza
#
# Fundo
# 40 - Branco
# 41 - Vermelho
# 42 - Verde
# 43 - Amarelo
# 44 - Azul escuro
# 45 - Magenta
# 46 - Azul claro
# 47 - Cinza
#
