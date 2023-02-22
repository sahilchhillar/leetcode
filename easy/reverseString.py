def reverseString(s: list):
    low, high = 0, len(s)-1

    while low <= high:
        s[low], s[high] = s[high], s[low]
        low += 1
        high -= 1
    
    return s