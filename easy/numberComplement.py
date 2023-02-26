def numberComplement(n):
    n = 0
    i = 0
    while c > 0:
        lastBit = not c&1
        n += lastBit*pow(2, i)
        i += 1
        c >>= 1
    return n
    
print(numberComplement(5))