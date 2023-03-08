def pivotIndex(nums):
    s = sum(nums)
    left = 0
    for i, num in enumerate(nums):
        if left == (s-left-num):
            return i
        left += num
    return -1

print(pivotIndex(nums = [-1,-1,-1,-1,0,1]))