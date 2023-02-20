def addNum(num):
    sum = 0
    while num > 0:
        rem = num % 10
        sum += rem
        num //= 10
    return sum

def addDigits(num):
    # Solution 1
    # while num > 9:
    #     num = addNum(num)
    # return num

    # Solution 2
    if num == 0:
        return 0
    elif num%9 == 0:
        return 9
    else:
        return num%9

print(addDigits(-1))