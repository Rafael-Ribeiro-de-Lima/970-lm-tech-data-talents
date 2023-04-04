import numpy as np

'1-) Crie um array aleatório de 15 itens entre 0 e 100'

np.random.seed(2)
array = np.random.randint(0, 101, size=15)
print(f'Array: {array}')


'2-) Qual o maior número do array?'

maior = array.max()
print(f'Maior número: {maior}')


'3-) Qual a sua posição?'

pos = np.where(array == maior)[0]
print(f'Índice do maior valor: {pos}')


'4-) Quais números do array são maiores que 10?'

maior_que_10 = np.where(array > 10)[0]
print(f'Números maiores que 10: {maior_que_10}')


'5-) Crie um novo array em que existam apenas elementos entre 10 e 30 (10 e 30 inclusos)'

novo_array = np.random.randint(20, 31, 15)
print(f'Novo array: {novo_array}')