def soma(a, b):
    if (type(a) == type(5) or type(a) == type(0.5)) and (type(b) == type(5) or type(b) == type(0.5)):
        return float(a) + float(b)
    else:
        raise TypeError("Os inputs devem ser do tipo float ou int")
    

