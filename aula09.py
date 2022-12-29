frase = 'Hello, amongus'
print(frase[7:14:2])
# começa do 7, mas só vai até o 13
print(frase[7:])
print(frase[1::2])
print(frase[::2])
print(len(frase))
# len analisa a variável frase e diz quanto caracteres ela possui
print(frase.count('o', 0, 5))
# count conta quantas vezes a str 'o' aparece na variável frase
print(frase.find('gus'))
# procura e mostra on de esta a str 'gus' na variável frase, se a str não existir retorna o valor -1
print('ll' in frase)
# mostra se a str 'll' existe na variável frase
print(frase.replace('Hello', 'Shup up'))
# replace troca as str
print(frase.upper())
# upper deixa os caracteres da variável frase maiúsculos
print(frase.lower())
# deixa os caracteres da variável frase em minusculo
print(frase.capitalize())
# capitalize deixa a primeira letra maiúscula e todas as outras minusculas
print(frase.title())
# deixa a primeira letra de cada palavra maiúscula e o resto minuscula
frase2 = '   TEXTO TEXTO2   '
print(frase2.strip())
# “strip” remove espaços inúteis do início e do final da frase
print(frase2.rstrip())
# remove os espaços inúteis do final ou da direita, o r é de right
print(frase2.lstrip())
# remove os espaços inúteis do início ou da esquerda, o l é de left
f21 = frase2.split()
print(f21)
# cria uma lista com todas as palavras da frase
print('-'.join(f21))
# separa as paravas por um caractere qualquer
print(f21[0])
print(f21[0][2])
