def summaryRanges(nums):
    ranges = []

    begin = nums[0]
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1] or nums[i]+1 == nums[i+1]:
            continue
        else:
            if begin == nums[i]:
                string = f'{begin}'
                ranges.append(string)
            else:
                string = f'{begin}->{nums[i]}'
                ranges.append(string)
            begin = nums[i+1]
    
    if begin == nums[len(nums)-1]:
        string = f'{begin}'
    else:
        string = f'{begin}->{nums[len(nums)-1]}'
    ranges.append(string)

    return ranges


print(summaryRanges(nums = [0,0,2,3,4,6,8,9]))