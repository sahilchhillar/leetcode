def reverse(s):
    arr = list(s)
    low, high = 0, len(arr)-1
    while low <= high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
    return ''.join(arr)

def reverseString3(s):
    # Solution 1
    # arr = s.split(' ')
    # for i in range(len(arr)):
    #     arr[i] = reverse(arr[i])
    # return ' '.join(arr)

    # Solution 2
    temp = ""
    new_s = ""

    for i, char in enumerate(s):
        if char != ' ':
            temp += char
        else:
            new_s += temp[::-1] + ' '
            temp = ""
    
    if temp != "":
        new_s += temp[::-1]
    return new_s
        

print(reverseString3(s = "Let's take LeetCode contest"))