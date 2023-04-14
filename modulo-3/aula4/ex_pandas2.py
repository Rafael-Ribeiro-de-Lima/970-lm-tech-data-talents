import pandas as pd

# (a) Crie uma Series com os valores da tabela acima.
notas = pd.Series([2, 7, 5.5, 10, 6.2], index=['Wilfred', 'Abbie', 'Harry', 'Julia', 'Carrie'])
print(f'Notas: \n{notas}')

# (b) Retorne o número de alunos que foram aprovados (considerando que a nota mínima para a aprovação é 7).
print(f'\nAprovados: \n{(notas>=7).sum()}')

# (c) Qual foi a nota média da turma.
print(f'\nMédia: \n{notas.mean()}')

# (d) Obtenha o nome dos alunos que tiraram notas acima da média da turma.
print(f'\nAcima da média da turma: \n{notas[notas>=notas.mean()].index.tolist()}')



