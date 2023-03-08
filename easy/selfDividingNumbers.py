def dividingNums(num):
    n = num
    while n > 0:
        rem = n%10
        if rem == 0 or num%rem != 0:
            return False
        n //= 10
    return True

def selfDividingNumbers(left, right):
    res = []
    for i in range(left, right+1):
        if dividingNums(i):
            res.append(i)
    return res

print(selfDividingNumbers(left = 66, right = 709))