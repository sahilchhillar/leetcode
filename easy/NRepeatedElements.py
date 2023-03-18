def repeatedElements(nums):
    count = {}
    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            return num

print(repeatedElements(nums = [1,2,3,3]))