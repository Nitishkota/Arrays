def findMedianSortedArrays(nums1, nums2):
    
    merged = sorted(nums1 + nums2)
    n = len(merged)
    if n % 2 == 1:
        return float(merged[n // 2])
    else:
        mid1 = merged[n // 2 - 1]
        mid2 = merged[n // 2]
        return (mid1 + mid2) / 2.0

# Example usage:
nums1 = [1, 3]
nums2 = [2]
median = findMedianSortedArrays(nums1, nums2)
print(median)

nums1 = [1, 2]
nums2 = [3, 4]
median = findMedianSortedArrays(nums1, nums2)
print(median)