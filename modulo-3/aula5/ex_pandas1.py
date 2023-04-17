'''
O arquivo avocado.csv consiste em um dataset que contém dados sobre vendas de abacates (avocado, em inglês) em diversas
regiões dos Estados Unidos. Essa dataset contém as seguintes colunas:

Date - a data da observação
AveragePrice - o preço médio de um único abacate
year - o ano
region - a cidade ou região da observação
Total Volume - volume total de abacates vendidos

Além das informações acima, contidas no arquivo avocado.csv, o tipo do abacate (convencional ou orgânico) 
também seria uma informação importante para a sua análise. Suponhamos que você conseguiu essas informações para cada uma das 
observações do arquivo avocado.csv, na mesma ordem, e salvou-as no arquivo avocado_type.csv. Portanto, tudo o que você precisa
é juntar esses dois arquivos em um mesmo DataFrame. E, em seguida, salve-o em um arquivo csv.
'''

import os
import pandas as pd



df_avocado = pd.read_csv(r'modulo-3\aula5\db\avocado.csv')
df_type = pd.read_csv(r'modulo-3\aula5\db\avocado_type.csv')


df = df_avocado.merge(df_type, left_index=True, right_index=True)

df.to_csv(r'modulo-3\aula5\db\avocado_with_type.csv')




