def powerOfTwo(n):
    if n == 0:
        return False
    
    return n == 1 or (n%2 == 0 and powerOfTwo(n//2))

print(powerOfTwo(1))