def containDuplicate(nums):
    # Solution 1
    # duplicate = {}

    # for num in nums:
    #     if duplicate.get(num) is None:
    #         duplicate[num] = 1
    #     else:
    #         return True
    # return False

    # Solution 2
    # nums = sorted(nums)

    # for i in range(len(nums)-1):
    #     if nums[i] == nums[i+1]:
    #         return True
    # return False

    # Solution 3
    num_set = set(nums)
    if len(num_set) != len(num_set):
        return True
    return False

print(containDuplicate([1]))