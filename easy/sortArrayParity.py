def sortArrayParity(nums):
    low, high = 0, len(nums)-1

    while low <= high:
        if nums[low]%2 == 1 and nums[high]%2 == 0:
            nums[low], nums[high] = nums[high], nums[low]
        
        if nums[low]%2 == 0:
            low += 1
        if nums[high]%2 == 1:
            high -= 1

    print(nums)

sortArrayParity(nums = [0,1,2,3,4,5,6,7,8])