def monotonicArray(nums):
    ascending, descending = 1, 1

    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            ascending += 1
        elif nums[i] > nums[i+1]:
            descending += 1
        else:
            ascending += 1
            descending += 1

    return ascending == len(nums) or descending == len(nums)

print(monotonicArray(nums = [6,5,4,4]))