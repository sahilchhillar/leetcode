def moveZeros(nums):
    zeroPointer = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            if nums[zeroPointer] != 0:
                zeroPointer = i+1
            else:
                nums[i], nums[zeroPointer] = nums[zeroPointer], nums[i]
                zeroPointer += 1
    
    print(nums)



moveZeros(nums = [1,1,0,0,3,12])