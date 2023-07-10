from math import e, log, sin
import sympy
import pandas as pd

cod = 0
n = 0
x = sympy.symbols('x')

a = 1.5
b = 2

x0 = (a + b) / 2
num = 2  # número de casas decimais confiáveis
erro = 10 ** -num
n_max = 100  # número máximo de iterações

fun = f'({x}/2)**2 - sin({x})'

f_x0 = sympy.sympify(fun).subs({x: x0})
k = (log(b - a) - log(erro)) / log(2)

n_values = []
a_values = []
b_values = []
x0_values = []
interval_values = []

if f_x0 >= erro:
    print(f'Valor de x0: {x0}')
else:
    # Loop principal para encontrar a raiz
    while abs(a - b) > erro and n < n_max:
        x0 = (a + b) / 2

        # Avaliação da função nos pontos a, b e x0
        f_a = eval(str(sympy.sympify(fun).subs({x: a})))
        f_b = eval(str(sympy.sympify(fun).subs({x: b})))
        f_x0 = eval(str(sympy.sympify(fun).subs({x: x0})))

        # Verificação de condições para atualizar os limites do intervalo
        if f_a * f_x0 < 0:
            b = x0

        elif f_b * f_x0 < 0:
            a = x0

        else:
            cod = 1
            break

        # Adicionar valores às listas
        a_values.append(a)
        b_values.append(b)
        x0_values.append(x0)
        interval_values.append(b - a)

        n += 1

    # Verificação do resultado
    if cod == 0:
        # Criar DataFrame com os valores
        df = pd.DataFrame({
            'a': a_values,
            'b': b_values,
            'x0': x0_values,
            'Erro': interval_values
        })

        df.index = df.index + 1

        # Exibir o DataFrame
        print(f'{df}\n')
        print(f'k > {k}')
        print(f'Valor de a: {a}')
        print(f'Valor de b: {b}')
        print(f'Valor de x0: {x0}')

    else:
        print('Não há raiz no intervalo')
