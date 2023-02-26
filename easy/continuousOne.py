def continousOne(nums):
    count = 0
    max_one = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            max_one = max(count, max_one)
            count = 0
    if count != 0:
        max_one = max(count, max_one)
    return max_one

print(continousOne(nums = [1,0,0,1,1,0,1]))