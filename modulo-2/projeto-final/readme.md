O objetivo deste relatório é treinar o desenvolvimento de queries em POSTGRESQL bem como praticar alguns conceitos de normalização e correção de dados em tabelas. Para isso será realizada uma análise descritiva dos dados contidos nas bases do 
Sistema Nacional de Informações de Defesa do Consumidor (SINDEC- Procons), disponível em: 
https://dados.mj.gov.br/dataset/cadastro-nacional-de-reclamacoes-fundamentadas-procons-sindec

Essa base de dados consiste de Reclamações fundamentadas dos consumidores que não conseguiram
resolver seus problemas por caminhos mais simples, e então necessitam realizar uma audiência para tentativa 
de resolução, o que pode acontecer tanto pela complexidade da demanda, quanto pelo tipo de postura
adotado pelo fornecedor na resolução do conflito.

Para concluir o objetivo deste relatório, primeiramente foi necessario realizar a consolidação dos dados (originalmente
em formato .csv) disponibilizados em arquivos anuais. Foram analisados os dados correspondentes aos anos 2017 a 2021.

Posteriormente foi feita uma avaliação com o intuito de identificar possíveis normalizações ou otimizações a serem feitas nas
tabelas. Por fim, as tabelas organizadas foram importadas em um banco de dados POSTGRESQL onde foram feitas as queries
para análise dos dados.

O relatório final atualizado pode ser visualizado no arquivo "Procon_Kelvin_e_Rafael.ipynb".

Trabalho desenvolvido durante o curso LM Tech Data Talents - ministrado pela escola ADA em parceria com a Leroy Merlin por:

Rafael Ribeiro Lima - https://www.linkedin.com/in/rafael-ribeiro-de-lima/

Kelvin Pichinini - https://www.linkedin.com/in/kelvinpichinini/ || https://github.com/KelvinPichinini
