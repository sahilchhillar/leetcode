def reverse(arr, low, high):
    while low <= high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
    return arr

def reverseString2(s, k):
    arr = list(s)
    i = 0

    while i <= len(arr):
        if (i+k-1) >= len(arr):
            arr = reverse(arr, i, len(arr)-1)
        else:
            arr = reverse(arr, i, i+k-1)
        i += 2*k

    return ''.join(arr)

print(reverseString2(s = "abcdefg", k = 9))