from funcoes import soma
from funcoes import subtracao
from funcoes import divisao
from funcoes import multiplicacao


def calcule():
    a = input('Digite um valor: ')
    b = input('Digite um segundo valor: ')

    while True:
        funcao = input('Escolha a função desejada (+, -, /, *): ')
        funcs = {'+': soma, '-': subtracao, '/': divisao, '*': multiplicacao}
        if funcao in funcs:
            break
    
    print(funcs[funcao](a, b))

calcule()


