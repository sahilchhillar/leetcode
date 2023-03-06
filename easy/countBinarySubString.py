def countBinarySubString(s):
    nums = []
    count = 1
    s += '2'
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            nums.append(count)
            count = 1
    
    ans = 0
    for i in range(1, len(nums)):
        ans += min(nums[i], nums[i-1])
    
    return ans
        
print(countBinarySubString(s = "10101"))