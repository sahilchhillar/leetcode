def containsNearbyDuplicate(nums, k):
    duplicate = {}

    for i in range(len(nums)):
        if duplicate.get(nums[i]) is None:
            duplicate[nums[i]] = i
        else:
            if abs(duplicate[nums[i]] - i) <= k:
                return True
            else:
                duplicate[nums[i]] = i

    return False


print(containsNearbyDuplicate(nums = [1,0,1,1], k = 1))