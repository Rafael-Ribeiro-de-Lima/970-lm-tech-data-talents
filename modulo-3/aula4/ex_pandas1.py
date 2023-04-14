import pandas as pd

escolaridade = pd.Series({'Fundamental completo': 451, 'Médio completo': 627, 'Superior completo': 292, 'Pós-graduação completa': 95})

# (a) O número total de inscritos
print(f'Total de inscritos: {escolaridade.sum()}')

# (b) Número inscritos que possuem, pelo menos, o superior completo.
print(f"\nCandidatos com pelo menos o superior completo: {escolaridade[['Superior completo', 'Pós-graduação completa']].sum()}")
# ou print(escolaridade.iloc[[2, 3]].sum())

# (c) Suponha que a inscrição foi prorrogada e, com isso, foi obtido um número adicional de inscrições: 68, 93, 22 e 0 inscritos a mais em cada uma das categorias de escolaridade apresentados na tabela acima (na mesma ordem). Assim, crie uma nova Series com esses valores.
novos_inscritos = pd.Series({'Fundamental completo': 68, 'Médio completo': 93, 'Superior completo': 22, 'Pós-graduação completa': 0})
print(f'\nNovos inscritos: \n{novos_inscritos}')

# (d) Utilizando as duas Series que você tem, calcule o número total de inscritos após a prorrogação do período de inscrições.
total_escolaridade = escolaridade + novos_inscritos
print(f'\nTotal final de inscritos: \n{total_escolaridade}')


