def majorityElement(nums):
    majority = len(nums)//2

    occurrences = {}

    for num in nums:
        if occurrences.get(num) is None:
            occurrences[num] = 1
        else:
            occurrences[num] += 1
            if occurrences[num] > majority:
                return num
    
    return -1


print(majorityElement([2,2,1,1,1,2,2]))