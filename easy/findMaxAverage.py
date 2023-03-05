def findMaxAverage(nums, k):
    maxSum = sum(nums[:k])
    start, end = 0, k-1
    ele = maxSum

    while end+1 < len(nums):
        ele = ele - nums[start] + nums[end+1]
        maxSum = max(ele, maxSum)
        start += 1
        end += 1
    
    return maxSum/k

print(findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))