def binarySearch(nums, target):
    low, high = 0, len(nums)-1
    mid = (high+low)//2
    while low <= high:
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid+1
        else:
            high = mid-1
        mid = (high+low)//2
    return -1

print(binarySearch(nums = [-1,0,3,5,9,12], target = 9))