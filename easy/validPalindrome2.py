def validPalindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # Try deleting either the left or right character and check if the resulting string is a palindrome
            return isPalindrome(s, left+1, right) or isPalindrome(s, left, right-1)
        left += 1
        right -= 1
    return True

def isPalindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(validPalindrome(s = "aba"))