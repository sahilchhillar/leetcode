def isPerfectSquare(n):
    low, high = 1, n

    while low <= high:
        mid = (high+low)//2
        if mid * mid == n:
            return True
        elif mid * mid < n:
            low = mid + 1
        else:
            high = mid - 1
    return False

print(isPerfectSquare(17))