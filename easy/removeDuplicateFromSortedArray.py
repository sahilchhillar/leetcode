def removeDuplicateFromSortedArray(nums):
    k = 0
    for i in range(len(nums)):
        if nums[i] == nums[i+1]:
            continue
        elif nums[i] != nums[i+1]:
            nums[k+1] = nums[i+1]
            k += 1
    return k+1
    

nums = [3,2,2,3]
val = removeDuplicateFromSortedArray(nums)
print(nums[:val])