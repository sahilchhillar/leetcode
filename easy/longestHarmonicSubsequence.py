def longestHarmonicSubsequence(nums):
    seqCount = {}

    for num in nums:
        if seqCount.get(num) is None:
            seqCount[num] = 1
        else:
            seqCount[num] += 1

    maxLen = 0

    for seq in seqCount:
        if seq+1 in seqCount:
            maxLen = max((seqCount[seq] + seqCount[seq+1]), maxLen)
    return maxLen

print(longestHarmonicSubsequence(nums = [1,1,1,1]))