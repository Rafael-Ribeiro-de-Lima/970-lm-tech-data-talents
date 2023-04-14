import pandas as pd

pessoas = pd.DataFrame([[72, 180, 31], [80, 170, 21], [60, 175, 16], [90, 174, 28], [100, 185, 23]], columns=['Peso (kg)', 'Altura (cm)', 'Idade'])

# Com base no DataFrame criado, realize o que pedido nos itens abaixo:

# (a) Visualize apenas os dados da coluna que contém a altura das pessoas.
alturas = pessoas['Altura (cm)']
print(f"Alturas: \n{alturas}")

# (b) Obtenha a idade média das pessoas.
print(f"\nMédia idade: {pessoas['Idade'].mean()}")

# (c) Obtenha os dados das pessoas que estão abaixo da altura média.
print(f"\nAbaixo altura média: \n{pessoas[alturas < alturas.mean()]}\n")

# (d) Crie um nova coluna no DataFrame que contenha o IMC (Índice de Massa Corporal) de cada pessoa.
pessoas['IMC'] = (pessoas['Peso (kg)'] / (alturas/100)**2).round(2)
print(pessoas)

# (e) Remova a coluna que contém a idade das pessoas.
pessoas = pessoas.drop('Idade', axis=1)
print(pessoas)

# (f) Salve esses dados do DataFrame em um arquivo csv.
pessoas.to_csv('Peso_Altura.csv')



