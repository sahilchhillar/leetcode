def longestIncreasingSubSequence(nums):
    longest = 0
    i = 0
    count = 1
    while i < len(nums)-1:
        if nums[i] < nums[i+1]:
            count += 1
        else:
            longest = max(count, longest)
            count = 1
        i += 1
    
    return max(longest, count)

print(longestIncreasingSubSequence(nums = [1,1,1]))