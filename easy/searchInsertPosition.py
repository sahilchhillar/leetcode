def searchInsertPosition(nums, target):
    l, r, mid = 0, len(nums), 0

    while l <= r:
        mid = (l+r)//2

        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            l = mid+1
        else:
            r = mid-1
    
    return l


print(searchInsertPosition([1,3,5,6], 2))