def reverseOnlyLetters(s):
    low, high = 0, len(s)-1
    s = list(s)

    while low <= high:
        if s[low].isalpha() and s[high].isalpha():
            s[low], s[high] = s[high], s[low]
            low += 1
            high -= 1
        
        elif not s[low].isalpha():
            low += 1
        elif not s[high].isalpha():
            high -= 1
    
    return ''.join(s)


print(reverseOnlyLetters(s = "a"))