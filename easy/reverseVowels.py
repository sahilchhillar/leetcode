def reverseVowels(s: str):
    vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
    arr = []
    for i in range(len(s)):
        arr.append(s[i])
    print(arr)

    low, high = 0, len(arr)-1

    while low <= high:
        if arr[low] not in vowels:
            low += 1
        if arr[high] not in vowels:
            high -= 1
        
        else:
            if arr[high] in vowels and arr[low] in vowels:
                arr[low], arr[high] = arr[high], arr[low]
                low += 1
                high -= 1
    
    return ''.join(arr)

print(reverseVowels("a"))