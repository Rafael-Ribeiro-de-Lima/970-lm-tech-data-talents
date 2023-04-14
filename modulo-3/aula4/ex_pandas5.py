import pandas as pd

# Carregue, em um objeto DataFrame, o mesmo dataset que você salvou na Questão 3. Em seguida,
pessoas = pd.read_csv('Peso_Altura.csv', index_col=[0])

# (a) Adicione uma nova coluna nesse DF chamada Classificação, que contenha a classificação de cada indivíduo, de acordo com o seu IMC. Para isso, consulte a tabela abaixo.

# IMC	Classificação	Obesidade (grau)
# Menor que 18,5	Magreza	0
# Entre 18,5 e 24,9	Normal	0
# Entre 25,0 e 29,9	Sobrepeso	I
# Entre 30,0 e 39,9	Obesidade	II
# Maior que 40,0	Obesidade Grave	III

def classificar(imc):
    if imc < 18.5:
        return 'Magreza'
    elif imc < 25:
        return 'Normal'
    elif imc < 30:
        return 'Sobrepeso'
    elif imc < 40:
        return 'Obesidade'
    else:
        return 'Obesidade Grave'
    
pessoas['Classificação'] = pessoas['IMC'].apply(classificar)

# (b) Salve em DataFrame no formato xlsx.

pessoas.to_excel('Peso_Altura.xlsx')