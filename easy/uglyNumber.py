def uglyNumber(num):
    if num == 1:
        return True
    
    factors = [2,3,5]

    for factor in factors:
        while num%factor == 0:
            num //= factor
    
    return num == 1


print(uglyNumber(8))