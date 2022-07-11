def solution(xs):
    p = [i for i in xs if i > 0]
    n = [i for i in xs if i < 0]
    
    if max(xs) == 0:
        return '0'
    
    if len(p) == 0 and len(n) == 0:
        return '0'
    
    if len(n) %2 !=0:

        if len(n) == 1 and len(p) == 0:
            return str(n[0])
        
        n.sort()
        n.pop()
        
    if p or n:
        
        prod = 1
        
        for x in p + n:
            prod = prod * x
                
        return str(prod)
        
    return '0'
    
