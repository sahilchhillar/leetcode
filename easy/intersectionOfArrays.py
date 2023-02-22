def intersectionOfArrays(nums1, nums2: list):
    nums1.sort()
    nums2.sort()
        
    ans = set()
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            ans.add(nums1[i])
            i += 1
            j += 1
    return list(ans)

print(intersectionOfArrays([4,5,9], [9,4,4,9,8]))