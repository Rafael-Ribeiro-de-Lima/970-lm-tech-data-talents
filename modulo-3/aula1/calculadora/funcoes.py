def soma(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return float(a) + float(b)
    else:
        raise TypeError("Os inputs devem ser do tipo float ou int")
    
def subtracao(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return float(a) - float(b)
    else:
        raise TypeError("Os inputs devem ser do tipo float ou int")
    
def divisao(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        a, b = float(a), float(b)
        if b != 0:
            return a/b
        else:
            raise ZeroDivisionError("Divisão por zero!")
    else:
        raise TypeError("Os inputs devem ser do tipo float ou int")
    
def multiplicacao(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return float(a) * float(b)
    else:
        raise TypeError("Os inputs devem ser do tipo float ou int")

