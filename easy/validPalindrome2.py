def isPalindrome(s, low, high):
    while low <= high:
        if s[low] != s[high]:
            return False
    return True

def validPalindrome(s):
    low, high, count = 0, len(s)-1, 0

    while low <= high:
        if s[low] != s[high]:
            if not (isPalindrome(s, low+1, high) or isPalindrome(s, low, high-1)):
                return False
        low += 1
        high -= 1
    return True

print(validPalindrome(s = "abca"))