def reverse(x):
    x_rev = 0
    while x > 0:
        rem = x % 10
        x = x // 10
        x_rev = x_rev*10 + rem
    return x_rev

def palindromeNumber(x):
    if x < 0:
        return False
    
    # O(n)
    x_rev = reverse(x)
    if x_rev == x:
        return True
    return False


print(palindromeNumber(121))