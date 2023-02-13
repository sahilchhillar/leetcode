def validPalindrome(s):
    s = s.lower()
    low, high = 0, len(s)-1

    while low < high:
        while low < high and not s[low].isalnum():
            low += 1
        
        while low < high and not s[high].isalnum():
            high -= 1

        if s[low].isalnum() and s[high].isalnum() and s[low] != s[high]:
            return False
        
        low += 1
        high -= 1
    
    return True


print(validPalindrome("Fb Ley'?P:\"'I\":P?IyeL bF"))