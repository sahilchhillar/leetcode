# Solution 1
def happyNumber(n):
    visited = set()

    while n not in visited:
        visited.add(n)
        n = sumOfSquares(n)
        if n == 1:
            return True
    return False

def sumOfSquares(n):
    output = 0
    while n:
        digit = n%10
        digit = digit**2
        output += digit
        n //= 10
    return output


# Solution 2
def isHappy(n):
    slow, fast = n, n

    slow = sumOfSquares(slow)
    fast = sumOfSquares(slow)
    fast = sumOfSquares(fast)

    while slow != fast:
        slow = sumOfSquares(slow)
        fast = sumOfSquares(slow)
        fast = sumOfSquares(fast)
    
    if slow == 1:
        return True
    return False


print(isHappy(19))