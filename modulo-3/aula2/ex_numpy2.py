import numpy as np

'1-) Crie uma matriz (5, 2) com números igualmente espaçados entre 0 e 100 (utilize o np.linspace)'

matriz = np.linspace(0, 100, 10).reshape(5, 2)
print(matriz)


'2-) Qual o maior valor da matriz?'

maior = matriz.max()
print(f'O maior é: {maior}')


'3-) Qual o valor máximo por linha?'

maior_por_linha = matriz.max(axis=1)
print(f'Os maiores valores em cada linha são: {maior_por_linha}')


'4-) Qual o valor máximo por coluna?'

maior_por_coluna = matriz.max(axis=0)
print(f'Os maiores valores em cada coluna são: {maior_por_coluna}')


'5-) Qual a média por linha?'

media_por_linha = matriz.mean(axis=1)
print(f'Os valores médios em cada linha são: {media_por_linha}')


'6-) Qual a média da matriz?'

media = matriz.mean()
print(f'O valor médio da matriz é: {media}')