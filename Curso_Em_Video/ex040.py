from statistics import *
nota_1 = float(input('Qual a primeira nota? '))
nota_2 = float(input('Qual a segunda nota? '))
nota = mean([nota_1, nota_2])
if nota >= 7:
    print(f'A media é {nota}, está aprovado.')
elif 5 <= nota < 7:
    print(f'Com a media {nota}, o aluno esta de recuperação.')
else:
    print(f'Com a media {nota}, o aluno está reprovado.')
