"""
Analise de Produtos
Date: 24/05/06
Author: Veras-D
"""
import pandas as pd

cont = 'S'
produtos = []
prices = []

print('Loja\n')
while cont == 'S':
    produto = str(input('Produto: '))
    produtos.append(produto)
    price = float(input('Preço: '))
    prices.append(price)
    cont = str(input('Continuar[S/N]: ')).upper().strip()[0]

dados = pd.DataFrame({
                      'Produto': produtos,
                      'Price': prices
                      })
min_prod = dados[dados.Price == dados.Price.min()].Produto.values[0]
text = f"""
Total em compras: {sum(dados.Price)}
A quantidade de produtos que custam mais de 1000 reais é: {len(dados[dados.Price > 1000])}
O produto mais barato é {min_prod} custando {dados.Price.min()}
"""
print(text)
