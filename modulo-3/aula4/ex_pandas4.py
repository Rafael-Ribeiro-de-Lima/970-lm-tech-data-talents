import pandas as pd

# Carregue, em um objeto DataFrame, o arquivo CSV que você salvou no item (f) da questão anterior. Em seguida,

pessoas = pd.read_csv('Peso_Altura.csv', index_col=[0])

# (a) Crie uma nova coluna que contenha o nome das pessoas (sinta-se à vontade para atribuir os nomes que preferir).# 
pessoas['Nome'] = ['Juan', 'Gilberto', 'Rafael', 'Maria', 'Joana']

# (b) Defina a nova coluna criada (com os nomes) como o índice (index) do seu DataFrame.
pessoas = pessoas.set_index('Nome')
print(pessoas)

# (c) Obtenha o nome das pessoas que são classificadas com Sobrepeso (IMC entre 25 e 29,9).
sobrepeso = pessoas[pessoas['IMC'].between(25, 29.9)]
print(sobrepeso)



