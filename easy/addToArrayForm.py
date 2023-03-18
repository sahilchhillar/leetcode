def addToArrayForm(nums, k):
    carry = 0
    for i in range(len(nums)-1, -1, -1):
        rem = k%10
        k //= 10
        nums[i] += rem+carry
        if nums[i] > 9:
            nums[i] %= 10
            carry = 1
        else:
            carry = 0
    
    if k > 0:
        while k > 0:
            rem = k%10
            k //= 10
            rem = rem+carry
            if rem > 9:
                nums.insert(0, rem%10)
                carry = 1
            else:
                nums.insert(0, rem)
                carry = 0
    
    if carry:
        nums.insert(0, 1)
    return nums

print(addToArrayForm(nums = [2,1,5], k = 806))        