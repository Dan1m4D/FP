def closertoTarget(x, y, target):
    
    dif1 = abs(target - x)
    dif2 = abs(target - y)
    
    if x == y:
        return print("os nº são iguais")
    else:
        if dif1 == dif2:
            if x > y:
                return y
            else:
                return x
            
             
        