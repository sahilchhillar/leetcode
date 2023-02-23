def longestPalindrome(s):
    counts = {}
    for i, char in enumerate(s):
        if counts.get(char) is None:
            counts[char] = 1
        else:
            counts[char] += 1
    
    result, odd_found = 0, False

    for key, val in counts.items():
        if val%2 == 0:
            result += val
        else:
            odd_found = True
            result += val-1
        
    if odd_found:
        result += 1
    return result

print(longestPalindrome("abccccdd"))