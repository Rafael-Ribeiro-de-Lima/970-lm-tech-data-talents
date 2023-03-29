def soma(a, b):
    try:
        return float(a) + float(b)
    except:
        return "Os inputs devem ser do tipo float ou int"
    
def subtracao(a, b):
    try:
        return float(a) - float(b)
    except:
        return "Os inputs devem ser do tipo float ou int"
    
def divisao(a, b):
    try:
        a, b = float(a), float(b)
        if b != 0:
            return a/b
        else:
            return "Divisão por zero!"
    except:
        return "Os inputs devem ser do tipo float ou int"
    


