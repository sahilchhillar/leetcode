def removeElement(nums, target):
    index = 0
    for i in range(len(nums)):
        if nums[i] == target:
            continue
        else:
            nums[index] = nums[i]
            index += 1
    return index


nums = [3,2,2,3]
target = 3

val = removeElement(nums, target)
print(nums[:val])