def isPowerOfThree(n: int):
    if n == 0:
        return False

    return n == 1 or (n%3 == 0 and isPowerOfThree(n//3))