import numpy as np
import matplotlib.pyplot as plt

np.random.seed = 4

# Definindo as características dos clusters
cluster_0_centro = [0.5, 0.5]
cluster_0_desvio_padrao = 0.5

cluster_1_centro = [1, 1]
cluster_1_desvio_padrao = 0.5

# Gerando dados para o cluster 0
X_cluster_0 = np.random.randn(15, 2) * cluster_0_desvio_padrao + cluster_0_centro
Y_cluster_0 = np.zeros(15)

# Gerando dados para o cluster 1
X_cluster_1 = np.random.randn(15, 2) * cluster_1_desvio_padrao + cluster_1_centro
Y_cluster_1 = np.ones(15)

# Concatenando os dados dos dois clusters
X = np.concatenate((X_cluster_0, X_cluster_1))
Y = np.concatenate((Y_cluster_0, Y_cluster_1))

# Plotando os dados
plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.xlabel('Característica X')
plt.ylabel('Característica Y')
plt.title('Conjunto de dados')
plt.show()
