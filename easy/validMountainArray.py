def validMountainArray(arr):
    if len(arr) < 3:
        return False

    i = 0

    while i < len(arr)-1:
        if arr[i] < arr[i+1]:
            i += 1
        else:
            break
    
    if i == 0 or i == len(arr)-1:
        return False
    
    while i < len(arr)-1:
        if arr[i] > arr[i+1]:
            i += 1
        else:
            break
    
    return i == len(arr)-1

print(validMountainArray(arr = [4,3,2,1]))