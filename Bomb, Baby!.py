def solution(x, y):
    # Your code here
    
    x, y = int(x), int(y)

    yeah = 0
    while (x != 1 and y != 1):
        if x % y == 0:
            return "impossible"
        else:

            yeah = yeah +int(max(x, y)/min(x, y))
            x, y = max(x, y) % min(x, y), min(x, y)
    return str(yeah+max(x, y)-1)
