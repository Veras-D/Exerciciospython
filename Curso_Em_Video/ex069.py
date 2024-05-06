"""
Analise de dados
Date: 24/01/26
Author: Veras-D
"""
import pandas as pd

cont = 'S'
idades = []
sexos = []
sex_type = ['M', 'F']

print('CADASTRO\n')
while cont == 'S':
    idade = int(input('Idade: '))
    idades.append(idade)
    sexo = str(input('Sexo[M/F]: ')).upper()
    while sexo not in sex_type:
        sexo = str(input('Sexo[M/F]: ')).upper().strip()[0]
    sexos.append(sexo)
    cont = str(input('Continuar[S/N]: ')).upper().strip()[0]

dados = pd.DataFrame({
                      'Idade': idades,
                      'Sexo': sexos
                      })
text = f"""
Total de pessoas com mais de 18: {len(dados[dados.Idade > 18])}
O total de homens é: {len(dados[dados.Sexo == 'M'])}
E a quantidade de mulheres com menos de 20 anos é: {len(dados.query("Sexo == 'F' & Idade < 20"))}
"""
print(text)
