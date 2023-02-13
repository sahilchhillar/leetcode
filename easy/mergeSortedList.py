def mergeSortedList(nums1: list, m: int, nums2: list, n:int):
    ptr = m + n - 1

    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[ptr] = nums1[m-1]
            m -= 1
        else:
            nums1[ptr] = nums2[n-1]
            n -= 1
        ptr -= 1
    
    while n > 0:
        nums1[ptr] = nums2[n-1]
        n -= 1
        ptr -= 1
    
    return nums1


print(mergeSortedList([2, 0], 1, [1], 1))