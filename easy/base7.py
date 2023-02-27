def base7(num):
    ans = 0
    i = 0
    sign = 'N' if num < 0 else 'P'
    num = abs(num)
    while num > 0:
        rem = num%7
        ans += rem*pow(10,i)
        i += 1
        num //= 7
    
    if sign == 'N':
        ans *= -1
    return str(ans)

print(base7(-7))