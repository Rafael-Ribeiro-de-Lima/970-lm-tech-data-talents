import numpy as np
import matplotlib.pyplot as plt

'''Crie um array com 40 números aleatórios, distribuídos uniformemente, entre [0, 5).

Para cada elemento do array, calcule:

Seno
Cosseno
Log na base 2'''


array = np.random.uniform(0, 5, 40)

sen = np.sin(array)
cos = np.cos(array)
log2 = np.log2(array)

print(f'Array: \n{array}')
print(f'\nSeno: \n{sen}')
print(f'\nCosseno: \n{cos}')
print(f'\nLog2: \n{log2}')

