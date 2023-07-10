# condições aninhadas
# elif
nome = str(input('Qual seu nome? '))
if nome == 'Danilo':
    print('Que nome legal.')
elif nome == 'João' or nome == 'Maria' or nome == 'Paulo':
    print('Que nome popular.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Que nome bonito voce tem.')
else:
    print('Que nome normal.')
print(f'Tenha um bom dia, {nome}.')
